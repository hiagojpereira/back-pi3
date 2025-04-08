from flask import Flask
from app.routes import user_data_routes, sheet_routes

from flask import Blueprint, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Configurações da aplicação
app.config.from_object('config')

# Registrando as rotas
# app.register_blueprint(user_data_routes.bp)
app.register_blueprint(sheet_routes.bp)

CORS(app, origins=["http://localhost:4200"])

if __name__ == "__main__":
    app.run(debug=True)