#gera a conexão com banco de dados

import mysql.connector
from mysql.connector import Error
from config import Config

class Database: 
    _instance = None 
    
    def __new__(cls): #
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = None
        return cls._instance
    
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=Config.DB_HOST,
                port=Config.DB_PORT,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD,
                database=Config.DB_NAME
            )
            return self.connection
        except Error as e:
            print(f"Erro ao conectar: {e}")
            return None
    
    def get_connection(self):
        if self.connection is None or not self.connection.is_connected():
            return self.connect()
        return self.connection
    
    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            self.connection = None

def get_db():
    db = Database()
    return db.get_connection()