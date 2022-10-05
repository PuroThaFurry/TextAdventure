from cx_Freeze import Executable, setup

base = None

executables = [
    Executable('main.py',
               base = base,
               icon = 'Imagens/ico.jpg')
]

includeFiles = ["Jsons/", "Imagens/", "Audios/", "utils.py"]
packages = ["pygame"]
excludes = ["_distutils_hack", "PyInstaller", "altgraph", "asyncio", "cffi", "chardet",
            "concurrent", "ctypes", "curses", "cv2", "distutils", "docutils", "email",
            "html", "http", "lib2to3", "xml", "xmlrpc", "urllib", "tkinter", "unittest", "test",
            "PIL", "numpy", "ordlookup", "multiprocessing", "logging", "pygments", "pycparder"
            "setuptools", "pydoc_data", "pkg_resources"]

setup(name = 'Text Adventure',
      version = '0.1',
      description = 'Aventure-se por dentro do seu sistema, e salve-o dos Malwares!!',
      options = {'build_exe':{'include_files':includeFiles, "packages":packages, "excludes":excludes}},
      executables = executables
      )
