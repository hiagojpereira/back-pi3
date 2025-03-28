from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def teste():
    return jsonify({"message": "api funcionando"})

if __name__ == '__main__':
    app.run(debug=True)