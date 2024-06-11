import hashlib

def store_password(password):
    # High severity, medium confidence issue (insecure cryptographic storage)
    hashed_password = hashlib.md5(password.encode()).hexdigest()  # Using MD5 for hashing, which is insecure
    print(f"Storing password: {hashed_password}")

if __name__ == "__main__":
    store_password("SuperSecretPassword123!")
import subprocess
subprocess.Popen(['ls', '-l'])
