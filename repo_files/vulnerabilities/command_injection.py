import subprocess

def run_command(user_input):
    # Medium severity, low confidence issue (potential command injection)
    command = f"echo {user_input}"
    subprocess.run(command, shell=True)  # Using shell=True can be risky

if __name__ == "__main__":
    user_input = "hello; rm -rf /"
    run_command(user_input)

