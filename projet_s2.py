# -*- coding: utf-8 -*-
#!/usr/bin/env python

lf = []
d1 = {}
d2 = {}
d = {}

l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = [2,11,12,13,14,15,16,17,18,19]

project = {1:'Boite aux lettres',
           2:'Mirroir connecté',
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

def coef(l1, l2):
    #On affecte des coefs en fonction de la position dans la liste
    for i in range(len(l1)):
        d1[l1[i]] = 1 / (i+1)
    for j in range(len(l2)):
        d2[l2[j]] = 1 / (j+1)
        
    l3 = d1.items()
    l4 = d2.items()
    
    for k in range(2*len(l3)):
        d[k] = 0  
        
    #On aditionne les coefs de chaque projet à l'ancien (si inexistant 0)
    for i, j in zip(l3, l4):
        d[i[0]] += i[1]
        d[j[0]] += j[1]
    
    #Liste de tuples de la forme [(numéro 1, coef 1), ..., (numéro n, coef n)]       
    return d.items()

def getKey(item):
    return item[1]

#On trie la liste dans l'ordre des coefs décroissants
lf = sorted(coef(l1, l2), key=getKey, reverse=True)[:10]


#Affichage
for i in range(len(lf)):
    projectNumber = lf[i][0]
    
    if (i+1)/10 < 1:
        if len(project[projectNumber]) < 13:
            print('{}  : {}\t\t\t({:.3f})'.format(i+1, project[projectNumber], lf[i][1]))
        else:
            print('{}  : {}\t\t({:.3f})'.format(i+1, project[projectNumber], lf[i][1]))       
    else:
        if len(project[projectNumber]) < 13:
            print('{} : {}\t\t\t({:.3f})'.format(i+1, project[projectNumber], lf[i][1]))
        else:
            print('{} : {}\t\t({:.3f})'.format(i+1, project[projectNumber], lf[i][1]))

        
