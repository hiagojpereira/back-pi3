  
from flask import Blueprint, request, jsonify
from app.services.firestore_service import add_user_data_fs, get_all_user_data_fs

# Criando o blueprint para as rotas de usuários
bp = Blueprint('user', __name__, url_prefix='/user')

# Rota para adicionar um usuário
@bp.route('/add', methods=['POST'])
def add_user_route():
    data = request.json  # Obtém os dados JSON enviados pelo cliente
    try:
        id = add_user_data_fs(data)  # Chama o serviço que adiciona o usuário no Firestore
        return jsonify({"message": "Usuário adicionado com sucesso!"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 400

# Rota para listar todos os usuários
@bp.route('/list', methods=['GET'])
def list_users():
    try:
        user_data = get_all_user_data_fs()  # Chama o serviço que busca os usuários no Firestore
        return jsonify({"data": user_data }), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 400
