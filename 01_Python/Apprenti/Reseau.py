# -*- coding: utf-8 -*-
#Importer le moodule Socket
import socket

#Créer le socket
serveur=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#lire le socket

serveur.bind((hoste,port))

#ecouter les connexion entrantes
serveur.listen(nombre_de_connxions)

#accepter un connxion

client, infos_client = serveur.accept();
