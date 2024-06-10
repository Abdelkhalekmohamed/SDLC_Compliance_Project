def connect_to_service():
    # High severity, low confidence issue (hardcoded password in a less typical usage)
    password = "SuperSecretPassword123!"  # Hardcoded password
    print(f"Connecting to service with password: {password}")

if __name__ == "__main__":
    connect_to_service()

