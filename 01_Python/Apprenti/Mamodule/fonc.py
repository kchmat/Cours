# -*- coding: utf-8 -*-
import os
def Mafonction():
    return 100;

"""definition de ma fonction de creation d'un dossier"""

def ouvrirfichier(moncontenu,monchemin="data.txt" ):
    fichier = open(monchemin, "w");
    fichier.write(moncontenu);
    fichier.close();
def lirefichier (nomfichier="data.txt"):
    f=open(nomfichier,'r')
    a=True;
    while a:
        a=f.readline();
        print(a);
    f.close();


def monchemin():
    print ("mon chemin est le suivant {0}".format(os.curdir));
    print ("mon chemin de travail est le suivant {0}".format(os.getcwd()));

def changerdir(path):
    os.chdir("D:/{0}".format(path))



a=Mafonction()
print(type(a));
print("la vlaeur de ma focntion est {0}".format(a));
monchemin();
changerdir("testpy");
monchemin();
ouvrirfichier("hollla \n amine \n koora\n");
lirefichier();