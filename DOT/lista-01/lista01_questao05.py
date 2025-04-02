'''
5. Faça um programa que leia a altura e o sexo (codificado da seguinte forma:
1:feminino 2:masculino) de uma pessoa. Depois faça uma função chamada peso ideal que receba a altura e o sexo via parâmetro e que calcule e retorne seu peso ideal, utilizando as seguintes fórmulas:
- para homens : (72.7 * h) - 58
- para mulheres : (62.1 * h) - 44.7
Observação: Altura = h (na fórmula acima).
'''

def peso_ideal(h,sexo):
    if sexo == 1:
        peso_ideal = (62.1 * h) - 44.7
    elif sexo == 2:
        peso_ideal = (72.7 * h) - 58
    return peso_ideal
    
while True:
    try:
        altura = float(input("\nDigite a sua altura: "))
        sexo = int(input("\nInforme seu sexo: 1:feminino 2:masculino."))
        peso_ideal = peso_ideal(altura,sexo)
        print(f'\nSeu peso ideal é {peso_ideal:.2f}.')
        break
    except:
        print("\nValor inválido. Digite novamente!")
