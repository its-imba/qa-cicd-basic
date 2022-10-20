'''Basic static web app'''

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Static web app with Flask'

app.run(host='0.0.0.0', port=80, debug=True)