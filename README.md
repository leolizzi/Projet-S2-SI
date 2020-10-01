# Projet-S2-SI

Ce programme permet à 2 personnes ayant classé 10 sujets par ordre de préférence chacun de leur côté 
(il y a donc deux listes, une par personne) d'obtenir une seule liste qui tente de satisfaire les deux personnes au maxiumum.

Les sujets ont des importances de moins en moins fortes selon leur classement en suivant la loi donnée par la fonction suivante :

f(x) = pi/2 - arctan(0,5 * (x - n/2)), n étant le nombre de sujets.

![fonction_importance](fonction_importance.png)

(graphe de la courbe dans les fichiers)
