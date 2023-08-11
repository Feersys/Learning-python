from flask import Flask, request, jsonify
from flask_api import status
from pydantic import BaseModel

app = Flask(__name__)
h = "Hello"
error = "Sorry, not found"
users = [{"id": 0, "name": "Abraham", "sname": "Lincoln"},
         {"id": 1, "name": "Donald", "sname": "Trump"},
         {"id": 2, "name": "Donald", "sname": "Mc.Duck"}]


class Model1:
    first_num: float
    operation: str
    second_num: float


class Calculator:
    def __init__(self, first_num, operation, second_num):
        self.first_num = first_num
        self.operation = operation
        self.second_num = second_num

    def calc(self):
        print("calc:")
        if self.operation == "+":
            return self.first_num + self.second_num
        elif self.operation == "-":
            return self.first_num - self.second_num
        elif self.operation == "*":
            return self.first_num * self.second_num
        elif self.operation == "/":
            return self.first_num / self.second_num

        return None


instance = Calculator(float(input("Input first number: ")), input("Input operation: "),
                      float(input("Input second number: ")))
print(instance.calc())


@app.route("/utils/calculator/eval", methods=['POST'])
def calc():
    first_num = float(request.data.decode("utf-8"))
    operation = request.data.decode("utf-8")
    second_num = float(request.data.decode("utf-8"))
    Calculator(first_num, operation, second_num)


@app.route("/")
def main():
    return h


@app.route("/answer", methods=['POST'])
def post():
    content = request.data.decode("utf-8")
    print(content)
    return str(content) + "!!!"


@app.route("/users", methods=['GET'])
def users_list_query():
    user_id = request.args.get('id')
    user_id = int(user_id)
    if user_id > len(users) - 1:
        return error, 404
    user = users[user_id]
    return jsonify(user)


@app.route("/users/<user_id>", methods=['GET'])
def users_list_route(user_id):
    user_id = int(user_id)
    if user_id > len(users) - 1:
        return error, 404
    return jsonify(users[user_id])


@app.route('/endpoint', methods=['DELETE'])
def delete_endpoint():
    return jsonify({'error': 'I\'m a teapot'}), status.HTTP_418_IM_A_TEAPOT


@app.route('/change', methods=['PUT'])
def change():
    content = {}
    text = str(request.data.decode("utf-8"))
    content["input text"] = text
    print(content)
    return jsonify(content)


if __name__ == "__main__":
    app.run()
