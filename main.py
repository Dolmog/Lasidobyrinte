import turtle
from replit import audio #Alix
import random

"""Timothé, Alexandre, Margot, Alix et Judith"""

def generate_labyrinth(rows, cols):  #Alexandre 
    """Fonction pour créer un labyrinthe aléatoire avec des murs en haut et à gauche"""
    # Créer une grille avec des murs partout
    labyrinth = [['1' for i in range(cols)] for i in range(rows)]

    # Liste des directions possibles
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]

    def is_valid(row, col):#Alexandre
        """Fonction pour vérifier si une cellule est valide"""
        return row > 0 and row < rows and col > 0 and col < cols

    def is_unvisited_neighbor(row, col):#Alexandre
        """Fonction pour vérifier si une cellule voisine est non visitée"""
        unvisited_neighbors = []
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if is_valid(new_row, new_col) and labyrinth[new_row][new_col] == '1':
                unvisited_neighbors.append((new_row, new_col))
                #print((new_row, new_col))
        return unvisited_neighbors

    # Position de départ à l'intérieur du labyrinthe
    start_col = random.randint(1, cols-2)
    labyrinth[0][start_col] = '2'
    entree = (0,start_col)
    position = (0,start_col)
    # Liste pour suivre les cellules visitées
    stack = [(0, start_col)]

    # Parcours de la grille en profondeur
    while stack:
        row, col = stack[-1]
        unvisited_neighbors = is_unvisited_neighbor(row, col)
        if unvisited_neighbors:
            new_row, new_col = random.choice(unvisited_neighbors)
            labyrinth[new_row][new_col] = '0'
            labyrinth[row + (new_row - row) // 2][col + (new_col - col) // 2] = '0'
            stack.append((new_row, new_col))
        else:
            # Retirer la cellule actuelle de la pile
            stack.pop()

    # Générer aléatoirement une sortie sur le bord inférieur
    
    w = True
    while w == True:
      exit_col = random.randint(2, cols-2)
      if labyrinth[rows-2][exit_col]!= "1" :   # si ca marche pas c'est là 
        w = False
    labyrinth[rows - 1][exit_col] = '2'
    sortie = (rows-1,exit_col)

    liste_objets_bleu = []
    for i in range(len(labyrinth)):
      for u in range(len(labyrinth[1])):
        o = random.randint(0,100)
        if labyrinth[i][u]=="0" and o == 10 :
          labyrinth[i][u] = "3"
          liste_objets_bleu.append((i,u))
    return labyrinth,sortie,liste_objets_bleu,entree,position


def f_verif_laby(labyrinth,rows,cols):#Alexandre
  """ Fonction de vérification pour vérifier que les bords du labyrinthe soient des murs """
  c = 0
  for i in range(rows):
    if labyrinth[i][cols-1] != '1':
      c+=1
  if c != 0: return False
  else : return True

def f_verif_laby2(labyrinth,rows,cols):#Alexandre
  """ Fonction de vérification pour vérifier que les bords du labyrinthe soient des murs """
  c = 0
  for i in range(rows):
    if labyrinth[rows-1][i] != '1':
      c+=1
  if c > 1: return False
  else : return True
    
def f_verif_laby3(labyrinth,rows,cols):#Alexandre
  """ Fonction de vérification pour vérifier que les bords du labyrinthe soient des murs """
  c = 0
  for i in range(rows):
    if labyrinth[0][i] != '1':
      c+=1
  if c > 1: return False
  else : return True
    
def f_créé_fichier(labyrinth):#Alexandre

  # Nom du fichier à créer et ouvrir en mode écriture
  fichier = open("plan_chateau.txt", "w")
  for i in range (len(labyrinth)):
    for y in range(len(labyrinth[1])):
      fichier.write(labyrinth[i][y])
      fichier.write(" ")
    fichier.write("\n")
  fichier.close()
  return()

# Exemple d'utilisation
rows = 44
cols = 44
labyrinth,sortie,liste_objets_bleu,entree,position = generate_labyrinth(rows, cols)
k=True
while k == True:
  labyrinth,sortie,liste_objets_bleu,entree,position = generate_labyrinth(rows, cols)
  if f_verif_laby(labyrinth,rows,cols) == True :
    if f_verif_laby2(labyrinth,rows,cols) == True :
      if f_verif_laby3(labyrinth,rows,cols) == True:
        k = False
f_créé_fichier(labyrinth)


def lire_matrice(fichier): #Margot 
  """Fonction pour lire le plan sous forme de matrice"""
  matrice = []
  f = open(fichier) #On ouvre le fichier 
  for i in f:
    matrice.append([int(x) for x in i.split()])
  return matrice


def calculer_pas(matrice):#Alexandre  Margot
  """Fonction qui attribue la bonne dimension aux cases afin que cela rentre dans le cadre de la fenetre turtle"""
  nbre_cases_y = rows*10 / len(matrice)  # nombres de cases sur la hauteur du rectangle
  nbre_cases_x = cols*10 / len(matrice[0])  # nombres de cases sur la largeur du rectangle
  if nbre_cases_y < nbre_cases_x:
    pas = nbre_cases_y
  else:  # adapte le pas en fonction de l'orientation du labyrinthe
    pas = nbre_cases_x
  return pas


def coordonnees(case, pas):  #Margot
  """Calcule les coordonées du coin inférieur gauche de la case d'où part le pion définie par ses coordonnées"""
  coo = (-240 + case[1] * pas, (200 - pas) - case[0] * pas)
  return coo  # On part du milieu de la fenetre


def tracer_case(case, couleur, pas): #Margot 
  """ Fonction pour tracer une case"""
  turtle.setheading(
    0)  # Sert à ne pas avoir plus de 1 personnage sur le terrain
  turtle.up()
  turtle.speed('fastest')  #  Pour que le labyrinthe se crée instantanément
  turtle.tracer(0)
  turtle.goto(case)
  turtle.down()
  turtle.fillcolor(couleur)
  turtle.pencolor(couleur)
  turtle.begin_fill()
  turtle.down()
  turtle.forward(pas)
  turtle.left(90)
  turtle.forward(pas)
  turtle.left(90)
  turtle.forward(pas)
  turtle.left(90)
  turtle.forward(pas)
  turtle.left(90)
  turtle.end_fill()
  turtle.up()


def afficher_plan(matrice):  #Alexandre Margot
  """Affiche le labyrinthe"""
  for x in range(len(matrice)):
    for y in range(len(matrice[0])):
      pas = calculer_pas(matrice)
      case = (x, y)
      case = coordonnees(case, pas)
      j = matrice[x][y]
      if j == 0:
        couleur = 'black' # si la case est un 0 alors c'est le chemin
      elif j == 1:
        couleur = 'blue' # si la case est un 1 alors c'est un mur
      elif j == 2:
        couleur = 'purple' # si la case est un 2 alors c'est l'entrée ou bien la sortie 
      elif j == 3:
        couleur = 'brown' # si la case est un 3 alors c'est un objet à ramasser
      tracer_case(case, couleur, pas)

def deplacer(matrice, position,mouvement):  #Margot
  """Donne les coordonnées de la nouvelle position après un mouvement"""
  nv_position = (position[0] + mouvement[0], position[1] + mouvement[1]) # Somme des positions afin d'avoir les coordonnées de la nouvelle position
  if matrice[nv_position[0]][
      nv_position[1]] == 1:  # Impossible de parcourir les murs
    nv_position = position
  else:
    print("mv", position, "-->", nv_position)
  return nv_position

def deplacer_gauche():#Alexandre Timothé Margot
  """déplacement vers la gauche"""
  global matrice, position, pas, entree, sortie, couleur, couleur_entree_sortie, couleur_objet # paramètres nécessaires 
  mouvement = (0, -1) # Pour aller vers la gauche le 0 correspond au y et le -1 a l'axe x
  audio.play_tone(0.1,174,1)
  nv_position = deplacer(matrice, position, mouvement) #appel de la fonction deplacer
  while position != nv_position:
    if position == entree or position == sortie: # si notre posititon est sur l'entrée ou la sortie
      dessine_point(coordonnees(nv_position, pas)) # On dessine le personnage sur la nouvelle position et on remet la couleur de la case violet
      tracer_case(coordonnees(position, pas), couleur_entree_sortie, pas)
    elif position in liste_objets_bleu: #si la position est sur un objet
      dessine_point(coordonnees(nv_position, pas)) #alors on deplace le perso et on remet l'objet bleu derriere
      tracer_case(coordonnees(position, pas), couleur_objet, pas)
    else:
      dessine_point(coordonnees(nv_position, pas)) #sinon on déplace le perso et on met derriere lui une case de couleur verte 
      tracer_case(coordonnees(position, pas), couleur, pas)
    if nv_position == sortie and liste_objets_bleu == [] : #si la new pos est sur la sortie et qu'on a tt les objets alors on affiche le mess de sorti
      print("Bravo, vous êtes sortie !")
      audio.play_tone(0.1,110,1)
      turtle.pencolor("red") # le message s'affiche 
      turtle.write("Bravo, vous êtes sortit !", move=False, align="center", font=("Arial", 20, "bold"))
    position = nv_position

def deplacer_droite():#Alexandre Timothé Margot
  """ Déplacement vers la droite """
  global matrice, position, pas, entree, sortie, couleur, couleur_entree_sortie, couleur_objet # parametres de notre fonction
  mouvement = (0, 1) #pour aller vers la droite, le 0 correspond au y et le 1 au x
  audio.play_tone(0.1,220,1)
  nv_position = deplacer(matrice, position, mouvement) #on appelle la fonction deplacer
  while position != nv_position:
    if position == entree or position == sortie: #sinon si notre position avant la nouvelle position est sur l'entrée ou la sortie alors
      dessine_point(coordonnees(nv_position, pas)) #On dessine le personnage sur la nouvelle position et on remet la couleur de la case violette 
      tracer_case(coordonnees(position, pas), couleur_entree_sortie, pas)
    elif position in liste_objets_bleu: #si la position est sur un objet bleu ciel
      dessine_point(coordonnees(nv_position, pas)) #alors on deplace le perso et on remet l'objet bleu derriere
      tracer_case(coordonnees(position, pas), couleur_objet, pas)
    else:
      dessine_point(coordonnees(nv_position, pas)) # sinon on déplace le perso et on met derriere lui une case de couleur verte
      tracer_case(coordonnees(position, pas), couleur, pas)
    if nv_position == sortie and liste_objets_bleu == [] :  #si la nouvelle pos est sur la sortie et qu'on a tt les objets alors on affiche le mess de sorti
      print("Bravo, vous êtes sortit !")
      audio.play_tone(0.1,220,1)
      turtle.pencolor("red")
      turtle.write("Bravo, vous êtes sortit !", move=False, align="center", font=("Arial", 20, "bold"))
    position = nv_position


def deplacer_haut():#Alexandre Timothé Margot
  """Déplacement vers le haut"""
  global matrice, position, pas, entree, sortie, couleur, couleur_entree_sortie, couleur_objet  # on ajoute tout les parametres de notre fonction
  audio.play_tone(0.1,247,1)
  mouvement = (-1, 0)  #pour aller vers le haut, le -1 correspond au y et le 0 au x
  nv_position = deplacer(matrice, position, mouvement)  #on appelle la fonction deplacer
  while position != nv_position:
    if position == entree or position == sortie:  #sinon si notre pos avant la nouvelle est sur l'entrée ou la sortie alors
      dessine_point(coordonnees(nv_position, pas))  #On dessine le personnage sur la nouvelle position et on remet la couleur de la case violet
      tracer_case(coordonnees(position, pas), couleur_entree_sortie, pas)

    elif position in liste_objets_bleu:  #si la position est sur un objet
      dessine_point(coordonnees(nv_position, pas))  #alors on deplace le perso et on remet l'objet bleu derriere
      tracer_case(coordonnees(position, pas), couleur_objet, pas)
    else:
      dessine_point(coordonnees(nv_position, pas))  #sinon on déplace le perso et on met derriere lui une case de couleur verte
      tracer_case(coordonnees(position, pas), couleur, pas)
    if nv_position == sortie and liste_objets_bleu == [] :  #si la new pos est sur la sortie et qu'on a tt les objets alors on affiche le mess de sorti
      audio.play_tone(0.1,220,1)
      turtle.pencolor("red")
      turtle.write("Bravo, vous êtes sortit !", move=False, align="center", font=("Arial", 20, "bold"))
    position = nv_position


def deplacer_bas():  #Alexandre Timothé Margot
  """Déplacement vers le bas"""
  global matrice, position, pas, entree, sortie, couleur, couleur_entree_sortie, couleur_objet # on ajoute tout les parametres de notre fonction
  audio.play_tone(0.1,261,1)
  mouvement = (1, 0)  #pour aller vers le bas, le 1 correspond au y et le 0 au x
  nv_position = deplacer(matrice, position, mouvement)  #on appelle la fonction deplacer
  while position != nv_position:
    if position == entree or position == sortie:   #sinon si notre pos avant la nouvelle est sur l'entrée ou la sortie alors
      dessine_point(coordonnees(nv_position, pas))  #On dessine le personnage sur la nouvelle position et on remet la couleur de la case violet
      tracer_case(coordonnees(position, pas), couleur_entree_sortie, pas)
    elif position in liste_objets_bleu: #si la position est sur un objet
      dessine_point(coordonnees(nv_position, pas))  #alors on deplace le perso et on remet l'objet bleu derriere
      tracer_case(coordonnees(position, pas), couleur_objet, pas)
    else:
      dessine_point(coordonnees(nv_position, pas)) #sinon on déplace le perso et on met derriere lui une case de couleur verte
      tracer_case(coordonnees(position, pas), couleur, pas)
    if nv_position == sortie and liste_objets_bleu == [] : #si la new pos est sur la sortie et qu'on a tt les objets alors on affiche le mess de sorti
      print("Bravo, vous êtes sortit !")
      audio.play_tone(0.1,220,1)
      turtle.pencolor("red")
      turtle.write("Bravo, vous êtes sortit !", move=False, align="center", font=("Arial", 20, "bold"))
    position = nv_position
  

def dessine_point(coo): #Margot 
  """Fonction qui dessine le personnage (point)"""
  global pas
  turtle.setheading(0)  # Tourne la tête de la tortue vers la droite
  turtle.up()
  turtle.goto(coo)
  turtle.forward(pas / 2)
  turtle.left(90)
  turtle.forward(pas / 2)
  turtle.dot(RATIO_PERSONNAGE * pas, COULEUR_PERSONNAGE)


def recup(): #Alexandre
  """Fonction pour récupérer les objets"""
  global matrice, position, couleur, couleur_objet, compteur, liste_objets_bleu, pas
  if position in liste_objets_bleu: #si la pos est ds la liste des objets mais on ne sait pas lequel c'est
    audio.play_tone(0.1,130,1)
    g=0
    b = True
    while g < len(liste_objets_bleu) or b == True : #alors on regarde auquel ça correspond et le supprimer
      if position == liste_objets_bleu[g] : # test si la pos est égale à une position dans la liste_objets_bleu
        del liste_objets_bleu[g] #alors on supp l'objet correspondant a l'indice i
        b = False
      g+=1
    tracer_case(coordonnees(position, pas), couleur, pas)  #on dessine le personnage et la couleur en arriere plan sans l'objet
    dessine_point(coordonnees(position, pas))

def f_Titre():  #Alexandre Alix
  """actualise le compteur d'objets et le timer"""
  global q
  title = "Le lasidobyrinthe - Nombre d'objet restant a collecter: "+str(len(liste_objets_bleu)) + " Temps écoulé: "+str(q)  
  turtle.title(title)
  q+=1
  turtle.ontimer(f_Titre, 1000)
  return q
  
  
# Attribution des valeurs globales
turtle.setup(width=0.75,height=0.75,startx=1,starty=1)
matrice = lire_matrice('plan_chateau.txt')  # On lit le plan du chateau afin de créer le labyrinthe
pas = calculer_pas(matrice)
turtle.title("Le lasidobyrinthe")
couleur = 'green'
couleur_entree_sortie = 'purple'
couleur_objet = 'light blue'
COULEUR_PERSONNAGE = 'yellow'  # Couleur du personnage
RATIO_PERSONNAGE = 0.9  # Rapport entre le diamètre du personnage et la dimension des cases
q = 0 #timer
q = f_Titre() # initialisation du timer 

"""Seconde partie du corps du programme"""

afficher_plan(matrice)  # Affiche le plan du chateau
dessine_point(coordonnees(
  position, pas))  # Affiche le personnage à sa position de départ.
turtle.listen()  # Déclenche l’écoute du clavier
turtle.onkeypress(deplacer_gauche, "Left")  # Associe à la touche Left une fonction appelée deplacer_gauche
turtle.onkeypress(deplacer_droite, "Right")
turtle.onkeypress(deplacer_haut, "Up")
turtle.onkeypress(deplacer_bas, "Down")
turtle.onkeypress(recup, "e")
turtle.mainloop() # Place le programme en position d’attente d’une action du joueur
