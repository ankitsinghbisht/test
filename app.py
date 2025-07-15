from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get('/ping')
def ping():
    return jsonify({'message': 'pong'})

@app.post('/login')
def login():
    data = request.get_json(force=True, silent=True) or {}
    username = data.get('username')
    password = data.get('password')
    if username == 'user' and password == 'pass':
        return jsonify({'status': 'success'})
    return jsonify({'status': 'failure'}), 401

if __name__ == '__main__':
    app.run()
