def generate_html(user_input):
    return f"<html><body>{user_input}</body></html>"


print(generate_html('<script>alert("XSS")</script>'))
