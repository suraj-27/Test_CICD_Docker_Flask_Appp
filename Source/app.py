from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome To Home Page!'

@app.route('/about')
def about():
    return 'About Page'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)