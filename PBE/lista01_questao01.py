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
        num = int(input("\nDigite um número: "))
        if par_impar(num) == True:
            print("\nO número %d é par."%num)
        else:
            print("\nO número %d é ímpar."%num)
        break
    except:
        print("\nNúmero inválido. Digite novamente!")