from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>hello123</h1>"


@app.route('/test')
def test_page():
    return "<h5>test page</h5>"


@app.route('/greet/<name>')
def name(name):
    return f"<h3>hello {name}</h3>"


@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    # number1 = int(number1)
    # number2 = int(number2)
    return f"{number1} + {number2} = {number1 + number2}"





if __name__ == "__main__":
    app.run(debug=True, port=5555, host="0.0.0.0")
