# -*- coding: utf-8 -*-
import datetime
import os
#definition de la fonction qui affiche mon menu

def PrintMenu():
    print("please inserer une commande pour continue");
    print("1\ E pour Exporter");
    print("2\ I pour effacer l'ecran");
    print("3\ A pour ecrire dans un fichier /tmp/aminmodule.txt");
    print("4\ Q pour quitter le programme");
    print("5\ L pour lister les packages installer sur ce serveur")


#definition de la fonction qui crée un fichier
def EcrireFichier(monchemin="default.txt" ):
    fichier = open(monchemin, "w");
    fichier.write("Amine M9Awadeeeee moncontenu");
    fichier.close();


def changerdir(path='/tmp/'):
    os.chdir("{0}".format(path))


def ListerPack():
    os.system('yum list installed')



today =datetime.date.today();
print(today)
#k=raw_input("entrer une lettre:")
#print(k)
PrintMenu()
b=True;
while b==True:
    a=raw_input(">");
    if a=="Q":
        #b=False;
        break;
    elif a=="E":
        e=raw_input("please entrer le nom de fichier a créer:")
        changerdir();
        EcrireFichier(e);
        PrintMenu();
    elif a=="L":
        ListerPack();
        PrintMenu();
    else:
        PrintMenu()
print("c'est bon c'est plus dans le menu des commande");

