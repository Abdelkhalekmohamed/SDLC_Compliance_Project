import hashlib


def insecure_hash(input_data):  # Renamed 'data' to 'input_data'
    return hashlib.md5(input_data.encode()).hexdigest()


data = "example_data"
print(insecure_hash(data))
import subprocess
subprocess.Popen(['ls', '-l'])
