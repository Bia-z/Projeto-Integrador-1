#regras de autenticação do sistema, no caso, verifica se o email digitado existe na tabela de operadores

from repositories.operador_repository import OperadorRepository #impor da classe OperadorRepository da repositories
from models.operador import Operador #import da calsso operador, dentro da models
class AuthService: #cria uma classe chamada AuthService
    
    def __init__(self): #método que é executado automaticamente quando um objeto da classe é criado, inicializzando variáveis internas
        self.operador_repo = OperadorRepository() #cria um objeto da classe OperadorRepository, que vai ser usado para acessar o bd
    
    def login_operador(self, email: str): #define o método chamado login_operador, recebendo o próprio objeto, e o email que é uma string
        operador = self.operador_repo.buscar_por_email(email) #chama a função buscar_por_email que ta no repositório, ele vai no bd e busca na tabela de operadores um com o email
                                                              # fornecido, e guarda o resultado na varíavel operador
        if operador:#se achar
            return operador #retorna a variável
        else: #se não,
            return None #retorna none