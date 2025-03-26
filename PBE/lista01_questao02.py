'''
2. Escreva um programa que leia o raio de um círculo e faça duas funções: uma função chamada área que calcula e retorna a área do círculo e outra função chamada perímetro que calcula e retorna o perímetro do círculo.
Área = PI * r2; Perímetro = PI * 2 * r;
Obs.: Sempre tratar a entrada de dados para evitar que o programa aborte.
'''

def calcular_perimetro(raio):
    perimetro = 3.1415 * 2 * raio
    return perimetro

def calcular_area(raio):
    area = 3.1415 * raio**2
    return area
    
while True:
    try:
        num = float(input("\nDigite o raio de um círculo: "))
        print(f'\nO perímetro do círculo é {calcular_perimetro(num)}.')
        print(f'\nA área do círculo é {calcular_area(num)}.')
        break
    except:
        print("\nNúmero inválido. Digite novamente!")
