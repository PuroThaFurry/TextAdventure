from pygame.mixer import music, init

init(frequency = 44100, channels = 2)

def load():
    music.load("Audios/Musicas/Morning Moo.mp3")
    play()

def play():
    music.play(loops = -1)
