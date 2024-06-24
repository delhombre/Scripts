#!/usr/bin/python3

import os

print("Affichage d'une variable non définie")
try:
    print(message)  # type: ignore
except:
    print("Désolé, la variable 'message' n'est pas définie", end="\n\n")

#### Example with try-except-else
while True:
    try:
        diviseur = int(input("Entrez un diviseur entier : "))
        resultat = 10 / diviseur
    except ZeroDivisionError:
        print("Vous ne pouvez pas diviser un nombre par zéro")
        print("Bye Bye")
        break
    else:
        print(
            "10 divisé par " + str(diviseur) + " est égal à " + str(resultat),
            end="\n\n",
        )

#### Exemple avec try-except-except
print("*** Calcul d'un prix TVAC ***")
try:
    htva = input("Entrez un prix HTVA : ")
    # tvac = htva * 1.21
    tvac = float(htva) * 1.21
    print("Prix TVAC : " + str(tvac))
except NameError:
    print("Désolé, la variable 'tvac' n'a pas été définie")
except TypeError:
    print("Désolé, la variable 'htva' doit être convertie en float")

#### Exemple avec try-except-finally
print()
print("*** Lecture d'un fichier de configuration ***")
file = input("Entrez un fichier de configuration : ")  # /etc/host au lieu de /etc/hosts

try:
    f = open(file)
except:
    print("Le fichier " + file + " n'existe pas!")
    print("Vérifiez si le fichier n'est pas dans la liste ci-dessous", end="\n\n")
    cmd = "ls -l " + file + "*"
    os.system(cmd)
    print()
    file = input("Entrez un fichier valide : ")
finally:
    f = open(file)
    print(f.readlines(), end="\n\n")

print("À bientôt pour d'autres découvertes avec Python")
