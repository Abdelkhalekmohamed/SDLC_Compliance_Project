import os
import logging
from compliance_check import download_files, run_bandit

# Configure logging
logging.basicConfig(level=logging.INFO)

# GitHub repository URL
GITHUB_REPO_URL = 'https://api.github.com/repos/Abdelkhalekmohamed/SDLC_Compliance_Project/contents/'

if __name__ == "__main__":
    local_dir = 'repo_files'
    os.makedirs(local_dir, exist_ok=True)
    download_files(GITHUB_REPO_URL, local_dir)
    run_bandit(local_dir)

