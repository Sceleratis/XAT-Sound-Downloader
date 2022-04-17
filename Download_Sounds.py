#!/usr/bin/python3 

import wget
import requests

xatAudiesUrl = "https://xat.com/content/sounds/audies/"
downloadFolder = "Sounds/"
soundStrings = "SoundStrings.txt"
extension = ".webm"

def checkWebStatus(url: str):
    print("Checking url exists for "+ url +"...")
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False

def downloadSound(name: str):
    url = xatAudiesUrl + name
    if (checkWebStatus(url)):
        print("Downloading "+ name +"; URL: "+ url)
        wget.download(url, downloadFolder + name)

def loadLinesFromFile(file: str): 
    print("Loading lines from file: "+ file)
    with open(file) as file:
        return file.readlines()

def main():
    fileLines = loadLinesFromFile(soundStrings)
    for line in fileLines:
        soundName = ((line[1:] if line[0] == "#" else line) + extension).replace('\n', '')
        print("Download: "+ soundName)
        downloadSound(soundName)

main()