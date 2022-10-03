from datetime import date
import json
import os

stats = "Jsons/stats.json"

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