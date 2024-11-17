from datetime import datetime

data_atual = datetime.now()
print(data_atual)

data_vencimento = datetime(year=2024, month=12, day=10)

print(data_vencimento - data_atual)