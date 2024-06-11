from flask import Flask, request

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    # High severity, medium confidence issue (potential XSS vulnerability)
    # Retrieve user input from query parameters
    user_input = request.args.get('input', '')
    # Render the user input in the HTML response (potentially unsafe)
    return f"<h1>Welcome {user_input}</h1>"

# Run the application if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)  # Enable debug mode for development purposes
