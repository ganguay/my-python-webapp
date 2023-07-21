import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    app_color = os.environ.get('APP_COLOR', 'blue')
    return f'<h1 style="color: {app_color};">Hello, this is the {app_color} version of the web app!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

