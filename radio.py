from pygame.mixer import Sound, music, init

init(frequency = 44100, channels = 2)

beep1 = Sound("Audios/SFX/click.wav")
beep2 = Sound("Audios/SFX/wrong.wav")

def load():
    music.load("Audios/Musicas/Morning Moo.mp3")
    play()

def play():
    music.play(loops = -1)

def next():
    Sound.play(beep1)

def wrong():
    Sound.play(beep2)