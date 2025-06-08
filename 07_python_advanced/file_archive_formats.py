# 07_python_advanced/file_archive_formats.py

# Archive modules

# zipfile   → ZIP (multi-file archives)
# tarfile   → TAR, TAR.GZ, TAR.BZ2 (flexible, hierarchical)
# gzip      → compress one file (stream or .gz)
# bz2       → one-file compression, better ratio than gzip
# lzma      → one-file compression (.xz), high ratio

# shutil.make_archive / unpack_archive → high-level creation/extraction


# ZIP archives with zipfile
import zipfile
from pathlib import Path

# Create ZIP
with zipfile.ZipFile("archive.zip", "w") as z:
    z.write("example.txt")
    z.writestr("in_memory.txt", "This is written from a string.")

# List contents
with zipfile.ZipFile("archive.zip", "r") as z:
    print("ZIP contents:", z.namelist())

# Extract files
with zipfile.ZipFile("archive.zip", "r") as z:
    z.extractall("unzipped_folder")

# Read file content from archive
with zipfile.ZipFile("archive.zip") as z:
    with z.open("example.txt") as f:
        print("Read from zip:", f.read().decode("utf-8"))


# TAR and compressed TARs with tarfile
import tarfile

# Create uncompressed TAR
with tarfile.open("archive.tar", "w") as tar:
    tar.add("example.txt")

# Create gzipped TAR
with tarfile.open("archive.tar.gz", "w:gz") as tar:
    tar.add("example.txt")

# Extract all
with tarfile.open("archive.tar.gz", "r:gz") as tar:
    tar.extractall("tar_extracted")

# List contents
with tarfile.open("archive.tar.gz", "r:gz") as tar:
    print("TAR contents:")
    for member in tar.getmembers():
        print(member.name)

# Read a file from tar directly
with tarfile.open("archive.tar.gz", "r:gz") as tar:
    member = tar.getmember("example.txt")
    f = tar.extractfile(member)
    if f:
        print("From tar:", f.read().decode("utf-8"))


# GZIP (single-file compression)
import gzip

# Write compressed file
with gzip.open("compressed.txt.gz", "wt") as f:
    f.write("This is gzip-compressed text.")

# Read compressed file
with gzip.open("compressed.txt.gz", "rt") as f:
    text = f.read()
    print("From gzip:", text)


# BZ2 compression
import bz2

data = b"This is some binary data." * 10

# Write bz2
with bz2.open("data.bz2", "wb") as f:
    f.write(data)

# Read bz2
with bz2.open("data.bz2", "rb") as f:
    print("BZ2 read:", f.read())


# LZMA / .xz compression
import lzma

# Compress to file
with lzma.open("data.xz", "wb") as f:
    f.write(data)

# Read from .xz
with lzma.open("data.xz", "rb") as f:
    print("XZ read:", f.read())


# Practical tips

# - Use zipfile/tarfile for multi-file archives
# - Use gzip/bz2/lzma for single large files
# - Combine with `pathlib` for clean file management
# - Always use context managers (`with ...`) to avoid file leaks
# - Use `writestr()` in zipfile to avoid temporary files
