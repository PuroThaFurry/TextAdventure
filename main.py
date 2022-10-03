#Importando bibliotecas
from radio import load, next, wrong
from datetime import date
import json
import os

stats = "Jsons/stats.json"

#Definições
def agora():
    agora.data = str(date.today())

def clean():
    os.system('cls')

def startradio():
    load()

#Inicializando funções iniciais
agora()
startradio()

#Início do código
clean()

texto = "Para começar digite 'SouBroxa': "

data = agora.data
user = input(texto)

user.casefold()

while user != 'soubroxa':
    wrong()
    clean()
    print("Oops, parece que você digitou errado :/")
    user = input("Para começar digite 'SouBroxa': ")

next()
clean()

texto = 'Obrigado por inicializar nosso sistema, agora digite seu nome!'

print(texto)
name = input("Name: ")

while len(name) > 10:
    clean()
    print('Seu nome não pode conter mais de 10 caracteres!')
    name = input("Nome: ")
    name = name.capitalize()

clean()

print("Perfeito! Tudo o que eu preciso agora é da sua conta bancária :3\n" +
      "Mentira, mas preciso saber para qual estação deseja proceguir! " + f"{name} \n" +
      "[1] Vale do Disco Rígido\n" +
      "[2] Floresta Gráfica\n" +
      "[3] Parque da RAM\n" +
      "[4] Praia das FANS")

estacao = input("Digite o número da estação: ")

data["Name"] = name

with open (stats, "r", encoding = "utf-8") as f:
    json.dump(data, f)

if estacao == 1:
    data["Estacao"] = 1