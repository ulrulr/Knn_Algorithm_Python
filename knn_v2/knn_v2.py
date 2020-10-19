# -*- coding: utf-8 -*-
"""
Created on Thu May  7 14:55:27 2020

@author: HP Victoire
"""

import math


#CHARGEMENT DES DONNEES
def chargedonnees(fichier):
    
    dataset = open(fichier, "r")
    
    fi = dataset.readlines() #met le fichier dataset.csv sous forme d'1 grande liste
                                
    for i in range (len(fi)):
        fi[i]=fi[i].rstrip('\n') #pour retirer les \n  à la fin de chaque élmt de la liste
    
    
    
    for i in range(len(fi)):
        fi[i] = fi[i].split(";") #";" est le séparateur des éléments,de chaque liste
                                 
    return fi    



def kprochevoisins(k, x_test, y_test, z_test, t_test):

    #CHARGEMENT DES DONNEES
    fi = chargedonnees('apprentissage.csv')
 
    #CALCUL DE LA DISTANCE EUCLIDIENNE ENTRE LA DONNEE DE TEST ET CHAQUE DONNEE D'APPRENTISSAGE
    x_data=[] #on récupère tous les x (1ère colonne du fichier csv) dans la liste x_data
    for i in range (len(fi)): 
        x_data.append(float(fi[i][0]))
    
    
    y_data=[] #on récupère tous les y (2e colonne du fichier csv) dans la liste y_data
    for i in range (len(fi)): 
        y_data.append(float(fi[i][1]))
    
    
    z_data=[] #on récupère tous les z (3e colonne du fichier csv) dans la liste z_data
    for i in range (len(fi)): 
        z_data.append(float(fi[i][2]))
    
    
    t_data=[] #on récupère tous les t (4e colonne du fichier csv) dans la liste t_data
    for i in range (len(fi)): 
        t_data.append(float(fi[i][3])) 
    
    
    type_data=[] #on récupère toutes les classes (5e colonne du fichier csv) dans la liste type_data
    for i in range(len(fi)):
        type_data.append(fi[i][4])
    
    
    liste_distances=[]
    for i in range (len(fi)) :
        liste_distances.append(math.sqrt((x_data[i]-x_test)**2
                                         +(y_data[i]-y_test)**2
                                         +(z_data[i]-z_test)**2
                                         +(t_data[i]-t_test)**2))
    
    
    #ORDONNER LES DISTANCES PAR ORDRE CROISSANT        
    liste_distances_croissantes = sorted(liste_distances)
    
    
    #PRENDRE LES TOP K TROUVES
    liste_knn=[]
    for i in range (k) :
        liste_knn.append(liste_distances_croissantes[i])
        
    
    #RETOURNER LA CLASSE LA PLUS FREQUENTE PARMIS LES TOP K
    liste_result=[] #liste des classes estimées
    c=0
    coeff = k #on va rajouter "coeff fois" la classe dans la liste_result
                #on affecte une pondération : + le voisin est proche, + il a de poids
    while c < k:
        
        indice=liste_distances.index(liste_knn[c]) #on récupère l'indice
        while coeff!=0:
            liste_result.append(fi[indice][4])
            coeff=coeff-1
        coeff=k-1 #on attribue au voisin le plus proche un coeff =k, puis à 
                    #chaque fois qu'on s'éloigne, on décrémente le coeff de 1      
        c=c+1
        
    
    #ON COMPTE LE NOMBRE DE FOIS QU'APPARAISSENT LES CLASSES PARMIS LES TOP K
    result = [[x,liste_result.count(x)] for x in set(liste_result)]
    #result[ind][0] : la classe de la variable x
    #result[ind][1] : le nb de fois que la classe de la variable x apparait dans 
    #                 la liste de toutes les classes retournées précédemment
    
    
    N=[]
    for i in range(len(result)):
        N.append(result[i][1])
    
    maxi=max(N)    #occurence de la classe qui apparaît le plus
    
    ind=0
    while result[ind][1] != maxi: #on cherche l'indice qui nous donnera la classe qui apparait le plus de fois
        ind=ind+1
        
    
    prev = result[ind][0] #classe qui apparait le plus
    
    
    return prev

def returnData(k,fichier):
    
    liste_test = chargedonnees(fichier)
    liste_estimees=[]
    for i in range(len(liste_test)):
        liste_test[i][0]= float(liste_test[i][0])
        liste_test[i][1]= float(liste_test[i][1])
        liste_test[i][2]= float(liste_test[i][2])
        liste_test[i][3]= float(liste_test[i][3])
            
    
    #print(liste_reelles)    
    
    for i in range(len(liste_test)):
        liste_estimees.append(kprochevoisins(k, liste_test[i][0], liste_test[i][1], liste_test[i][2], liste_test[i][3]))
     
    
    fi = open("VictoireLopez_UlrichMama.txt", "w")
    for i in range(len(liste_estimees)):
      fi.write(liste_estimees[i]+'\n')
     
    fi.close()    
    
    print("Le fichier a été créé")
    
    return fi



if __name__ == '__main__':
    
    print(returnData(3,'finalTest.csv'))

   