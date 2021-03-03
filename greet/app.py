"""Greeting app"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def default():
    """Homepage"""

    return """<html> 
    <body>
    <h1>Home Page</h1>
    </body>
    </html>"""

@app.route('/welcome')
def welcome():
    """Welcome user to page"""

    return """<html> 
    <body>
    <h1>welcome</h1>
    </body>
    </html>"""

@app.route('/welcome/home')
def home():
    """Welcome user to page"""

    return """<html> 
    <body>
    <h1>welcome home</h1>
    </body>
    </html>"""

@app.route('/welcome/back')
def back():
    """Welcome user to page"""

    return """<html> 
    <body>
    <h1>welcome back</h1>
    </body>
    </html>"""