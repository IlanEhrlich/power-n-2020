import turtle #naturellement, notre outil principal dans le programme d'affichage est la tortue. notre première opération est donc de l'importer


#comme vu dans le programme, il est parfois nécessaire de créer les variables à utiliser plus tard, quitte à les définir par None. ainsi, on les utilisera comme globales dans les fonctions, à chaque fois qu'on aura à les modifier. 
discworld= None
ATuin= None
screen = None


#cja=couleur du joueur de numéro nj. ce dictionnaire associe simplement le numéro du joueur 1 à la couleur bleue définie par #0038B8 et le joueur 2 à la couleur jaune définie par #FFDF00
cja={1:"#0038B8", 2:"#FFDF00"}
#ce dictionnaire sera en fait la seule variable globale du programme d'animation, en plus des variables de commande du programme définies plus haut



def ecran():
    
    """
    la fonction ecran rassemble toutes les commandes de création et de mise en place de la page graphique
    """
    
    
    global discworld, ATuin, screen
    discworld = turtle.Screen()
    ATuin = turtle.Turtle()
    screen = turtle.Screen()
    screen.screensize()
    screen.setup(width = 1.0, height = 1.0)
    ATuin.hideturtle()
    ATuin.speed(0)
    ATuin.pencolor("black") #puisque tous les traits seront toujours noirs dans l'affichage, on peut déjà commencer par installer le crayon comme tel 

    
    

def blank():
    
    """
    la fonction blank sert à repeindre totalement en blanc toute la page, en général pour faire place à un nouvel affichage. il faut donc à la fois effacer tous les dessins de la tortue, mais aussi effacer les gifs déjà présents. pour ce faire, on ajoute une image totalement blanche  
    """
    
    
    ATuin.clear()    
    #image('white')
    screen.addshape(r"images et animations\{0}.gif".format('white')) 
    turtle.shape(r"images et animations\{0}.gif".format('white'))
    
    
    
def image(x):

    """
    la fonction image est utilisée à chaque fois qu'une image est affichée au jeu. elle prend en paramètre le nom de l'image, efface tout le reste de l'écran et affiche l'image en la cherchant dans le dossier images et animations, en lui ajoutant .gif à la fin, étant donné que toutes les images finissent par .gif et sont dans ce même dossier
    """
    
    
    blank()

    screen.addshape(r"images et animations\{0}.gif".format(x)) 
    turtle.shape(r"images et animations\{0}.gif".format(x))

    
    
def tableauscores(nj1,nj2,nbvic1,nbvic2,nbdef1,nbdef2): 
    
    """
    la fonction tableauscores est celle qui affiche aux endroits corresponants à l'image qu'elle importe les informations sur les noms, les victoires et les défaites de chaque joueur
    """
    
    
    blank()
    image('tableauscores')
    ATuin.up()
    ATuin.goto(-267.0, 74.0)
    ATuin.color("black")
    ATuin.write(f"{nj1}", font=("Calibri", 22, 'normal', 'bold',))
    ATuin.goto(290, 74.0)
    ATuin.write(f"{nj2}", font=("Calibri", 22, 'normal', 'bold',))
    ATuin.goto(-350, 4)
    ATuin.write(f"{str(nbvic1)}", font=("Calibri", 22, 'normal', 'bold',))
    ATuin.goto(172, 4)
    ATuin.write(f"{str(nbvic2)}", font=("Calibri", 22, 'normal', 'bold',))
    ATuin.goto(-350, -60.0)
    ATuin.write(f"{str(nbdef1)}", font=("Calibri", 22, 'normal', 'bold',))
    ATuin.goto(172, -60.0)
    ATuin.write(f"{str(nbdef2)}", font=("Calibri", 22, 'normal', 'bold',))



def rayon(l,c):

    """
    la fonction rayon définit le rayon approprié à donner à chacun des petits cercles faisant office de trous dans le plateau. il dépend du plus petit espace disponible issu du nombre de lignes ou de colonnes, pour éviter de surcharger l'affichage
    """
    

    a=(580/c-10)/2
    b=(490/l-10)/2
    
    if a<b:
        r=a
        
    else: 
        r=b

    return r



def espacements(l,c):

    """
    la fonction espacements définit les espacements appropriés à mettre entre les cercles du plateau. en fonction du nombre de ligne et de colonnes, qu'elle prend en paramètres, elle retourne une valeur sur x qui correspond à l'espacement entre les colonnes et une valeur y qui correspond à celui entre les lignes. en fait, elle assigne par défaut une des deux valeurs à 10, et va définir l'autre de façon à espacer équitablement les cercles 
    """


    if c>l:
        x=10
        y=(500-2*l*rayon(l,c))/(l+1)
        
    else:
        x=(590-2*c*rayon(l,c))/(c+1)
        y=10
        
    return x,y
    
    
    
def circl(r,c):

    """
    la fonction circl fait apparaître un cercle de rayon r et de couleur c, dont le contour est noir
    """


    ATuin.width(2)
    ATuin.fillcolor(c)
    ATuin.begin_fill()
    ATuin.circle(r)
    ATuin.end_fill()



