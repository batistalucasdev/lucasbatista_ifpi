'''
8. Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere somente se ele for igual a 'S' ou 'N'. Se o caractere não for nem 'S' nem 'N', a função imprime a mensagem 'Caractere inválido. Digite novamente'. Use esta função em um programa que fica lendo do usuário um número qualquer e imprime este número ao cubo na tela. O programa deve ficar lendo os números até o usuário responder 'N' à pergunta se ele deseja continuar ou não.
Obs.: Sempre tratar a entrada de dados para evitar que o programa aborte.
'''

def calcular_cubo(numero):
    cubo = numero ** 3
    return print(f"\n{numero} elevado ao cubo = {cubo}.")

def continuar(resposta):
    if resposta == 'S':
        return resposta
    elif resposta == 'N':
        return resposta
    else:
        return print (f"Caractere inválido. Digite novamente")
    
while True:
    try:
        numero = int(input("\nDigite um número qualquer: "))
        cubo = calcular_cubo(numero)
        pergunta = input("\nDeseja continuar ou não?")
        #pergunta = continuar(resposta)
        break
    except:
        print("\nValor inválido. Digite novamente!")
