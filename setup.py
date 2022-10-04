import sys
from cx_Freeze import Executable, setup

base = None
if sys.platform == 'win32': base = 'win32GUI'

executables = [
    Executable('main.py',
               base = base,
               icon = 'Imagens/ico.jpg')
]

includeFiles = ["Jsons/", "Imagens/", "Estacoes/", "Audios/", "radio.py", "utils.py"]

setup(name = 'Text Adventure',
      version = '0.1',
      description = 'Aventure-se por dentro do seu sistema, e salve-o dos Malwares!!',
      options = {'build_exe':{'include_files':includeFiles}},
      executables = executables
      )
