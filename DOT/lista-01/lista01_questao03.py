'''
3. Escreva um programa para ler uma temperatura em graus Fahrenheit. Faça uma função chamada celsius para calcular e retornar o valor correspondente em graus Celsius.
Fórmula: C = ((F-32)/9)*5
Obs.: Sempre tratar a entrada de dados para evitar que o programa aborte.
'''

def celsius(fahrenheit):
    celsius = ((fahrenheit-32)/9)*5
    return celsius
    
while True:
    try:
        temperatura = float(input("\nDigite uma temperatura em graus Fahrenheit: "))
        valor_convertido = celsius(temperatura)
        print(f'\nO valor correspondente em graus Celsius é {valor_convertido:.2f}.')
        break
    except:
        print("\nNúmero inválido. Digite novamente!")
