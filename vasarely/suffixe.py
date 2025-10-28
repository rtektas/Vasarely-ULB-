"""
projet 1 (Vasarely):
dessine un pavage hexagonale
et fait une deformation circulaire dans un endroit
du pavage selon les paramètres reçus
Auteur: Tektas Resul
Date: 26-10-19
"""
from deformation import deformation
import turtle
from math import pi, sin, cos, radians
turtle.tracer(0,0)
def hexagone(point,longueur,col,centre,rayon):
    """
    Dessine avec turtle un hexagone
    en position ( abscisse_centre, ordonnee_centre)
    paramètres :
    -longueur: la  longueur de chaque arête de l'hexagone
    -centre: centrede la déformation
    -rayon: le rayon de la sphère de déformation
    """
    turtle.up()
    c_x, c_y, c_z = centre
    color1, color2, color3 = col
    abscisse_centre, ordonnee_centre = point
    deformat = deformation((point[0],point[1],0),centre,rayon) # variable déformé
    angle = 0
    couleur = 0
    turtle.goto(deformat[0],deformat[1]) # coordonnées du centre de l'hexagone déformé
    turtle.down()
    for i in range(3): # à chaque itération, trace un losange
        turtle.color(col[couleur])
        turtle.begin_fill()
        for i in range(3): # à chaque itération, trace un segment pour former le losange
            cosinus = longueur * cos(radians(angle))
            sinus = longueur * sin(radians(angle))
            x, y, z = deformation((cosinus+point[0], sinus+point[1], 0), centre, rayon)
            turtle.goto(x,y)
            angle+=60 # augmente l'angle de 60 pour le pivotage
        turtle.goto(deformat[0],deformat[1])
        turtle.end_fill()
        angle -= 60
        couleur += 1 # augmente de 1 pour le changement de couleur

def pave(inf_gauche, sup_droit,longueur,col,centre,rayon):
    """
    Dessine avec turtle un pave hexagonal
    en position ( abscisse_centre, ordonnee_centre)
    paramètres :
    -inf_gauche: coordonnées inférieur du pavage (debut)
    -sup_droit: coordonnées supérieur du pavage (fin)
    -longueur: la  longueur de chaque arête du pavé
    -col: les couleurs des 3 losanges des hexagones
    -centre: centrede la déformation
    -rayon: le rayon de la sphère de déformation
    """
    col1,col2,col3 = col
    c_x, c_y, c_z = centre
    a = 0
    x = inf_gauche
    y = inf_gauche
    y1=sup_droit
    while y < y1:
        """Tant que les coordonnées supérieur du pavage n'est pas atteint : continue 
        de dessiner des lignes d'hexagones"""
        x=inf_gauche
        y=inf_gauche+a
        while x< sup_droit-(longueur*2): # lignes d'hexagones inférieur
                hexagone((x,y),longueur,col,centre,rayon)
                x+=longueur*3 # l'ecart entre les hexagones
        x = inf_gauche + longueur + 10
        y = inf_gauche + longueur - 2.8+a
        while x< sup_droit-(longueur*2): # lignes d'hexagones supérieur
                hexagone((x,y),longueur,col,centre,rayon)
                x+=longueur*3
        a+=longueur + 15


pave(-300, 300, 20,('brown','yellow','black'),(-50,-50,0),240)
turtle.done()
