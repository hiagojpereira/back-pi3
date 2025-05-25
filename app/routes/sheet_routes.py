from flask import Blueprint, request, jsonify
from app.services.firestore_service import add_sheet_fs, get_all_sheets_fs, delete_sheet_fs, get_sheet_fs

bp = Blueprint('sheet', __name__, url_prefix='/sheet')

# Rota para listar todos os usuários
@bp.route('/get_all', methods=['GET'])
def get_all_sheets():
    try:
        sheets = get_all_sheets_fs()
        for sheet in sheets:
            sheet['dados'] = []
        return jsonify({"success": sheets, 'error': False}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400
    
@bp.route('/get/<string:sheet_id>', methods=['GET'])
def get_sheet(sheet_id):
    try:
        sheet = get_sheet_fs(sheet_id)
        return jsonify({"success": sheet, 'error': False}), 201
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

@bp.route('/add', methods=['POST'])
def add_sheet():
    data = request.json 
    try:
        id = add_sheet_fs(data)
        return jsonify({"success": id, 'error': False}), 201
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400
    
@bp.route('/delete/<string:sheet_id>', methods=['DELETE'])
def delete_sheet(sheet_id):
    try:
        id = delete_sheet_fs(sheet_id)
        return jsonify({"success": id, 'error': False}), 201
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400