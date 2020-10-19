# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 20:34:06 2020

@author: HP Victoire
"""

import math
import pandas as pd

#Q1
#On peut modifier le calcul de la distance (distance euclidienne, distance de Manhattan, etc).

#Q2
#Algo en classification -> retourne une classe
#Algo en régression -> retourne une valeur numérique (continue)
#DONC, pour utiliser l'algo en régression, on peut calculer la MOYENNE des valeurs trouvées au lieu de faire un vote
#(Si on veut sophistiquer on peut faire une moyenne pondréeée a la distance :
#   + le voisin est proche, + il a de poids sur la moyenne)


#Q3 et Q4

def chargedonnees(fichier):
    #CHARGEMENT DES DONNEES
    iris_fichier = open(fichier, "r")
    
    fi = iris_fichier.readlines() #met le fichier irix.txt sous forme d'1 grande liste
                                
    for i in range (len(fi)):
        fi[i]=fi[i].rstrip('\n') #pour retirer les \n  à la fin de chaque élmt de la liste
    
    
    
    for i in range(len(fi)):
        fi[i] = fi[i].split(",") #pour que chaque élmt de la liste soit 1 liste
                                 #fi[0] est la 1ère ligne du fichier
                                 #fi est 1 grande liste composée de plusieurs listes (fi[i])
                                 
    return fi    



def kprochevoisins(k, x_test, y_test, z_test, t_test):

    #CHARGEMENT DES DONNEES
    fi = chargedonnees('iris_apprentissage.txt')
 
    #CALCUL DE LA DISTANCE EUCLIDIENNE ENTRE LA DONNEE DE TEST ET CHAQUE DONNEE D'APPRENTISSAGE
    x_iris=[] #on récupère toutes les longueurs des sépales dans la liste x_iris
    for i in range (len(fi)): 
        x_iris.append(float(fi[i][0]))
    
    
    y_iris=[] #on récupère toutes les largeurs des sépales dans la liste y_iris
    for i in range (len(fi)): 
        y_iris.append(float(fi[i][1]))
    
    
    z_iris=[] #on récupère toutes les longueurs de pétales dans la liste z_iris
    for i in range (len(fi)): 
        z_iris.append(float(fi[i][2]))
    
    
    t_iris=[] #on récupère toutes les largeurs de pétales dans la liste t_iris
    for i in range (len(fi)): 
        t_iris.append(float(fi[i][3])) 
    
    
    type_iris=[] #on récupère tous les types d'iris dans la liste type_iris
    for i in range(len(fi)):
        type_iris.append(fi[i][4])
    
    
    liste_distances=[]
    for i in range (len(fi)) :
        liste_distances.append(math.sqrt((x_iris[i]-x_test)**2
                                         +(y_iris[i]-y_test)**2
                                         +(z_iris[i]-z_test)**2
                                         +(t_iris[i]-t_test)**2))
    
    
    #ORDONNER LES DISTANCES PAR ORDRE CROISSANT        
    liste_distances_croissantes = sorted(liste_distances)
    
    
    #PRENDRE LES TOP K TROUVES
    liste_knn=[]
    for i in range (1,k+1) :
        liste_knn.append(liste_distances_croissantes[i])
        
    
    #RETOURNER LA CLASSE LA PLUS FREQUENTE PARMIS LES TOP K
    liste_result=[]
    c=0
    while c < k:
        
        indice=liste_distances.index(liste_knn[c])
        liste_result.append(fi[indice][4])
        c=c+1
        
        
    iris_setosa =0
    iris_versicolor=0
    iris_virginica=0
    
    #ON COMPTE LE NOMBRE DE FOIS QU'APPARAISSENT LES CLASSES PARMIS LES TOP K
    for i in range(len(liste_result)):
        if liste_result[i] == 'Iris-setosa':
            iris_setosa = iris_setosa + 1
        elif  liste_result[i] =='Iris-versicolor':   
            iris_versicolor = iris_versicolor + 1
        else :
            iris_virginica = iris_virginica + 1
    
    #ON CHOISIT LA CLASSE QUI APPARAIT LE PLUS DE FOIS AFIN D'IDENTIFIER CELLE QUI CORRESPOND À LA CLASSE DE L'ÉLÉMENT TESTÉ
    maxi = max(iris_setosa, iris_versicolor, iris_virginica)  
    
    a=''
    if maxi == iris_setosa:
        a= 'Iris-setosa'
    elif maxi == iris_versicolor:
        a= 'Iris-versicolor'
    
    else :
        a='Iris-virginica'
    
    
    return a


#Q5 et 6
#On va tester notre code avec la matrice de confusion appliquée à 30 données test.
#On prendra la même valeur de k pour les 30 données à tester.
def matrice_de_confusion(k, fichier):
    
    liste_test = chargedonnees(fichier)
    liste_reelles=[]
    liste_estimees=[]
    for i in range(len(liste_test)):
        liste_test[i][0]= float(liste_test[i][0])
        liste_test[i][1]= float(liste_test[i][1])
        liste_test[i][2]= float(liste_test[i][2])
        liste_test[i][3]= float(liste_test[i][3])
        
    for i in range(len(liste_test)):
        liste_reelles.append(liste_test[i][4])
        
    for i in range(len(liste_test)):
        liste_estimees.append(kprochevoisins(k, liste_test[i][0], liste_test[i][1], liste_test[i][2], liste_test[i][3]))

    y_reelles = pd.Series(liste_reelles, name='Réelles')
    y_estimees = pd.Series(liste_estimees, name='Estimées')

    matrice_de_conf = pd.crosstab(y_reelles, y_estimees, rownames=['Réelles'], colnames=['Estimées'])
    
    return matrice_de_conf




if __name__ == '__main__':
    #Q3 et Q4 : on teste notre fonction avec une donnée du fichier :
#    k=3
#    x_test = 4.9
#    y_test = 3.0
#    z_test = 1.4
#    t_test = 0.2
    print("La classe de l'élément testé est : ", kprochevoisins(3, 4.9, 3.0, 1.4, 0.2))
    
    #Q5
    print('\n')
    print(matrice_de_confusion(3,'iris_test.txt')) #k=3
    
    #Q6
    print('\n')
    print(matrice_de_confusion(20,'iris_test.txt')) #k=20
    #Quand on augmente k, notre matrice de confusion s'améliore, donc notre classification s'améliore.
    