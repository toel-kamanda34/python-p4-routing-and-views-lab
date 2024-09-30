#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:username>')
def print_string(username):
    print(username)
    return username


@app.route('/count/<int:param>')
def count(param):
    return "\n".join(str(i) for i in range(param)) + "\n"

@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        result = num1/num2
    elif operation == "%":
        result = num1 % num2
    else:
        return "Invalid     Oprion"
    return str(result) 

