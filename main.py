#Importando bibliotecas
from datetime import date
from radio import load
import os

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
    clean()
    print("Oops, parece que você digitou errado :/")
    user = input("Para começar digite 'SouBroxa': ")

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
      "Mentira, mas preciso saber para qual estação deseja proceguir!" + name)
input("Digite o número da estação: ")