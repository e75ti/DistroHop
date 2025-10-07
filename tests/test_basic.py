import os
import tarfile
import json
import pytest
import sys

try:
    import compression.zstd as zstd
except Exception:
    zstd = None

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from linux_migration_tool import create_backup

def _collect_names_from_tarfile_obj(tar):
    names = []
    for member in tar:
        names.append(member.name)
    return names

def test_create_backup_generates_archive(tmp_path):
    dest = tmp_path
    # sample files and directory to include
    f1 = dest / "file1.txt"
    f1.write_text("hello")
    d1 = dest / "somedir"
    d1.mkdir(parents=True, exist_ok=True)
    (d1 / "nested.txt").write_text("nested")

    selected = [str(f1), str(d1)]
    apps = ["example-app"]

    success, archive_path = create_backup(selected, apps, str(dest))
    assert success is True
    assert os.path.exists(archive_path)

    if archive_path.endswith(".tar.gz"):
        with tarfile.open(archive_path, "r:gz") as tar:
            names = tar.getnames()
            # archive should contain the files (may include relative paths) and manifest.json
            assert any(name.endswith("file1.txt") for name in names)
            assert any("manifest.json" == os.path.basename(name) for name in names)
            # verify manifest content
            # find the manifest member name
            mname = next(n for n in names if os.path.basename(n) == "manifest.json")
            mf = tar.extractfile(mname)
            manifest = json.load(mf)
            assert manifest["apps"] == apps

    elif archive_path.endswith(".tar.zst"):
        if zstd is None:
            pytest.skip("compression.zstd not available in this environment")
        # stream-decompress and iterate members
        with zstd.open(archive_path, "rb") as zf:
            with tarfile.open(fileobj=zf, mode="r|") as tar:
                names = _collect_names_from_tarfile_obj(tar)
                assert any(name.endswith("file1.txt") for name in names)
                assert any(os.path.basename(name) == "manifest.json" for name in names)
    else:
        pytest.fail(f"Unexpected archive extension: {archive_path}")