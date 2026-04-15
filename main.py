#arquivo principal, junta o CLI e inicia o programa

from services.auth_service import AuthService #importa a classe AuthServie dos services, que cuida do login do operador
from cli.operador_cli import OperadorCLI #importa OperadorCLI, que mostra o menu do operador

def main(): #função principal, será executado quando chamamarmos main
    auth_service = AuthService() #cria objeto, que tem acesso a todas as funções da classe AuthService, e cria auth_service que é usado para o login do operador
    operador_cli = OperadorCLI() #mesma coisa, mas para mostrar o menu do operador
    
    while True: #loop infinito, até o break, no caso mantém o programa rodando até o usuário escolher sair
        print("\n" + "-"*40) #linha de separação
        print("SISTEMA DE SOLICITAÇÕES")
        print("-"*40)
        print("1. Login Operador")
        print("2. Sair")
        
        opcao = input("\nDigite sua opção: ") 
        
        if opcao == "1":
            email = input("Digite seu email: ")
            operador = auth_service.login_operador(email) #chamando a função login_operador, dentro de auth_service, ao receber (email) como parâmetro ele vai no bd e retorna os dados SE encontrar, caso encontre,
                                                          #caso encontre, guarda na variável operador, se não, 'operador' fica NONE
            if operador: #se operdaor n for NONE
                operador_cli.menu_operador(operador) #chama a função menu operador, que está em operador_cli, recebendo os dados e mostrando o menu especifíco dos operadores
            else: #se não,
                print("\nEmail não encontrado!") #printa email não encontrado
                
        elif opcao == "2":
            print("\nSaindo...")
            break
        else:
            print("\nOpção inválida!")

if __name__ == "__main__": #garante que o código rode depois de dar python main.py
    main() #chama a função main, que acabou de ser definida