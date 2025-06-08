# 07_python_advanced/standard_library_os_windows.py

import os
import subprocess
from pathlib import Path
import tempfile
import shutil

# Basic information about the system
print("OS name:", os.name)           # 'nt' on Windows
print("Platform:", os.sys.platform)  # 'win32'

# Current working directory
print("Current dir:", os.getcwd())

# Changing the working directory
# os.chdir(r"C:\Users")

# Environment variables
print("USERNAME:", os.environ.get("USERNAME"))
print("USERPROFILE:", os.environ.get("USERPROFILE"))
print("PATH:", os.environ.get("PATH"))

# Setting an environment variable for the duration of the script
os.environ["MY_ENV_VAR"] = "value"

# Working with paths (os.path / pathlib)
user_dir = os.path.join(os.environ["USERPROFILE"], "Desktop")
print("Desktop path:", user_dir)

path = Path("C:/Windows/System32")
print("Is absolute?", path.is_absolute())
print("Exists?", path.exists())

# Create/delete directories and files
folder = Path("C:/Temp/my_script_logs")
folder.mkdir(parents=True, exist_ok=True)

with open(folder / "log.txt", "w") as f:
    f.write("Windows log initialized.\n")

os.remove(folder / "log.txt")
shutil.rmtree(folder)

# Enumerate files and directories
for root, dirs, files in os.walk("C:\\Windows\\System32"):
    for name in files:
        if name.endswith(".dll"):
            print("Found DLL:", os.path.join(root, name))
    break  # не рекурсивно

# Executing system commands (safer subprocess)
# subprocess.run returns CompletedProcess (exit code, output, etc.)

# Open Notepad
subprocess.run(["notepad.exe"])

# Run dir and get the result
result = subprocess.run(["cmd", "/c", "dir"], capture_output=True, text=True)
print("DIR output:\n", result.stdout)

# PowerShell example
ps = subprocess.run(["powershell", "-Command", "Get-Date"], capture_output=True, text=True)
print("Date:", ps.stdout.strip())

# Temporary files and directories
with tempfile.TemporaryDirectory() as tmpdir:
    print("Temp dir:", tmpdir)

with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
    tmpfile.write(b"debug log")
    print("Temp file:", tmpfile.name)

# File metadata
file_path = "C:\\Windows\\notepad.exe"
if os.path.exists(file_path):
    stat = os.stat(file_path)
    print("Size:", stat.st_size, "bytes")

# Getting a list of disks (Windows)
drives = [f"{d}:\\" for d in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if os.path.exists(f"{d}:\\")]
print("Drives:", drives)

# Managing File Attributes (Windows)
import ctypes
FILE_ATTRIBUTE_HIDDEN = 0x02

# Hide file
ctypes.windll.kernel32.SetFileAttributesW("secret.txt", FILE_ATTRIBUTE_HIDDEN)

# Script autoload (creating a .bat file or shortcut in Startup)
startup = Path(os.environ["APPDATA"]) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"
bat = startup / "myscript.bat"

with open(bat, "w") as f:
    f.write(f'@echo off\npython "{Path(__file__).resolve()}"\n')

print("Autostart script created at:", bat)

# Working with the Windows Registry (via winreg)
import winreg

with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment", 0, winreg.KEY_READ) as key:
    try:
        val, _ = winreg.QueryValueEx(key, "TEMP")
        print("User TEMP path:", val)
    except FileNotFoundError:
        print("TEMP not set")

# Launching and managing processes
p = subprocess.Popen(["notepad.exe"])
p.wait()  # Wait for completion

# System sound (Beep)
import winsound
winsound.Beep(1000, 500)  # 1kHz, 500ms


# Best practices

# - Use pathlib for paths
# - subprocess is safer than os.system
# - Respect permissions (admin)
# - Log errors and execution path

