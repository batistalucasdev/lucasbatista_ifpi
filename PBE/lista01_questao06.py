'''
6. Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Faça um procedimento que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule e imprima o seguinte:
- Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
- Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
- Se o número de lados for igual a 5, escrever PENTÁGONO.
Obs.: Sempre tratar a entrada de dados para evitar que o programa aborte.
'''

def verifica_lados(numero_lados, medida_lado):
    perimetro = numero_lados * medida_lado
    if numero_lados == 3:
        print(f'TRIÂNGULO; Valor do perímetro = {perimetro:.2f}.')
    elif numero_lados == 4:
        print(f'QUADRADO; Valor do perímetro = {perimetro:.2f}.')
    elif numero_lados == 5:
        print(f'PENTÁGONO; Valor do perímetro = {perimetro:.2f}.')
    return 
    
while True:
    try:
        numero_lados = int(input("\nDigite o número de lados de um polígono regular: "))
        medida_lado = int(input("\nDigite a medida do lado deste polígono: "))

        lados = verifica_lados(numero_lados, medida_lado)
        
        break
    except:
        print("\nNúmero inválido. Digite novamente!")
