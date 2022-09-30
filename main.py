#Importando bibliotecas
from datetime import date
from gtts import gTTS
from speech import speaking
import threading
import time
import os

#Definições
def agora():
    agora.data = str(date.today())

def wait(data):
    time.sleep(5)
    os.remove(f"Audios/TextToSpeech/Speech{data}.mp3")

def clean():
    os.system('cls')

def speech(text):
    speak = gTTS(text, lang = 'pt-br')
    speak.save(f'Audios/TextToSpeech/Speech{agora.data}.mp3')
    speaking.audio()

#Inicializando funções iniciais
agora()

#Início do código
clean()

texto = "Para começar digite 'SouBroxa': "

speech(texto)
wait(data = agora.data)
user = input(texto)

user.casefold()

while user != 'soubroxa':
    clean()
    print("Oops, parece que você digitou errado :/")
    user = input("Para começar digite 'SouBroxa': ")

clean()

texto = 'Obrigado por inicializar nosso sistema, agora digite seu nome!'

speech(texto)
print(texto)
name = input("Name: ")

while len(name) > 10:
    clean()
    print('Seu nome não pode conter mais de 10 caracteres!')
    name = input("Nome: ")
    name = name.capitalize()

clean()
