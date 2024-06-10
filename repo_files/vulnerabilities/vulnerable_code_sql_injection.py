import sqlite3

def get_user_data_vulnerable(username):
    # High severity, high confidence issue (SQL injection vulnerability)
    query = f"SELECT * FROM users WHERE username = '{username}'"
    print(f"Executing vulnerable query: {query}")
    # Imagine this line executes the query
    # cursor.execute(query)

def get_user_data_safe(username):
    # Low severity, high confidence issue (safe query construction)
    query = "SELECT * FROM users WHERE username = ?"
    print(f"Executing safe query: {query}")
    # Imagine this line executes the query safely
    # cursor.execute(query, (username,))

def get_user_data_partially_safe(username):
    # Medium severity, medium confidence issue (partially safe but not recommended)
    query = "SELECT * FROM users WHERE username = '{}'".format(username)
    print(f"Executing partially safe query: {query}")
    # Imagine this line executes the query
    # cursor.execute(query)

username_input = "admin' OR '1'='1"
get_user_data_vulnerable(username_input)
get_user_data_safe(username_input)
get_user_data_partially_safe(username_input)
