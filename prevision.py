# Description: This file contains the API key and the link to get the weather forecast.

import requests

API_KEY = "3cb478365812f07bef9bb14b4fd256ce"

lat = -5.11400579902402
lon = -42.79944966912756
city_name = "Demerval Lobão"

#link = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&lang=pt_br"
link = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&lang=pt_br"
requisicao = requests.get(link)

if requisicao.status_code == 200:
    print("Requisição bem sucedida")

requisicao_dic = requisicao.json()
descricao = requisicao_dic["weather"][0]["description"]
temperatura = requisicao_dic["main"]["temp"] - 273.15
sensacao_termica = requisicao_dic["main"]["feels_like"] - 273.15
umidade = requisicao_dic["main"]["humidity"]
pressao = requisicao_dic["main"]["pressure"]
precipitacao = requisicao_dic["rain"]["1h"] if "rain" in requisicao_dic else 0
visibilidade = requisicao_dic["visibility"]
ultimo_update = requisicao_dic["dt"]

print(f"Cidade: {city_name}")
print(f"Tempo: {descricao}")
print(f"Temperatura: {temperatura} °C")
print(f"Sensação térmica: {sensacao_termica} °C")
print(f"Umidade: {umidade}%")
print(f"Pressão: {pressao} hPa")
print(f"Chuva: {precipitacao} mm")
print(f"Visibilidade: {visibilidade} m")
print(f"Última atualização: {ultimo_update}")

