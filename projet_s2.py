# -*- coding: utf-8 -*-
#!/usr/bin/env python

from math import atan, pi

#Ordre des sujets du premier membre du groupe
l1 = [1,2,3,4,5,6,7,8,9,10]
#Ordre des sujets du second membre du groupe
l2 = [2,11,12,13,14,15,16,17,18,19]

project = {1:'Boite aux lettres',
           2:'Miroir connecté',
           3:'Lanterne Android',
           4:'Eolienne',
           5:'Gameboy',
           6:'Ecran TDB',
           7:'Fusée à eau',
           8:'Rocket Stove',
           9:'Distributeur croquettes',
           10:'Télescope ISS',
           11:'Origami',
           12:'Maison connectée',
           13:'Robot TT',
           14:'Robot mécanoide',
           15:'Labyrinthe',
           16:'Borne arcade',
           17:'Caméra kart',
           18:'Ecran holographique',
           19:'Tracker GPS'
        }

def coefList(l1, l2):
    
    """
    Affecte un coefficient à chaque sujet selon son classement dans la liste
    
    Return une liste de tuple (numeroSujet, sonCoef)
    """
    
    l3 = []
    l4 = []
    
    #Nombre de sujets
    n = len(project)
    c = 0.5
    
    def importance(i):
        return pi / 2 - atan(c * (i - n/2))
    
    #On affecte des coefs en fonction de la position dans la liste
    for i in range(len(l1)):
        t1 = (l1[i], importance(i))
        l3.append(t1)
    for j in range(len(l2)):
        t2 = (l2[j], importance(j))
        l4.append(t2)
        
    d = {}
    for k in range(2*len(l3)):
        d[k] = 0  
        
    #On aditionne les coefs de chaque projet à l'ancien (si inexistant 0)
    for i, j in zip(l3, l4):
        d[i[0]] += i[1]
        d[j[0]] += j[1]
    
    #Liste de tuples de la forme [(numéro 1, coef 1), ..., (numéro n, coef n)]       
    return list(d.items())

l = coefList(l1, l2)

def sortedList(l):
    
    """
    Trie la liste dans l'ordre des coefficients décroissants
    et ne garde que les 10 premiers tuples
    """
    
    def getKey(item): 
        return item[1]
    
    return sorted(l, key=getKey, reverse=True)[:10]

#La liste triée par coef
l = sortedList(l)


#Affichage
for i in range(len(l)): 
    projectName = project[l[i][0]]
    weight = l[i][1]
    
    if len(projectName) < 10:
        print('{:>2} : {} \t\t({:.3f})'.format(i+1, projectName, weight))
    else:
        print('{:>2} : {} \t({:.3f})'.format(i+1, projectName, weight))


        
