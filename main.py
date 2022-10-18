
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 22:34:11 2022

@author: antoine
"""

import math

PATH = "" #Your path where you put your files

def Lecture(fichier):
    
    data=[]
    with open(fichier,"r") as file:
        for line in file:
            temp=line.split("\n")
            temp2=temp[0]
            temp3=temp2.split(";")
            data.append(temp3)
            
    file.close()
    del data[len(data)-1]
    return data


def distance(x,y):
    return math.sqrt((float(x[0])-float(y[0]))**2+(float(x[1])-float(y[1]))**2+(float(x[2])-float(y[2]))**2+(float(x[3])-float(y[3]))**2+(float(x[4])-float(y[4]))**2+(float(x[5])-float(y[5]))**2+(float(x[6])-float(y[6]))**2+(float(x[7])-float(y[7]))**2+(float(x[8])-float(y[8]))**2+(float(x[9])-float(y[9]))**2)


  
def knn(k):
    
    print("Lecture des fichiers...")
    train=Lecture(PATH + "data.txt") + Lecture(PATH + "preTest.txt")
    test=Lecture(PATH + "finalTest.txt")
      
    print("Calcul des distances...")
    myFile = open(PATH + "Resultats.txt", "w+")
    final=[]
    print("Selection des distances puis Ecriture dans le fichier...")
    for i in test:
        classementdist=[]
        dist=0
        for j in train:
            dist= distance(i,j)
            d =[dist,j[-1]]
            classementdist.append(d)
  
        #Tri des meilleures Distances
        tri=sorted(classementdist,key=lambda x:x[0] )
        
        #On garde les K-meilleurs distances
        topk=[]
        for l in tri[:k]:
            topk.append(l[1])
            
        #Calcul et ajout des fréquences
        freq=max(topk,key=topk.count)
        final.append(freq)
        
        #ecriture de la classe prédite du point a
        myFile.write(freq+"\n")
        
    myFile.close()   
    print("Fichier créé avec succès !")
    

def knndepart(k): #Avec Data et preTest afin de chercher le k ayant la précision optimale
    
    train=Lecture(PATH +"data.txt")
    test=Lecture(PATH +"preTest.txt")

    myFile = open(PATH +"prédiction.txt", "w+")
    
    final=[]
    for i in test: 
        
        #Tri des meilleures distances        
        classementdist=[]
        dist=0
        for j in train:
            
            dist=distance(i,j)
            d = [dist,j[-1]]
            classementdist.append(d)
        
        tri=sorted(classementdist,key=lambda x:x[0] )
        topk=[]
        for l in tri[:k]:
            topk.append(l[1])
        
        #Calcul et ajout des fréquences 
        freq=max(topk,key=topk.count)
        final.append(freq)
        myFile.write(freq+"\n")
        
    myFile.close()  
    
    #Ensemble des deux classes
    testclasse=list()
    for i in range(len(test)):
        testclasse.append(test[i][-1])

        
    # Vérification des valeurs
    verif=list()
    for i in range(len(test)):
        if(test[i][-1]==final[i]):
            verif.append(1)
        else:
            verif.append(0)
    
    ##Précision par rapport à data.txt
    precision=verif.count(1)/len(verif)
    return precision

#%%  Recherche de la meilleure valeur de k (entre 1 et 80)
"""
best=[]
for i in range(1,80):
    best.append([knndepart(i),i])
    print("Pour k =",i,"nous avons une précision de :", knndepart(i))
print("La meilleure précision est pour k =",max(best))


On a une précision de 0.7314629258517034 pour k = 14, 18, 73
On garde donc k = 14

"""
#%%  Lancement du knn  
knn(14)
