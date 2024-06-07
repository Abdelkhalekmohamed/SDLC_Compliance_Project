import os
import requests
import logging
import subprocess
import csv

# Configure logging
logging.basicConfig(level=logging.INFO)

# GitHub repository URL
GITHUB_REPO_URL = 'https://api.github.com/repos/Abdelkhalekmohamed/SDLC_Compliance_Project/contents/'

# Optional: Use your GitHub token for authentication if the repo is private
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')  # Store your token in an environment variable for security


def download_files(repo_url, local_dir):
    headers = {}
    if GITHUB_TOKEN:
        headers['Authorization'] = f'token {GITHUB_TOKEN}'

    response = requests.get(repo_url, headers=headers)
    logging.info(f"Fetching URL: {repo_url}")
    logging.info(f"Response Status Code: {response.status_code}")
    logging.info(f"Response Content: {response.text}")

    if response.status_code == 200:
        try:
            files = response.json()
        except requests.exceptions.JSONDecodeError as e:
            logging.error(f"JSON decode error: {e}")
            return
        for file in files:
            if file['type'] == 'file':
                download_file(file['download_url'], local_dir, file['name'])
            elif file['type'] == 'dir':
                new_local_dir = os.path.join(local_dir, file['name'])
                os.makedirs(new_local_dir, exist_ok=True)
                download_files(file['url'], new_local_dir)
    else:
        logging.error(f"Failed to retrieve repository contents: {response.status_code}")


def download_file(url, local_dir, filename):
    headers = {}
    if GITHUB_TOKEN:
        headers['Authorization'] = f'token {GITHUB_TOKEN}'

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(os.path.join(local_dir, filename), 'wb') as file:
            file.write(response.content)
    else:
        logging.error(f"Failed to download file: {response.status_code}")


def run_bandit(directory):
    command = ['bandit', '-r', directory, '-f', 'csv', '-o', 'compliance_report.csv']
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        logging.info("Bandit analysis completed successfully.")
        logging.info(f"Bandit output:\n{result.stdout}")
    else:
        logging.error(f"Bandit analysis failed: {result.stderr}")


def read_csv_report(file_path):
    if not os.path.exists(file_path):
        logging.error(f"CSV report file not found: {file_path}")
        return

    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        logging.info("Reading CSV report from compliance_report.csv")
        headers = csv_reader.fieldnames
        logging.info(",".join(headers))  # Print header
        for row in csv_reader:
            logging.info(",".join(row.values()))  # Print each row


if __name__ == "__main__":
    local_dir = 'repo_files'
    os.makedirs(local_dir, exist_ok=True)
    download_files(GITHUB_REPO_URL, local_dir)
    run_bandit(local_dir)
    read_csv_report('compliance_report.csv')


