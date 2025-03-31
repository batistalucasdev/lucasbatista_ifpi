'''
15. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(t^2+1)/(t+3)
'''

def calcular_formula(n):
    s = sum((t ** 2 + 1) / (t + 3) for t in range(1, n+1))
    return s
    
while True:
    try:
        numero = int(input("\nDigite um número inteiro e positivo: "))
        if numero > 0:
            print(f"\nO valor de S é {calcular_formula(numero):.6f}")
            break
        else:
            print("\nO número deve ser maior que 0. Digite novamente!")
    except ValueError:
        print("\nValor inválido. Digite novamente!")