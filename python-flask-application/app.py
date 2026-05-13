# Import Flask framework and render_template function
from flask import Flask, render_template

# Create Flask application instance
app = Flask(__name__)


# This route loads the index.html page
@app.route('/')
def home():
    return render_template('index.html')


# Used to verify if the application is running properly.
@app.route('/health')
def health():

    # Return application status in JSON format.
    return {
        "status": "running",
        "application": "Simple Flask App"
    }


# Main entry point of the application

if __name__ == '__main__':

    # host='0.0.0.0'
    # Makes the application accessible from outside the container/system

    app.run(host='0.0.0.0', port=5000, debug=True)