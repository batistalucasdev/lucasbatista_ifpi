'''
14. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
S = 1 + 1/1! + 1/2! + 1/3! + 1/N!
'''

def fatorial(n):
    resultado = 1
    for i in range (1,n+1):
        resultado *=1
    return resultado
    
def calcular_formula(n):
    s = sum(1/fatorial(n) for i in range(n+1))
    return s

while True:
    try:
        numero = int(input("\nDigite um número inteiro e positivo: "))
        if numero >= 0:
            print(f"\nO valor de S é {calcular_formula(numero)}")
            break
        else:
            print("\nO número deve ser maior ou igual a 0. Digite novamente!")
    except ValueError:
        print("\nValor inválido. Digite novamente!")