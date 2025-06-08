# 07_python_advanced/subprocess_intro.py

# Run external programs and interact with their input/output/error pipes.
# Use instead of os.system(). More control, safer, portable.

# subprocess.run([...])           → safest and most common pattern
# subprocess.Popen([...])         → for advanced streaming/interaction
# subprocess.check_output([...])  → quick one-liners (returns stdout)

import subprocess


# Basic: run command and wait

# Returns CompletedProcess object
result = subprocess.run(["echo", "Hello from subprocess"], capture_output=True, text=True)

print("Exit code:", result.returncode)
print("Output:", result.stdout.strip())


# Check for errors
try:
    subprocess.run(["ls", "/nonexistent"], check=True)
except subprocess.CalledProcessError as e:
    print("Command failed with return code", e.returncode)

# Capture both stdout and stderr
result = subprocess.run(
    ["python", "-c", "print('out'); import sys; sys.stderr.write('err\\n')"],
    capture_output=True,
    text=True
)

print("STDOUT:", result.stdout.strip())
print("STDERR:", result.stderr.strip())


# Pipe output to another subprocess
# (like `ls | grep py`)
p1 = subprocess.Popen(["ls"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["grep", "py"], stdin=p1.stdout, stdout=subprocess.PIPE, text=True)
p1.stdout.close()
output, _ = p2.communicate()
print("Filtered:", output)

# Pass input to command
result = subprocess.run(
    ["grep", "apple"],
    input="apple\nbanana\ncarrot",
    text=True,
    capture_output=True
)
print("Grep result:", result.stdout.strip())


# Get output directly with check_output
output = subprocess.check_output(["echo", "quick"], text=True)
print("check_output result:", output.strip())


# Run command in shell (be careful with untrusted input!)
result = subprocess.run("echo $HOME", shell=True, capture_output=True, text=True)
print("Shell output:", result.stdout.strip())

# Windows: use "dir", "type", etc.
# Linux/macOS: use "ls", "cat", etc.

# - shell=True: run through shell (use with caution!)
# - capture_output=True: shortcut for stdout=PIPE, stderr=PIPE
# - text=True: decode bytes to str (Python 3.7+)
# - check=True: raises CalledProcessError on non-zero exit

