class Produto:
    def __init__(self, codigo, nome, categoria, preco, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.quantidade = quantidade

    def valor_total(self):
        return self.preco * self.quantidade

    def exibir_info(self):
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.nome}")
        print(f"Categoria: {self.categoria}")
        print(f"Preço: R${self.preco:.2f}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Valor total: R${self.valor_total():.2f}")
        print("-" * 30)

estoque = {
    "101": Produto(101, "Notebook", "Eletrônicos", 3500.00, 5),
    "102": Produto(102, "Camiseta", "Vestuário", 40.00, 20),
    "103": Produto(103, "Cafeteira", "Eletrodomésticos", 250.00, 10),
    "104": Produto(104, "Tênis", "Vestuário", 200.00, 15),
}

#a) Exibir todos os produtos no estoque com suas informações formatadas.
print("=== Produtos no Estoque ===")
for produto in estoque.values():
    produto.exibir_info()

#b) Calcular e exibir o valor total geral do estoque.
valor_total_geral = sum(produto.valor_total() for produto in estoque.values())
print(f"Valor total geral do estoque: R${valor_total_geral:.2f}")

#c) Exibir o nome do produto com o maior valor total.
produto_maior_valor = max(estoque.values(), key=lambda p: p.valor_total())
print(f"Produto com maior valor total: {produto_maior_valor.nome} (R${produto_maior_valor.valor_total():.2f})")

#d) Permitir buscar produtos por categoria.
categoria_busca = input("Digite a categoria para busca: ").strip().capitalize()
print(f"\nProdutos da categoria '{categoria_busca}':")
encontrado = False
for produto in estoque.values():
    if produto.categoria.lower() == categoria_busca.lower():
        produto.exibir_info()
        encontrado = True
if not encontrado:
    print("Nenhum produto encontrado nessa categoria.")
