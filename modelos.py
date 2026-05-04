class Brinde:    
    
    def __init__(self, nome, categoria, preco_custo):
        self.nome = nome
        self.categoria = categoria
        self.preco_custo = float(preco_custo)

    def exibir_detalhes(self):        
        print(f"Nome: {self.nome} | Categoria: {self.categoria} | Custo: R$ {self.preco_custo:.2f}")