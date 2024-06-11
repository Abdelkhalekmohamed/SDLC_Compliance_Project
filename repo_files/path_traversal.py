import os

def read_file(filename):
    # High severity, medium confidence issue (path traversal vulnerability)
    with open(os.path.join('/etc/', filename), 'r') as file:
        data = file.read()
        print(f"File content: {data}")

if __name__ == "__main__":
    user_input = input("Enter the filename to read: ")  # User input that can lead to path traversal
    read_file(user_input)
