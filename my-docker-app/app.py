from flask import Flask
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

@app.route('/')
def hello():
    return "Hello, Docker Compose!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')

