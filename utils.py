from pygame.mixer import Sound, music, init
from datetime import date
import Estacoes.grafic
import Estacoes.disk
import Estacoes.fans
import Estacoes.ram
import json
import os

stats = "Jsons/stats.json"

init(frequency = 44100, channels = 2)

beep1 = Sound("Audios/SFX/click.wav")
beep2 = Sound("Audios/SFX/wrong.wav")

def load():

    music.stop()

    callstats()

    if callstats.data["stats"]["Estacao"] == 0: music.load("Audios/Musicas/Void.mp3")
    if callstats.data["stats"]["Estacao"] == 1: music.load("Audios/Musicas/SSD.mp3")
    if callstats.data["stats"]["Estacao"] == 2: music.load("Audios/Musicas/GPU.mp3")
    if callstats.data["stats"]["Estacao"] == 3: music.load("Audios/Musicas/RAM.mp3")
    if callstats.data["stats"]["Estacao"] == 4: music.load("Audios/Musicas/Fans.mp3")

    play()

def play():

    music.play(loops = -1)

def next():

    Sound.play(beep1)

def wrong():

    Sound.play(beep2)

def agora():

    agora.data = str(date.today())

def clean():

    os.system('cls')

def callstats():

    with open(stats, "r") as f:
        callstats.data = json.load(f)

def bumpstats():

    with open (stats, "w") as f:
        json.dump(callstats.data, f)

def disk():
    Estacoes.disk.Disk.here()

def grafic():
    Estacoes.grafic.here()

def ram():
    Estacoes.ram.here()

def fans():
    Estacoes.fans.here()

def getInput(user):
    user = input("O que deseja fazer agora? ")