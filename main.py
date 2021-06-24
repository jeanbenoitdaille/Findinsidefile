import os
from glob import glob
     
dossier = "/Users/thibh/Documents"
fichier_a_trouver = "fichier_a_trouver.txt"
     
fichiers = glob(dossier + "/**", recursive=True)
fichiers_trouves = [f for f in fichiers if os.path.split(f)[1] == fichier_a_trouver]
print(fichiers_trouves)