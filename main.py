#Importando bibliotecas
from radio import load, next, wrong
from utils import *

#Definições
def startradio():
    load()

#Inicializando funções iniciais
startradio()
callstats()

#Início do código
clean()

if callstats.data["stats"]["Estacao"] == 0:

    texto = "Para começar digite 'SouBroxa': "

    user = input(texto)
    user = user.casefold()

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
        wrong()
        clean()
        print('Seu nome não pode conter mais de 10 caracteres!')
        name = input("Nome: ")

    name = name.capitalize()

    next()
    clean()

    print("Perfeito! Tudo o que eu preciso agora é da sua conta bancária :3\n" +
        "Mentira, mas preciso saber para qual estação deseja proceguir! " + f"{name} \n\n" +
        "[1] Vale do Disco Rígido\n" +
        "[2] Floresta Gráfica\n" +
        "[3] Parque da RAM\n" +
        "[4] Praia das FANS\n")

    estacao = input("Digite o número da estação: ")
    estacao = int(estacao)

    next()
    clean()

    callstats.data["stats"] = {}
    callstats.data["stats"]["Name"] = f'{name}'
    callstats.data["stats"]["Cash"] = 0

    if estacao == 1: callstats.data["stats"]["Estacao"] = 1
    if estacao == 2: callstats.data["stats"]["Estacao"] = 2
    if estacao == 3: callstats.data["stats"]["Estacao"] = 3
    if estacao == 4: callstats.data["stats"]["Estacao"] = 4

    bumpstats()
    
else:
    pass

if callstats.data["stats"]["Estacao"] == 1: disk()
if callstats.data["stats"]["Estacao"] == 2: grafic()
if callstats.data["stats"]["Estacao"] == 3: ram()
if callstats.data["stats"]["Estacao"] == 4: fans()