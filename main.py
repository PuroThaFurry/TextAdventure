#Main script

#Importing libraries
from utils import *

#calling json data
callstats()

#Start
clean()
next()

#if player have already played, we pass these first steps
if callstats.data["stats"]["Estacao"] == 0:

    load()

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

    estacoes = f"Perfeito! Tudo o que eu preciso agora é da sua conta bancária :3\nMentira, mas preciso saber para qual estação deseja proceguir! {name} \n\n[1] \033[31mVALE DO DISCO RÍGIDO\033[0;0m \n[2] \033[32mFLORESTA GRÁFICA\033[0;0m \n[3] \033[35mPARQUE DA RAM\033[0;0m \n[4] \033[34mPRAIA DAS FANS\033[0;0m \n"

    print(estacoes)

    estacao = input("Digite o número da estação: ")
    estacao = int(estacao)

    while estacao < 1 or estacao > 4:
        wrong()
        clean()
        print(estacoes)
        print("Como você errou isso?")
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

if callstats.data["stats"]["Estacao"] == 1:
    load()
    disk()

if callstats.data["stats"]["Estacao"] == 2:
    load()
    grafic()
    
if callstats.data["stats"]["Estacao"] == 3:
    load()
    ram()

if callstats.data["stats"]["Estacao"] == 4:
    load()
    fans()