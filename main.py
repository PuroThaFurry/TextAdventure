import os

def clean():
    os.system('cls')

clean()

start = input("Para começar digite 'SouBroxa': ")
start = start.casefold()

while start != 'soubroxa':
    start = input("Para começar digite 'SouBroxa': ")

clean()

print('Obrigado por inicializar nosso sistema, agora digite seu nome!')
name = input("Name: ")
name = name.capitalize()
