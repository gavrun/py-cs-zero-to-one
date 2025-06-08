# 07_python_advanced/standard_library_os_linux.py

import os
import subprocess
from pathlib import Path
import tempfile
import shutil

# OS and environment
print("OS name:", os.name)             # 'posix'
print("Platform:", os.sys.platform)    # 'linux'
print("User:", os.environ.get("USER"))
print("Home:", os.environ.get("HOME"))

# Current working directory
print("Current dir:", os.getcwd())

# Change directory
# os.chdir("/var/www")

# Environment variables
os.environ["APP_ENV"] = "development"
print("PATH:", os.environ.get("PATH"))

# Working with paths (pathlib recommended)
log_dir = Path.home() / "logs"
log_dir.mkdir(exist_ok=True)

log_file = log_dir / "output.log"
with log_file.open("w") as f:
    f.write("Log start\n")

print("Log path:", log_file.resolve())

# File and directory management
Path("build").mkdir(exist_ok=True)
Path("build/tmp.txt").write_text("temp")

if Path("build/tmp.txt").exists():
    Path("build/tmp.txt").unlink()  # delete file

shutil.rmtree("build", ignore_errors=True)

# Running shell commands
# subprocess safer than os.system
res = subprocess.run("ls -la", shell=True, capture_output=True, text=True)
print("LS output:\n", res.stdout)

# Example with arguments
subprocess.run(["touch", "script_output.txt"])

# Getting uname, df, free, etc.
print("Uname:", subprocess.run(["uname", "-a"], capture_output=True, text=True).stdout)

# Reading logs (practice example)
with open("/var/log/syslog", "r") as log:
    for line in log:
        if "error" in line.lower():
            print("Syslog error:", line.strip())

# Checking file/directory/permissions availability
f = Path("/etc/passwd")
print("Readable?", os.access(f, os.R_OK))
print("Writable?", os.access(f, os.W_OK))

# Getting process information
print("PID:", os.getpid())
print("Parent PID:", os.getppid())

# Creating temporary file/directory
with tempfile.TemporaryDirectory() as tmpdir:
    print("Temp dir:", tmpdir)

with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
    tmp.write("temp data")
    print("Temp file:", tmp.name)

# Working with access rights
# os.chmod("file.txt", 0o644)
# os.chown("file.txt", uid, gid)  # sudo may be needed

# Cron job (create via crontab)
cron_line = "@daily python3 /home/user/scripts/backup.py >> /home/user/cron.log 2>&1"
subprocess.run(f'(crontab -l; echo "{cron_line}") | crontab -', shell=True)

# systemd unit (creating a simple user service)
service = """
[Unit]
Description=My Python App

[Service]
ExecStart=/usr/bin/python3 /home/user/app.py
Restart=always

[Install]
WantedBy=default.target
"""

unit_file = Path.home() / ".config/systemd/user/myapp.service"
unit_file.write_text(service)

# Activate (in console): systemctl --user daemon-reload && systemctl --user enable --now myapp

# Working with stdin/stdout (pipe-like)
p = subprocess.run(["grep", "root"], input="root:x:0:0:root\nuser:x:1000:1000:user\n",
                   text=True, capture_output=True)
print("Grep result:\n", p.stdout)

# Working with Bash variables and aliases
bashrc = Path.home() / ".bashrc"
bashrc.write_text('alias myrun="python3 ~/app.py"\n', append=True)

# Deleting large folders via shell
# subprocess.run(["rm", "-rf", "/tmp/mybigfolder"])

# Process signals
import signal

# os.kill(pid, signal.SIGTERM)  # stop process

# Security practices

# - Do not run shell=True with uncontrolled input
# - Check permissions and errors
# - Use try/except when working with the file system
# - Do not use os.system — subprocess is safer

# Additionally

# - For daemons: systemd, supervisord
# - For packaging: pyinstaller, shiv
# - For logs: logging + /var/log/
# - For user config: XDG spec (~/.config/)

