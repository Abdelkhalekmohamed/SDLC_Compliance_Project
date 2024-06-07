def get_database_connection():
    user = "admin"
    password = "password123"  # Hardcoded password (vulnerability)
    connection_string = f"postgresql://{user}:{password}@localhost/mydatabase"
    return connection_string
