import os

# Definindo variáveis de configuração
# Exemplo de configuração do Firebase
FIREBASE_CREDENTIALS = os.getenv('FIREBASE_CREDENTIALS', 'serviceAccountKey.json')

# Outras configurações podem ser adicionadas aqui, como chave secreta, DB, etc.
SECRET_KEY = os.getenv('SECRET_KEY', 'mysecretkey')
