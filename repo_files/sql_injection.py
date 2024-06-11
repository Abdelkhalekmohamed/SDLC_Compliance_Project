import sqlite3

def get_user_data(username):
    # High severity, low confidence issue (potential SQL injection)
    query = f"SELECT * FROM users WHERE username = '{username}'"  # Potentially vulnerable to SQL injection
    print(f"Executing query: {query}")

if __name__ == "__main__":
    user_input = "admin' OR '1'='1"
    get_user_data(user_input)
import subprocess
subprocess.Popen(['ls', '-l'])
import subprocess
subprocess.Popen(['ls', '-l'])
import subprocess
subprocess.Popen(['ls', '-l'])
import pickle
pickle.loads(b'')
import pickle
pickle.loads(b'')
