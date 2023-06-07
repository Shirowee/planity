import csv
import random
import os

def randomPlanet():
    '''
    prend les infos d'une planète au hasard et crée un fichier à son curszeur
    @entree: /
    @sortie: retourne un dictionnaire
    '''
    f = open('assets/data.csv', "r", encoding = 'utf-8')
    donnees = csv.DictReader(f)
    planet = []
    for ligne in donnees:
        planet.append(dict(ligne))
    f.close()

    randomPlanet = random.randint(0,len(planet))
    
    #génére le dossier
    os.mkdir('assets/planets/' + str(randomPlanet))
    
    #génére le fichier
    fichier = open("assets/planets/" + str(randomPlanet) + "/data.txt", "x")
    fichier.write(str(planet[randomPlanet]))
    fichier.close()
    
    return planet[randomPlanet]