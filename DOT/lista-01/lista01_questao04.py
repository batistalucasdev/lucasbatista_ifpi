'''
4. Escreva um programa para ler as notas das duas avaliações de um aluno no semestre. Faça um procedimento que receba as duas notas por parâmetro e calcule e escreva a média semestral e a mensagem “PARABÉNS! Você foi aprovado!” somente se o aluno foi aprovado (considere 6.0 a média mínima para aprovação).
Obs.: Sempre tratar a entrada de dados para evitar que o programa aborte.
'''

def calcular_media(n1,n2):
    media = (n1 + n2)/2
    return media
    
while True:
    try:
        nota01 = float(input("\nDigite a primeira nota do aluno: "))
        nota02 = float(input("\nDigite a segunda nota do aluno: "))

        media = calcular_media(nota01,nota02)
        if media >= 6:
            print(f'\nA média semestral do aluno é {media:.2f}.')
            print(f'\nPARABÉNS! Você foi aprovado!')
        else:
            print(f'\nA média semestral do aluno é {media:.2f}.')
            print(f'\nVocê não foi aprovado...')
        break
    except:
        print("\nNúmero inválido. Digite novamente!")
