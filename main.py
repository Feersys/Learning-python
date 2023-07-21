from flask import Flask, request, jsonify


app = Flask(__name__)
h = "Hello"
users = [{"id": 1, "name": "Abraham", "sname": "Lincoln"},
         {"id": 2, "name": "Donald", "sname": "Trump"},
         {"id": 3, "name": "Donald", "sname": "Mc.Duck"}]
query_params = {"id": 1}


@app.route("/")
def main():
    return h


@app.route("/answer", methods=['POST'])
def post():
    content = request.data.decode("utf-8")
    print(content)
    return str(content) + "!!!"


@app.route("/users", methods=['GET'], params=query_params)
def users_list():
    return jsonify(users)


@app.route('/endpoint', methods=['DELETE'])
def delete_endpoint():
    return jsonify({'error': 'I\'m a teapot'}), 418


@app.route('/change', methods=['PUT'])
def change():
    content = str(request.data.decode("utf-8"))+" input text"
    print(content)
    return jsonify(content)



if __name__ == "__main__":
    app.run(debug=True)
