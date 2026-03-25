#lê as variáveis da .env

import os 
from dotenv import load_dotenv #função que le arquivos da .env

load_dotenv() #carrega os arquivos da env

class Config: #cria classe que agrupa as configurações
    DB_HOST = os.getenv('DB_HOST', 'localhost') #os.getenv pega o valor da variável
    DB_PORT = int(os.getenv('DB_PORT', 3306))
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '')
    DB_NAME = os.getenv('DB_NAME', 'BD24022613')
    
    #tirar comentário quando a bibliteca for adicionada
    #DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}" #URL de conexão com o banco de dados que a biblioteca SQLAlchemy lê