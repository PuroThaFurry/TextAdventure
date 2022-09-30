from playsound import playsound
from datetime import date
import pygame.mixer

class speaking():
    def __init__(self):
        pygame.mixer.init()

    def audio():
        data = str(date.today())
        playsound(f"Audios/TextToSpeech/Speech{data}.mp3")