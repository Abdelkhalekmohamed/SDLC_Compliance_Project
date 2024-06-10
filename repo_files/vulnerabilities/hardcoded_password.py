def connect_to_database():
    # High severity, high confidence
    password1 = "SuperSecretPassword123!"  # Hardcoded password
    print(f"Connecting to database with password: {password1}")

def connect_to_ftp():
    # Medium severity, medium confidence
    password2 = "AnotherSecret"  # Another hardcoded password
    print(f"Connecting to FTP with password: {password2}")

def connect_to_api():
    # Low severity, low confidence
    password3 = "password"  # Simple hardcoded password
    print(f"Connecting to API with password: {password3}")

if __name__ == "__main__":
    connect_to_database()
    connect_to_ftp()
    connect_to_api()
