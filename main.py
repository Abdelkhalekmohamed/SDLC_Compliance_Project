import os
import logging
from compliance_check import run_bandit

# Configure logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    # Define the local directory where the cloned repository files are stored
    local_dir = 'repo_files'

    # Check if the specified local directory exists
    if not os.path.exists(local_dir):
        # Log an error message if the directory does not exist
        logging.error(f"Directory {local_dir} does not exist. Please ensure the repository is cloned correctly.")
    else:
        # If the directory exists, run the Bandit security analysis
        run_bandit(local_dir)
