from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Home Page</h1>
    <hr>
    <p>Welcome to our Flask Web Application!</p>
    """

@app.route('/about')
def about():
    return """
    <h1>About Us</h1>
    <hr>
    <p>This is a Flask project demonstrating static routing.</p>
    """

@app.route('/contact')
def contact():
    return """
    <h1>Contact Us</h1>
    <hr>
    <p>Email: info@example.com</p>
    <p>Phone: +91 9876543210</p>
    """

if __name__ == "__main__":
    app.run(debug=True)