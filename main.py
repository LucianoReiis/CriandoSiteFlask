from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Hello, World!</p>"

@app.route("/contato")
def contato():
    return 'Entre em contato pelo e-mail: xyz@xyz.com'


if __name__ == '__main__':
    app.run(debug=True)