import numpy as np

dados = np.genfromtxt("mudancas_climaticas.csv", delimiter=",", names=True, dtype=None, encoding="utf-8")

anos = dados["Ano"]
cidades = dados["Cidade"]
temperaturas = dados["Temperatura"]
co2 = dados["CO2"]
precipitacoes = dados["Precipitação"]

print("1. Primeiras 5 linhas do dataset:")
for i in range(5):
    print(f"Ano: {anos[i]}, Cidade: {cidades[i]}, Temperatura: {temperaturas[i]:.2f} °C, CO₂: {co2[i]:.2f} ppm, Precipitação: {precipitacoes[i]:.2f} mm")
print()

media_temp = np.mean(temperaturas)
media_co2 = np.mean(co2)
media_prec = np.mean(precipitacoes)

print("2. Médias gerais:")
print(f"Temperatura média: {media_temp:.2f} °C")
print(f"CO₂ médio: {media_co2:.2f} ppm")
print(f"Precipitação média: {media_prec:.2f} mm\n")

indice_maior_temp = np.argmax(temperaturas)
print("3. Cidade com maior temperatura média anual:")
print(f"Ano: {anos[indice_maior_temp]}, Cidade: {cidades[indice_maior_temp]}, Temperatura: {temperaturas[indice_maior_temp]:.2f} °C, CO₂: {co2[indice_maior_temp]:.2f}, Precipitação: {precipitacoes[indice_maior_temp]:.2f}\n")

indice_maior_co2 = np.argmax(co2)
print("4. Cidade com maior nível de CO₂:")
print(f"Ano: {anos[indice_maior_co2]}, Cidade: {cidades[indice_maior_co2]}, Temperatura: {temperaturas[indice_maior_co2]:.2f} °C, CO₂: {co2[indice_maior_co2]:.2f}, Precipitação: {precipitacoes[indice_maior_co2]:.2f}\n")

temperaturas_fahrenheit = temperaturas * 9 / 5 + 32
print("5. Temperaturas convertidas para Fahrenheit (primeiros 5 valores):")
print(temperaturas_fahrenheit[:5])
