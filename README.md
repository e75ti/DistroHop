> 📌 **Note:** This is a **fork** of the original [Linux Migration Tool](https://github.com/ORIGINAL_REPO_LINK_HERE).  
> I've made several enhancements, including:
> - **Zstandard (zstd) compression** support for faster and more efficient backups
> - Code **refactoring** for improved readability and maintainability
> - Added **GitHub Actions** for automated CI checks
> These changes aim to modernize and improve the tool while maintaining its original purpose and simplicity.  
> Contributions, feedback, and suggestions are welcome!


<h1 align="center">📦 Linux Migration Tool</h1>
    <p align="center">A simple CLI tool for backing up and restoring user files and applications on Linux.</p>

<h2>🚀 About</h2>
    <p>The <b>Linux Migration Tool</b> helps users back up important files, configurations, and installed applications and restore them on a new system. This tool simplifies migration between Linux distributions or after a fresh installation.</p>

<h2>🎯 Features</h2>
    <ul>
        <li>✔️ Backup & Restore: Save and restore user files, configurations, and installed applications.</li>
        <li>✔️ USB Detection: Automatically detects connected USB drives for storage.</li>
        <li>✔️ Application Backup: Detects installed applications and saves a list for reinstallation.</li>
        <li>✔️ Package Manager Support: Works with <code>apt</code>, <code>dnf</code>, <code>yum</code>, <code>pacman</code>, and <code>flatpak</code>.</li>
        <li>✔️ User-Friendly CLI: Simple menu-driven interface for easy navigation.</li>
        <li>✔️ Efficient Archiving: Uses compressed <code>.tar.gz</code> format for optimal storage.</li>
    </ul>

<h2>📥 Installation</h2>

<h3>🛠️ Prerequisites</h3>
    <ul>
        <li>Python 3.x</li>
        <li>A Linux-based operating system (Debian, Ubuntu, Fedora, Arch, etc.)</li>
        <li>USB storage for backups</li>
    </ul>

<h3>🔧 Setup</h3>
    <pre>
git clone https://github.com/bobomrac/DistroHop.git
cd DistroHop
chmod +x linux_migration_tool.py
./linux_migration_tool.py
    </pre>

<h2>🏗️ Usage</h2>
    <p>Run the tool and follow the on-screen instructions:</p>
    <pre>python3 linux_migration_tool.py</pre>

<h3>📤 Export Backup:</h3>
    <ol>
        <li>Select a USB drive for the backup.</li>
        <li>Choose which files and directories to back up.</li>
        <li>Choose installed applications to save for later reinstallation.</li>
        <li>Confirm and create the backup.</li>
    </ol>

<h3>📥 Import Restore:</h3>
    <ol>
        <li>Select a USB drive containing the backup.</li>
        <li>Choose the backup file to restore.</li>
        <li>Restore files to your home directory.</li>
        <li>Reinstall previously installed applications.</li>
    </ol>

<h2>🖥️ Supported Package Managers</h2>
    <ul>
        <li><b>apt</b> (Debian, Ubuntu)</li>
        <li><b>dnf</b> (Fedora)</li>
        <li><b>yum</b> (CentOS, RHEL)</li>
        <li><b>pacman</b> (Arch Linux, Manjaro)</li>
        <li><b>zypper</b> (openSUSE)</li>
        <li><b>flatpak</b> (Universal package manager)</li>
    </ul>



 <h2>🛠️ Troubleshooting</h2>

 <h3>❌ USB Drive Not Detected?</h3>
    <ul>
        <li>Ensure the USB is mounted.</li>
        <li>Run <code>lsblk</code> to check if it appears.</li>
        <li>Try running the tool with <code>sudo</code>.</li>
    </ul>

 <h3>❌ Backup Failed?</h3>
    <ul>
        <li>Ensure the USB has enough free space.</li>
        <li>Run <code>df -h</code> to check available disk space.</li>
        <li>Try running with <code>sudo</code> if permission issues occur.</li>
    </ul>

 <h3>❌ Apps Not Restored?</h3>
    <ul>
        <li>Some packages may have different names in different distros.</li>
        <li>Use <code>apt search package-name</code> or <code>dnf list available | grep package-name</code> to manually find missing apps.</li>
    </ul>


</div>

</body>
</html>
