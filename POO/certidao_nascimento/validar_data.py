from datetime import datetime

def validar_data(data_str):
    formato = "%d/%m/%Y"  # Formato esperado: dia/mês/ano
    try:
        data_valida = datetime.strptime(data_str, formato)
        return True  # A data é válida
    except ValueError:
        return False  # A data é inválida

def main():
    # Exemplo de uso - data = "31/02/2024"
    data = input("Digite a data: ")
    data = "31/02/2024"
    if validar_data(data):
        print("Data válida!")
    else:
        print("Data inválida!")

main()