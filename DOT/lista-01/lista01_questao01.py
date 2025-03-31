'''Faça uma função que recebe um número inteiro por parâmetro e retorna verdadeiro se ele for par e falso se for ímpar.
Obs.: Sempre tratar a entrada de dados para evitar que o programa aborte.
'''

def par_impar(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
while True:
    try:
        numero = int(input("\nDigite um número: "))
        if par_impar(numero) == True:
            print(f"\nO número {numero} é par.")
        else:
            print("\nO número {numero} é ímpar.")
        break
    except:
        print("\nNúmero inválido. Digite novamente!")