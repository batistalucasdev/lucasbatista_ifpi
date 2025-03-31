'''
10. Escreva um programa composto de uma função Max e o programa principal como segue:
a) A função Max recebe como parâmetros de entrada dois números inteiros e retorna o maior. Se forem iguais retorna qualquer um deles;
b) O programa principal lê 4 séries de 4 números a, b. Para cada série lida imprime o maior dos quatro números usando a função Max.
'''

def Max(a, b):
    return a if a >= b else b

for i in range(4):
    print(f"\nSérie {i + 1}:")
    try:
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        c = int(input("Digite o terceiro número: "))
        d = int(input("Digite o quarto número: "))

        maior = Max(Max(a, b), Max(c, d))  # Encontra o maior entre os quatro números
        print(f"O maior número da série {i + 1} é: {maior}")
    
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar apenas números inteiros.")
