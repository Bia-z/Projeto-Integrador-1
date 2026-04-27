#interface do terminal para o operador

class OperadorCLI: #cria classe OperadorCLI
    
    def menu_operador(self, operador): #define uma função chamada menu_operador, recebe ela mesma e operador (dados do login)
        while True:
            print("\n" + "-"*40)
            print(f"Bem-vindo, {operador.nome}!")
            print("-"*40)
            print("1. Ver todas solicitações")
            print("2. Filtrar solicitações")
            print("3. Atualizar status")
            print("4. Ver estatísticas")
            print("5. Sair")
            
            opcao = input("\nDigite sua opção: ")
            
            if opcao == "1":
                print("\n--- TODAS SOLICITAÇÕES ---")
                #print("vou fazer, preciso do banco")
                
            elif opcao == "2":
                print("\n--- FILTRAR SOLICITAÇÕES ---")
                #print("")
                
            elif opcao == "3":
                print("\n--- ATUALIZAR STATUS ---")
                #print("")
                
            elif opcao == "4":
                print("\n--- ESTATÍSTICAS ---")
                #print("")
                
            elif opcao == "5":
                print("\nSaindo do menu...")
                break
                
            else:
                print("\nOpção inválida!")