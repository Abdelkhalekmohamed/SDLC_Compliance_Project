import os
import requests
import logging
import subprocess
import csv

# Configure logging to display information and error messages
logging.basicConfig(level=logging.INFO)

# GitHub repository URL for fetching contents
GITHUB_REPO_URL = 'https://api.github.com/repos/Abdelkhalekmohamed/SDLC_Compliance_Project/contents/'

# Optional: Use your GitHub token for authentication if the repository is private
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')  # Store your token in an environment variable for security


# Function to download files from a GitHub repository
def download_files(repo_url, local_directory):
    headers = {}
    if GITHUB_TOKEN:
        headers['Authorization'] = f'token {GITHUB_TOKEN}'

    response = requests.get(repo_url, headers=headers)  # Make a GET request to fetch repository contents
    logging.info(f"Fetching URL: {repo_url}")
    logging.info(f"Response Status Code: {response.status_code}")

    if response.status_code == 200:
        try:
            files = response.json()  # Parse the JSON response
        except ValueError as e:
            logging.error(f"JSON decode error: {e}")
            return
        for file in files:
            file_path = os.path.join(local_directory, file['name'])
            if file['type'] == 'file':  # Check if the item is a file
                if not os.path.exists(file_path):
                    download_file(file['download_url'], local_directory, file['name'])  # Download the file
            elif file['type'] == 'dir':  # Check if the item is a directory
                if not os.path.exists(file_path):
                    os.makedirs(file_path, exist_ok=True)  # Create the directory if it doesn't exist
                download_files(file['url'], file_path)  # Recursively download files in the directory
    else:
        logging.error(f"Failed to retrieve repository contents: {response.status_code}")


# Function to download an individual file
def download_file(url, local_directory, filename):
    headers = {}
    if GITHUB_TOKEN:
        headers['Authorization'] = f'token {GITHUB_TOKEN}'

    response = requests.get(url, headers=headers)  # Make a GET request to download the file
    if response.status_code == 200:
        file_path = os.path.join(local_directory, filename)
        with open(file_path, 'wb') as file:
            file.write(response.content)  # Write the file content to local storage
        logging.info(f"Downloaded file: {filename}")
    else:
        logging.error(f"Failed to download file: {response.status_code}")


# Function to run Bandit security check on a specified directory
def run_bandit(directory):
    output_file = 'data/compliance_report.csv'
    if not os.path.exists('data'):
        os.makedirs('data')  # Create the data directory if it doesn't exist

    command = ['bandit', '-r', directory, '-f', 'csv', '-o', output_file]
    result = subprocess.run(command, capture_output=True, text=True)  # Run Bandit as a subprocess

    if result.returncode in (0, 1):
        # Bandit completed successfully, even if issues were found (exit code 1).
        logging.info("Bandit analysis completed with issues found.")
    else:
        # Handle other exit codes that indicate errors.
        logging.error(f"Bandit analysis failed with return code {result.returncode}.")
        logging.error(f"Error output:\n{result.stderr}")

    logging.info(f"Bandit output:\n{result.stdout}")

    if os.path.exists(output_file):
        logging.info(f"CSV output written to file: {output_file}")
    else:
        logging.error(f"CSV output file {output_file} was not created.")


# Function to read and log the CSV compliance report
def read_csv_report(file_path):
    if not os.path.exists(file_path):
        logging.error(f"CSV report file not found: {file_path}")
        return

    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        logging.info("Reading CSV report from compliance_report.csv")
        headers = csv_reader.fieldnames
        if headers:
            logging.info(",".join(headers))  # Print header
        for row in csv_reader:
            if isinstance(row, dict):
                row_values = [str(value) for value in row.values()]  # Convert each value to a string
                logging.info(",".join(row_values))  # Print each row
            else:
                logging.error(f"Expected row to be dict, got {type(row)}: {row}")


if __name__ == "__main__":
    project_directory = 'repo_files'
    if not os.path.exists(project_directory):
        os.makedirs(project_directory, exist_ok=True)
        download_files(GITHUB_REPO_URL, project_directory)  # Download repository files if they don't exist locally
    else:
        logging.info("Repo files already exist, skipping download.")

    run_bandit(project_directory)  # Run Bandit analysis on the project directory
    read_csv_report('data/compliance_report.csv')  # Read and log the compliance report
