import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Directory to check for duplicates
project_directory = 'repo_files'
root_directory = '.'  # Root of the project

# List all files in repo_files
repo_files = []
for root, dirs, files in os.walk(project_directory):
    for file in files:
        repo_files.append(os.path.relpath(os.path.join(root, file), start=project_directory))

# Delete duplicate files from the root directory
for file in repo_files:
    root_file_path = os.path.join(root_directory, file)
    if os.path.exists(root_file_path):
        os.remove(root_file_path)
        logging.info(f"Deleted duplicate file from root: {root_file_path}")

logging.info("Cleanup completed.")
