  
from flask import Blueprint, request, jsonify
from app.services.firestore_service import add_user_data_fs, get_all_user_data_fs

bp = Blueprint('user', __name__, url_prefix='/user')

# Rota para adicionar um usuário
@bp.route('/add', methods=['POST'])
def add_user_route():
    data = request.json 
    try:
        id = add_user_data_fs(data) 
        return jsonify({"message": "Usuário adicionado com sucesso!"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 400

# Rota para listar todos os usuários
@bp.route('/list', methods=['GET'])
def list_users():
    try:
        user_data = get_all_user_data_fs()
        return jsonify({"data": user_data }), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 400
