from modelos import Brinde

def exibir_menu():
    print("\n" + "="*40)
    print("  SISTEMA DE GERENCIAMENTO DE BRINDES  ")
    print("="*40)
    print("1. Cadastrar novo brinde")
    print("2. Listar catálogo completo")
    print("3. Buscar brinde específico")
    print("4. Sair do sistema")
    print("="*40)

def cadastrar_item(catalogo):    
    print("\n--- Cadastro de Item ---")
    nome_input = input("Digite o nome do brinde (ex: Caneca Térmica): ")
    categoria_input = input("Digite a categoria (ex: Metal, Plástico, Ecológico): ")
    
    try:
        preco_input = float(input("Digite o preço de custo (ex: 25.50): "))
        novo_item = Brinde(nome_input, categoria_input, preco_input)
        catalogo.append(novo_item)
        print("\n Item cadastrado com sucesso!")
    except ValueError:
        print("\n Erro de validação: O preço deve ser numérico.")

def listar_itens(catalogo):    
    print("\n--- Catálogo de Itens ---")
    if not catalogo:
        print("Nenhum item cadastrado no sistema ainda.")
    else:
        for item in catalogo:
            item.exibir_detalhes()

def buscar_item(catalogo):
    
    print("\n--- Busca de Item ---")
    termo_busca = input("Digite o nome do brinde que deseja buscar: ").lower()
    encontrado = False

    for item in catalogo:
        if termo_busca in item.nome.lower():
            print("\n🔍 Resultado encontrado:")
            item.exibir_detalhes()
            encontrado = True

    if not encontrado:
        print(f"\n Nenhum registro encontrado para '{termo_busca}'.")