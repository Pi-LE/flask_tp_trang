from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Ceci est un TP DevOps avec Flask, Git et Jenkins."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
