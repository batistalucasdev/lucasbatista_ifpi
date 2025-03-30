'''
13. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
S = 1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/N.
'''

def calcular_formula(n):
    s = 1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/n
    return s
    
while True:
    try:
        numero = int(input("\nDigite um número inteiro e positivo: "))
        if numero > 0:
            print(f"\nO valor de S é {calcular_formula(numero)}")
            break
        else:
            print("\nO número deve ser maior que 0. Digite novamente!")
    except:
        print("\nValor inválido. Digite novamente!")