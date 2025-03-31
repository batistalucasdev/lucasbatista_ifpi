'''
8. Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere somente se ele for igual a 'S' ou 'N'. Se o caractere não for nem 'S' nem 'N', a função imprime a mensagem 'Caractere inválido. Digite novamente'. Use esta função em um programa que fica lendo do usuário um número qualquer e imprime este número ao cubo na tela. O programa deve ficar lendo os números até o usuário responder 'N' à pergunta se ele deseja continuar ou não.
'''

def calcular_cubo(numero):
    return numero ** 3

def obter_resposta():
    while True:
        resposta = input("\nDeseja continuar? (S/N): ").strip().upper()
        if resposta in ('S', 'N'):
            return resposta
        print("Caractere inválido. Digite novamente.")

while True:
    try:
        numero = int(input("\nDigite um número qualquer: "))
        print(f"{numero} elevado ao cubo = {calcular_cubo(numero)}.")
        
        if obter_resposta() == 'N':
            break
    except ValueError:
        print("Valor inválido. Digite novamente!")
