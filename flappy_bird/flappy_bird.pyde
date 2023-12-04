import math
from random import*
import processing.core
from time import*

def score():
    fill(0, 0, 255)
    text("X = " + str(round(x,1)), 20, 20)
    text("Y = " + str(round(y, 1)), 20, 40)
    text("Vitesse dx = " + str(round(dx,2)), 20, 60)
    text("Vitesse dy = " + str(round(dy, 2)), 20 , 80)
    

def initialiser():
    """
        Initialise la position et la valeur de déplacement du mobile.
    """
    global y, dy , x ,dx   
    # Position initiale
    y = 200
    x = 50
    
    # Vitesse initiale
    dy = 0
    dx = 0

def appliquer_frottements_air():
    """
        Modifie la valeur de dy pour appliquer les effets de frottements de l'air.
    """
    global dx, dy, coeff_frottement    
        
    # Appliquons le ralentissement lié au frottements de l'air
    dy = dy * coeff_frottement
    dx = dx * coeff_frottement
    
    # Si le déplacement est trop petit, on l'annule
    if abs(dy) < 0.01:
        dy = 0
    if abs(dx) < 0.01:
        dx = 0   

def keyPressed(event):
    global dy, dx
    if keyCode == 37:
        # permet de déplacer la balle à gauche en changant dx pour une valeur négative
        dx = -2
    elif keyCode == 39:
        # permet de déplacer la balle à droite en changant dx en valeur positive
        dx = 2
    elif keyCode == 38:
        # permet d'arrêter la balle en changant dx en valeur nulle 
        dx = 0
    elif keyCode == 32:
        # permet de sauter avec la balle en changant dy en valeur négative
        dy = -5

def mousePressed(event):
    global x, y
    if realiser_deplacement() == False:
        if event.button == 39 and 300<=int(mouseX)<=700 and 200<=int(mouseY)<=400:
            y = 200
            x = 50

def appliquer_gravite():
    """
        Modifie la valeur de dy pour appliquer les effets de gravité.
    """
    global y, dy, valeur_gravite   
    # la gravité a une influence sur le déplacement en y.
    dy = dy + valeur_gravite



def doit_rebondir_mur():
    """
        Renvoie True si le mobile doit rebondir sur le sol,
        False sinon.
    """
    global x
    
    # Le mobile a un diametre de 50, 
    # donc si son centre dépasse 600 - 25,
    # elle rebondit.
    if x <= 25 or x >= 975:
        return True
    else:
        return False
    
        
def appliquer_rebonds_mur():
    """
        Réalise les modifications de dy en cas de rebond sur le mur.
    """
    global x, dx
    if doit_rebondir_mur():
        dx = - dx


        
def realiser_deplacement():
    global y , x
    if y > 25 and y < 575 :  
        """
        Modifie la position du mobile en utilisant les valeurs de déplacement.
        """
        global y, dy, x, dx
        y = y + dy
        x = x + dx
        return True
    else : 
        fill(0,0,0)
        rect(300,200, 400,200)
        fill(255,255,255)
        strokeWeight(30)
        text( "GAME OVER",460,250)
        fill(255,255,255)
        rect(415,305,50,15)
        stroke(0,0,0)
        text("[RIGHT CLICK HERE] TO TRY AGAIN", 420, 310)
        strokeWeight(1)
        return False

def Initialiser_Tuyau():
    global largeur
    for i in range(1, 6):
        hauteur = randint(100, 400)
        largeur = 50    
        z = 1000/5*i
        tuyau.append({
        "x": z,
        "hauteur": hauteur,
        "largeur": largeur,
        "y_bas": hauteur + 150,  # Coordonnée y pour la tuile du bas
        "hauteur_bas": 600 - (hauteur + 150)  # Hauteur pour la tuile du bas
        })


def afficher_tuyau():
    global largeur
    for tuyaux in tuyau:
        fill(10,255,10)
        rect(tuyau["x"],0,tuyau["hauteur"],tuyau["largeur"])
        rect(tuyau["x"],tuyau["y_bas"],tuyau["hauteur_bas"],tuyau["largeur"]) 

tuyaux_initialises = False
    

def setup():
    global y, dy, x, dx,w
    global coeff_frottement, valeur_gravite
        
    # Configuration de la fenêtre
    size(1000, 600)
    background(255)
        
    # On initialise la position et la vitesse de l'objet
    initialiser()
    tuyau = []
    
    # Autres paramètres
    coeff_frottement = 0.995
    valeur_gravite = 0.2
    # Vitesse d'affichage
    frameRate(60)
       
def draw():
    global y
    
    # Tracer le fond transparent
    fill(255, 255, 255, 40)
    stroke(0)
    rect(0, 0, 1000, 600)
    
    # Tracer le mobile
    fill(255, 0, 0)
    circle(x, y, 50)
    noStroke();
    # Tracer le bec de l'oiseau
    fill(255,131,51)
    triangle(x+10, y + 22, x + 50, y, x+10, y - 22  )
    fill(255,131,51)
    stroke(0,0,0)
    line(x+10,y,x+50,y)
    #Tracer l'oeil de l'oiseau
    strokeWeight(6)
    stroke(0,0,0)
    point(x-8,y-10)
    strokeWeight(1)
        
    
    # On applique toutes les modifications nécessaires aux déplacements
    appliquer_gravite()
    appliquer_frottements_air()
    appliquer_rebonds_mur() 
    
    # Puis on réalise le déplacement
    realiser_deplacement()
    Initialiser_Tuyau()
    afficher_tuyau()
    
    
    #enfin , on affiche les informations 
    score()
    
