#!/bin/bash

# Define directories for the generated files
DEB_DIST_DIR=./deb_dist
DIST_DIR=./dist

# Clean up the previous build directories, including the .egg-info directory
rm -rf "${DEB_DIST_DIR}" ./*.egg-info

# Build the Debian package
python3 setup.py --command-packages=stdeb.command bdist_deb

# Remove .tar.gz files from the root directory
rm -f ./*.tar.gz
echo ".tar.gz files in the root directory have been removed."

# Notify user of build completion and cleanup actions
echo "Build environment cleaned up, .tar.gz files removed from the root directory, and package built."

