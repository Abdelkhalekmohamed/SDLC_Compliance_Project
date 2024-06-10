import os


def get_database_connection():
    user = "admin"
    password = os.getenv("DB_PASSWORD")  # Secure password retrieval
    connection_string = f"postgresql://{user}:{password}@localhost/mydatabase"
    return connection_string