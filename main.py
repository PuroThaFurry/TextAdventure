#Importando bibliotecas
from datetime import date
from gtts import gTTS
import pygame.mixer
import os

#Inicializar o mixer
pygame.mixer.init(frequency = 44100, channels = 2)

def agora():
    agora.data = date.today()

def clean():
    os.system('cls')

def speech(text):
    speak = gTTS(text, lang = 'pt-br')
    speak.save(f'Audios/TextToSpeech/Speech{agora.data}.mp3')
    speak

clean()

text = "Para começar digite 'SouBroxa': "

speech(text)
input(text)

text = text.casefold()

while text != 'soubroxa':
    clean()
    print("Oops, parece que você digitou errado :/")
    text = input("Para começar digite 'SouBroxa': ")

clean()

print('Obrigado por inicializar nosso sistema, agora digite seu nome!')
name = input("Name: ")

while len(name) > 10:
    clean()
    print('Seu nome não pode conter mais de 10 caracteres!')
    name = input("Nome: ")
    name = name.capitalize()

clean()