def plateaudepart(l,c):

    """
    la fonction plateaudepart est une des plus importantes du programme d'affichage. elle affiche un grand plateau avec le nombre de lignes et de colonnes indiqués en paramètres
    """


    blank() #on commence par faire le vide
    image('fondjeu') #on affiche l'image de fond, qui contiendra les options présentes durant la partie
    ATuin.width(2)
    ATuin.pencolor("black")
    
    #dessin du cadre
    ATuin.up()
    ATuin.setheading(0)
    ATuin.goto(300,0) 
    ATuin.down()
    ATuin.fillcolor("#C7C7C7")
    ATuin.begin_fill()
    ATuin.left(90)
    ATuin.forward(250)
    ATuin.left(90)
    ATuin.forward(590)
    ATuin.left(90)
    ATuin.forward(500)
    ATuin.left(90)
    ATuin.forward(590)
    ATuin.left(90)
    ATuin.forward(250)
    ATuin.end_fill()

    #passage du dessin du cadre à celui des cercles 
    ATuin.up()
    ATuin.left(90)
    ATuin.forward(590-rayon(l,c)-espacements(l,c)[0])
    ATuin.left(90)
    ATuin.forward(250-espacements(l,c)[1])
    ATuin.left(90)
    ATuin.down()

    #dessin des cercles en guise de trous
    for i in range(l):
        for i in range(c):
            ATuin.fillcolor("#FFFFFF")
            ATuin.begin_fill()
            ATuin.circle(rayon(l,c))
            ATuin.end_fill()
            ATuin.up()
            ATuin.forward(espacements(l,c)[0]+2*rayon(l,c))
            ATuin.down()
        ATuin.up()
        ATuin.left(90)
        ATuin.forward(2*rayon(l,c)+espacements(l,c)[1])
        ATuin.left(90)
        ATuin.forward(c*(espacements(l,c)[0]+2*rayon(l,c)))
        ATuin.left(180)
        ATuin.down()
    
    #numérotation des colonnes
    for i in range(c):
        ATuin.color("black")
        ATuin.write("{0}".format(i+1), font=("Calibri", 13, 'normal'))
        ATuin.up()
        ATuin.forward(espacements(l,c)[0]+2*rayon(l,c))



def victorysign(njn): #njn=nom du joueur numéro n

    """
    la fonction victorysign est celle qui fait apparaître le message de victoire dans le programme d'affichage lorsque quelqu'un gagne. puisqu'elle a un nom à afficher, c'est le seul paramètre qu'elle aura à prendre. elle affichera donc quelques lignes de félicitations, et quelques lignes pour afficher les options restantes à la fin d'une partie 
    """


    #affichage de "victoire pour njn!"
    ATuin.up()
    ATuin.goto(0,0)
    ATuin.down()
    ATuin.color("green")
    ATuin.write("Victory",align="center", font=("Calibri", 100, 'normal', 'bold',))
    ATuin.right(90)
    ATuin.up()
    ATuin.forward(130)
    ATuin.write(f"for {njn}!",align="center", font=("Calibri", 90, 'normal', 'bold',))    
    ATuin.setheading(0)
    
    #affichage des options suivantes
    ATuin.up()
    ATuin.right(90)
    ATuin.forward(120)
    ATuin.write("A: Home\nB: Scores\nC: Restart a new gane\nChoose an option!\n",align="center", font=("Calibri", 15, 'normal', 'bold',))  
    
    

def aretour(l,c,x,y):

    """
    la fonction aretour peint simplement en blanc la case désignée. elle prendra donc des paramètres x et y, x étant la ligne et y la colonne où se trouve la case en question. pour savoir où l'effectuer, elle a tout de même besoin de connaître le nombre de lignes et de colonnes de notre plateau pour en connaître la représentation et la position de chaque case, c'est pourquoi elle les prend en paramètres 
    """


    ATuin.goto(-290+espacements(l,c)[0]+rayon(l,c)+(y-1)*(2*rayon(l,c)+espacements(l,c)[0]),-250+espacements(l,c)[1]+(l-x)*(2*rayon(l,c)+espacements(l,c)[1])) #cette ligne est d'ailleurs la réplique de celle de création de ces cercles dans la fonction plateaudepart, ou même de placement d'un jeton dans la fonction jeton, à voir un peu plus loin 
    circl(rayon(l,c),"#FFFFFF")
    
   
    
#faire apparaître un jeton dans la ligne l-i et dans la colonne cc
def jeton(l,c,cc,i,nj):

    """
    la fonciton jeton sert à faire apparaître un jeton dans une case donnée. elle prend donc plusieurs valeurs en paramètres:
    
    l: le nombre total de lignes dans notre plateau
    c: le nombre total de colonnes dans notre plateau (ceux-là servent à permettre à la tortue de se situer par rapport à la forme du plateau 
    cc: la colonne choisie dans laquelle se trouve la case en question 
    i: la ligne de la case en question (toujours en partant du bas!)
    nj: le numéro du joueur en train de jouer 
    """


    #co=couleur du joueur en train de jouer
    co=cja[nj]
    
    ATuin.up()
    ATuin.width(3)
    ATuin.goto(-290+espacements(l,c)[0]+rayon(l,c)+(cc-1)*(2*rayon(l,c)+espacements(l,c)[0]),-250+espacements(l,c)[1]+(i-1)*(2*rayon(l,c)+espacements(l,c)[1]))
    ATuin.down()
    circl(rayon(l,c),co)