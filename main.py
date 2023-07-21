from flask import Flask, request, jsonify
from flask_api import status

app = Flask(__name__)
h = "Hello"
error = "Sorry, not found"
users = [{"id": 0, "name": "Abraham", "sname": "Lincoln"},
         {"id": 1, "name": "Donald", "sname": "Trump"},
         {"id": 2, "name": "Donald", "sname": "Mc.Duck"}]
query_params = {"id": 1}


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
    if user_id > len(users)-1:
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
