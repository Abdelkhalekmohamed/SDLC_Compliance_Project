import os  # Ensure the os module is imported


def connect_to_database():
    # High severity, high confidence issue
    password1 = "SuperSecretPassword123!"
    print(f"Connecting to database with password: {password1}")


def connect_to_ftp():
    # Medium severity, medium confidence issue
    password2 = "AnotherSecret"
    print(f"Connecting to FTP with password: {password2}")


def connect_to_api():
    # Low severity, low confidence issue
    password3 = "password"
    print(f"Connecting to API with password: {password3}")


def get_database_connection():
    # Secure password retrieval using environment variable
    user = "admin"
    password = os.getenv("DB_PASSWORD")  # Secure password retrieval
    connection_string = f"postgresql://{user}:{password}@localhost/database"
    return connection_string


if __name__ == "__main__":
    connect_to_database()
    connect_to_ftp()
    connect_to_api()
    print(get_database_connection())
