from flask import Flask,request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    result = num1+num2
    return f'The sum of {num1} and {num2} is {result}'

@app.route('/multiply', methods=['GET'])
def multiply():
    # Get query parameters
    num1 = request.args.get('num1', type=int)
    num2 = request.args.get('num2', type=int)
    
    if num1 is None or num2 is None:
        return "Please provide both 'num1' and 'num2' as query parameters.", 400
    
    result = num1 * num2
    return f'The product of {num1} and {num2} is {result}.'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)