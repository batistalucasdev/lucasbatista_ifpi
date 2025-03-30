'''
10. Escreva um programa composto de uma função Max e o programa principal como segue:
a) A função Max recebe como parâmetros de entrada dois números inteiros e retorna o maior. Se forem iguais retorna qualquer um deles;
b) O programa principal lê 4 séries de 4 números a, b. Para cada série lida imprime o maior dos quatro números usando a função Max.
'''

def soma_intervalo(a,b):
    soma = 0
    for i in range (a,b+1):
        soma+=i
    return soma
    
while True:
    try:
        n1 = int(input("\nDigite o primeiro número inteiro: "))
        n2 = int(input("\nDigite o segundo número inteiro: "))
        if n1 <= n2:
            print("\nA soma do intervalo informado é ", soma_intervalo(n1,n2))
            break
        else:
            print("\nn2 deve ser maior que n1. Digite novamente!")
    except:
        print("\nValor inválido. Digite novamente!")