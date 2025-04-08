import firebase_admin
from firebase_admin import credentials, firestore
from .geocoding_service import geocode

# Inicializando o Firebase com a chave de credenciais
cred = credentials.Certificate(r'C:\repos\pi3\back-pi3\projeto-integrador-3-da126-firebase-adminsdk-fbsvc-4bf42901b0.json')
firebase_admin.initialize_app(cred)

# Obtendo uma instância do Firestore
db = firestore.client()

def add_user_data_fs(data):
    user_data_ref = db.collection("users_data").document()  # Usando o ID do usuário como chave
    user_data_ref.set(data)  # Adiciona os dados no Firestore
    return user_data_ref.id

def get_all_user_data_fs():
    users_data_ref = db.collection("users_data").stream()  # Obtém todos os documentos da coleção 'users'
    users_data = [{**doc.to_dict(), "id": doc.id} for doc in users_data_ref]  # Converte os dados em lista de dicionários
    return users_data


#################### SHEETS ####################

def get_all_sheets_fs():
    sheets_ref = db.collection("sheet_data").order_by("data", direction="DESCENDING").stream()  # Obtém todos os documentos da coleção 'users'
    sheets = [{**doc.to_dict(), "id": doc.id} for doc in sheets_ref]  # Converte os dados em lista de dicionários
    return sheets

def get_sheet_fs(sheet_id):
    doc = db.collection("sheet_data").document(sheet_id).get()
    if doc.exists:
        return doc.to_dict()
    else:
        return False

def add_sheet_fs(data):
    for dado in data['dados']:
        location = None
        try:
            location = geocode(dado['endereco'].replace('\u200b', ''))  
            dado['lat'] = location['lat'] if location else "not found"
            dado['lng'] = location['lng'] if location else "not found"                
        except:  
            dado['lat'] = location['lat'] if location else "not found"
            dado['lng'] = location['lng'] if location else "not found"  

    sheet_ref = db.collection("sheet_data").document()
    sheet_ref.set(data)
    return sheet_ref.id

def delete_sheet_fs(sheet_id):
    sheet_ref = db.collection("sheet_data").document(sheet_id)
    sheet_ref.delete()
    return sheet_ref.id
