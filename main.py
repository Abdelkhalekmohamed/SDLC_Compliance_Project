import os
import logging
from compliance_check import run_bandit

# Configure logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    local_dir = 'repo_files'  # Directory where your cloned files are located
    if not os.path.exists(local_dir):
        logging.error(f"Directory {local_dir} does not exist. Please ensure the repository is cloned correctly.")
    else:
        run_bandit(local_dir)
