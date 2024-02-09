# Description: This file contains the API key and the link to get the weather forecast.
from tkinter import messagebox

import requests
import tkinter as tk
from tkinter import *

def previsao():
    city = city_name.get()
    link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=pt_br"
    requisicao = requests.get(link)

    if requisicao.status_code == 200:
        requisicao_dic = requisicao.json()
        descricao = requisicao_dic["weather"][0]["description"]
        temperatura = requisicao_dic["main"]["temp"] - 273.15
        sensacao_termica = requisicao_dic["main"]["feels_like"] - 273.15
        umidade = requisicao_dic["main"]["humidity"]
        pressao = requisicao_dic["main"]["pressure"]
        precipitacao = requisicao_dic["rain"]["1h"] if "rain" in requisicao_dic else 0
        visibilidade = requisicao_dic["visibility"]
        ultimo_update = requisicao_dic["dt"]

        messagebox.showinfo("Previsão do tempo", f"Cidade: {city}\nTempo: {descricao}\nTemperatura: {temperatura} °C\nSensação térmica: {sensacao_termica} °C\nUmidade: {umidade}%\nPressão: {pressao} hPa\nChuva: {precipitacao} mm\nVisibilidade: {visibilidade} m\nÚltima atualização: {ultimo_update}")
        resultado_label = Label(window, text=resultado, font=("Courier", 12))
        resultado_label.pack()

API_KEY = "3cb478365812f07bef9bb14b4fd256ce"

window = tk.Tk()
window.title("Previsão do tempo")
window.geometry("300x100")

label = Label(window, text="Previsão do tempo", font=("Courier", 16, "italic"))
label.pack()

city_name = Entry(window, font=("Courier", 12))
city_name.pack()

button = Button(window, text="Consultar", font=("Courier", 12), command=previsao)
button.pack()

window.mainloop()
