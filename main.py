import processamento

def principal():
    
    catalogo = []
    
    while True:
        processamento.exibir_menu()
        opcao = input("Escolha uma opção do menu: ")

        if opcao == '1':
            processamento.cadastrar_item(catalogo)
            
        elif opcao == '2':
            processamento.listar_itens(catalogo)
            
        elif opcao == '3':
            processamento.buscar_item(catalogo)
            
        elif opcao == '4':
            print("\nEncerrando o sistema. Até a próxima!")
            break
            
        else:
            print("\n Opção inválida. Por favor, escolha um número de 1 a 4.")

if __name__ == "__main__":
    principal()