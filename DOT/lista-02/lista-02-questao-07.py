'''

'''

quantidades = []
precos = []
faturamentos = []

print("Digite os dados de 20 produtos:")

for i in range(20):
    qtd = int(input(f"Quantidade do produto {i + 1}: "))
    preco = float(input(f"Preço do produto {i + 1}: "))
    
    quantidades.append(qtd)
    precos.append(preco)

    faturamento = qtd * preco
    faturamentos.append(faturamento)

print("\nFaturamento por produto:")
for i in range(20):
    print(f"Produto {i + 1}: {quantidades[i]} x {precos[i]:.2f} = {faturamentos[i]:.2f}")

faturamento_total = sum(faturamentos)
media_faturamento = faturamento_total / len(faturamentos)

abaixo_da_media = 0
for f in faturamentos:
    if f < media_faturamento:
        abaixo_da_media += 1

print(f"\nFaturamento total: R$ {faturamento_total:.2f}")
print(f"Média dos faturamentos: R$ {media_faturamento:.2f}")
print(f"Quantidade de faturamentos abaixo da média: {abaixo_da_media}")