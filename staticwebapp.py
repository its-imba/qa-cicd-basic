'''Basic static web app'''

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Static web app with Flask'

app.run(host='20.68.23.128', port=9000, debug=True)