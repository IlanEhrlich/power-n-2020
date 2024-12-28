import anim #naturellement, on commence par importer le programme d'affichage que nous utiliserons 


#tous ces paramètres pourront être modifiés a posteriori dans le menu des paramètres:

l=8 #par défaut, le tableau contient 8 lignes
c=7 #par défaut, le tableau contient 7 colonnes

n=4 #par défaut,il faut aligner 4 jetons pour gagner

nj1='Benjamin' #par défaut, le joueur 1 s'appelle Benjamin (nj1 est nommé ainsi pour 'nom du joueur 1')
nj2='David' #par défaut, le joueur 2 s'appelle David


historiquecoups=[[0,0,2]] #avant que le jeu commence, il faut bien que l'historique soit vide. cependant, pour faire commencer le joueur 1, il faut qu'il contienne précédemment un 2, comme nous le verrons dans la fonction actio
derniercoup=[0,0,0] #le dernier coup est bien vide au début de la partie 
etat=0 #l'état du jeu vaut 0, c'est-à-dire en cours et non achevé
to=0 #to est le compteur de tours. il vaut 0 au début de la partie


def dic(nj1,nj2):
    
    """
    la fonction dict produit un dictionnaire qui associe le numéro d'un joueur à son nom. il suffit de lui donner deux noms en paramètres pour qu'elle retourne un dictionnaire les associant à 1 et 2 
    """
    
    return {1:nj1,2:nj2}



def tableaudepart(l,c):
    
    """
    la foncito tableaudepart génère une liste de listes correspondant au plateau de jeu. chaque liste à l'intérieur représente une ligne, et chaque rang dans une de ces listes représente une colonne 
    """
    

    lig=[]
    for i in range(l):
        col=[]
        for j in range(c):
            col.append(0)
        lig.append(col)
    return lig   



tableau0=tableaudepart(l,c) #on appelle tableau0 le tableau contenant l lignes et c colonnes

nbvic1=0 #nbvic1 représente le nombre de victoires du joueur 1
nbvic2=0 #nbvic2 représente le nombre de victoires du joueur 2
nbdef1=0 #nbvic1 représente le nombre de défaites du joueur 1
nbdef2=0 #nbvic2 représente le nombre de défaites du joueur 2

#tous ces paramètres sont à 0 lorsque le jeu est lancé



#nj=numéro du joueur
#cc=colonne choisie
#co=couleur du joueur en train de jouer



def vict(nj): 
    
    """
    vict est la fonction qui rassemble toutes le commandes à exécuter si le joueur numéro nj gagne
    """
    
    global etatv, nbvic1,nbvic2, nbdef1,nbdef2, tableau0 #il est nécessaire de mettre toutes ces variables en globales, car dans le cas d'une victoire, ils seraient tous modifiés
    print(f"victory for {dic(nj1,nj2)[nj]}!")
    anim.victorysign(dic(nj1,nj2)[nj])
    etat=1
    tableau0=tableaudepart(l,c) #à la fin d'une partie, il est nécessaire de recréer le tableau 
    
    if nj==1:
        nbvic1+=1
        nbdef2+=1
        
    else:
        nbvic2+=1
        nbdef1+=1
        
    finpartie()
        

def vv(l,c,n,i,cc,nj):
    
    """
    fonction de vérification de victoire:
    
    la fonction vv prend en paramètres:
    l: le nombre total de lignes dans le plateau en question 
    c: le nombre total de colonnes dans le tableau:
    n: le nombre de jetons à aligner pour gagner
    i: la ligne d'un jeton particulier, qui sera plus tard le jeton nouvellement placé, toutefois en partant du bas du tableau
    cc: la colonne de ce fameux jeton (cc -> colonne choisie)
    nj: le numéro du joueur en train de jouer
    
    avec ces paramètres, la fonction vv va lancer sa recherche de jetons de même couleur dans les quatre sens en partant du jeton particulier de position (-i,cc), et comptabilise les jetons de même couleur alignés. si ce nombre atteint n, il lance la fonction vict, qui annonce la victoire du joueur de numéro nj
    """
    
    
    # 1) vérification de victoire horizontale
    
    j=1 #j est le compteur de jetons alignés. comme le jeton nouveau compte déjà, il est originellement à 1 et pas à 0
    
    #tableau0[-i][cc-1] est la case du tableau choisie par le joueur. pour vérifier la victoire dans la ligne où le dernier jeton a été mis, le programme vérifie si le jeton à sa gauche ou à sa droite est de la même couleur. si c'est le cas, il lance une boucle qui parcourt tous les jetons de la même couleur qui s'enchaînent en partant du nouveau jeton, sur sa gauche et sur sa droite. à chaque fois qu'un nouveau jeton de cette couleur est remarqué, le nombre de jetons totaux qui s'enchaînent (j) augment d'un. si ce nombre atteint le nombre de jetons à aligner pour gagner (n), la victoire est annoncée
    
    t=1 #t est le "curseur" de la boucle while qui augmente d'un à chaque tour, et qui définit à quelle case le programme en est dans son analyse
    #pour éviter  les erreurs, il faut toutefois vérifier que la colonne dont on parle existe bien, il est donc nécessaire de vérifier que la colonne existe avant de la mentionner, d'où la condition supplémentaire de la boucle
    while cc-1+t in range(c) and tableau0[-i][cc-1+t]==nj:#le programme avance sa recherche vers la droite à mesure que t augmente
        j+=1
        t+=1
    
    t=1 #il est nécessaire de faire repartir le curseur à 1 pour éviter les trous dans la recherche entre le jeton nouveau et le jeton analysé. comme il est possible de gagner en plaçant un jeton au milieu de la chaîne, le compteur de jetons alignés, quant à lui, n'es pas réinitialisé.
    while cc-1-t in range(c) and tableau0[-i][cc-1-t]==nj:#le programme avance sa recherche vers la gauche à mesure que t augmente
    #ici le sens change, alors le signe de t change aussi
        j+=1
        t+=1
        
    #comme expliqué, si j égale ou dépasse n, la victoire est annoncée, et ainsi la fonction vict est lancée, qui exécute toutes les opérations à faire en cas de victoire
    if j>=n:
        vict(nj)
   


    # 2) vérification de victoire verticale 
    #même principe que pour la victoire horizontale, mais cette fois le programme parcourt la colonne et non plus la ligne. il cherche en haut et en bas du nouveau jeton des jetons de même couleur
    #cette fois, nous changeons de direction, et comme il n'est pas possible de rassembler une chaîne horizontale et une chaîne verticale pour gagner, il est nécessaire de remettre le compteur à 0 (en l'occurrence plutôt 1)
    
    j=1
    t=1
    while -(-i+t) in range(1,l+1) and tableau0[-i+t][cc-1]==nj:#le programme avance vers le bas à mesure que t augmente
    #rappelons que comme i est négatif, le curseur part du bas du tableau et non du haut. ainsi, lorsqu'un nombre positif lui est additionné, le curseur descend et ne monte pas. comme un la fonction range enegendre un intervalle positif, il faut rendre la valeur de -i+1 positive pour pouvoir les comparer, d'où son changement de signe
        j+=1
        t+=1
        
    t=1
    while -(-i-t) in range(1,l+1) and tableau0[-i-t][cc-1]==nj: #le programme avance vers le haut à mesure que t augmente   
        j+=1
        t+=1
        
    if j>=n:
        vict(nj)
        
        
        
    # 3) vérification de victoire, dans le sens allant du bas gauche au haut droit
    #même principe que précédemment, mais cette fois avec la diagonale. cette fois, on augmentera ou diminuera à la fois la colonne et la ligne
    
    j=1
    t=1
    while -(-i-t) in range(1,l+1) and cc-1+t in range(c) and tableau0[-i-t][cc-1+t]: #le programme avance vers le haut droit à mesure que t augmente: la ligne monte et la colonne aussi 
    #cette fois, il a une condition de plus, car les deux coordonnées du tableau sont variables
        j+=1
        t+=1
        
    t=1
    while -(-i+t) in range(1,l+1) and cc-1-t in range(c) and tableau0[-i+t][cc-1-t]: #le programme avance vers le bas gauche à mesure que t augmente: la ligne descend et la colonne aussi
        j+=1
        t+=1
        
    if j>=n:
        vict(nj)
    
    
    
    # 4) vérification de victoire, dans le sens allant du bas droit au haut gauche
    
    j=1
    t=1
    while -(-i-t) in range(1,l+1) and cc-1-t in range(c) and tableau0[-i-t][cc-1-t]: #le programme avance vers le haut gauche à mesure que t augmente: la ligne monte et la colonne descend
        j+=1
        t+=1
    
    t=1
    while -(-i+t) in range(1,l+1) and cc-1+t in range(c) and tableau0[-i+t][cc-1+t]: #le programme avance vers le bas droit à mesure que t augmente: la ligne descend et la colonne augmente
        j+=1
        t+=1
    
    if j>=n:
        vict(nj)

    


def reptab(tableau0):
    
    """
    la fonciton reptab représente proprement le tableau, à défaut d'un print(tableau0) dont l'apparence dépenderait de l'affichage de chaque lecteur du code. en l'occurrence, il représente bien alignée chaque ligne et chaque colonne, en plus d'afficher le numéro de chaque colonne, si bien qu'il serait aussi possible de jouer sans l'opérateur graphique
    """
    
    
    k=[]
    for i in range(1,c+1):
        k.append(i)
    print(2*'\n'+f'{k}')
    for i in range(len(tableau0)):
        print(tableau0[i])
    print(2*'\n')


    
    
def action(nj,cc): 
    global tableau0, derniercoup, historiquecoups, to
    
    """
    la fonction action est au coeur du jeu: c'est elle qui définit et exécute les opération qui agissent lorsqu'un joueur joue et place un jeton dans une colonne
    ainsi, elle prend en paramètres:
    nj: le numéro du joueur en train de jouer
    cc: la colonne qu'il choisit et qui, plus tard, sera introduite par la fonction input que le joueur remplira
    
    Principalement, elle modifie l'état du tableau à chaque tour, en plaçant dans la case adéquate le numéro du joueur qui se l'approprie par un jeton de sa couleur, et elle ordonne au programme d'animation de l'afficher
    """
    

    if cc not in range(1,c+1): #il est nécessaire de vérifier que la colonne choisie existe bien
        print("Inexisting column")

    elif tableau0[0][cc-1]!=0: #il est nécessaire de vérifier que la colonne choisie n'est pas pleine. si la ligne du haut est vide, donc contient un 0, c'est le cas. 
        print("Column full")

    else : #ces deux conditions vérifiées, on peut commencer à exécuter les opérations de chaque tour
        
        i=1 #i est le curseur variable par lequel le programme parcourt chaque ligne d'une colonne en partant du bas pour placer un jeton de la couleur du joueur en train de jouer dans la première libre qu'il aperçoit
        while tableau0[-i][cc-1]!=0:
            i+=1
         
    
        #une fois que i est assez grand pour que la ligne soit en effet libre, donc égale à 0, on peut enfin lancer nos opérations:
        
        tableau0[-i][cc-1]=nj #on remplace le 0 par un 1 ou un 2 dans cette case en foncton du joueur en train de jouer
        
        derniercoup=[l-i+1,cc,nj] #on crée une donnée de ce coup
        
        historiquecoups.append(derniercoup) #on ajoute cette donnée à la base de donnée des coups
        
        reptab(tableau0) #on représente le tableau dans le terminal
        
        anim.jeton(l,c,cc,i,nj) #on représente le tableau dans le programme d'animation, en utilisant la fonction 'jeton', définie dans l'autre module
        
        to+=1 #on augmente d'un le compteur de tours
        
        vv(l,c,n,i,cc,nj) #on lance la fonction de vérification de victoire en lui précisant les paramètres en occurrence
    
    
    
def actio(cc):
    
    """
    maintenant que toutes les opérations d'un tour sont programmées dans la fonction action, une autre fonction doit agir pour la lancer, sans que le joueur ait toujours à rappeler son numéro.
    Ainsi, la fonction actio va faire agir le joueur 1 ou le joueur 2 en foncion de l'information qu'il trouve dans l'historique des coups
    """
    
    if historiquecoups[-1][-1]==2:
        action(1,cc)

    else:
        action(2,cc)



def retour():
    
    """
    la fonction retour annule le coup qui vient d'être joué. elle sera plus tard reprise par des commandes du input
    """
    
    
    global  tableau0, historiquecoups, to 
    
    #la fonction doit donc:
    tableau0[historiquecoups[-1][0]-1][historiquecoups[-1][1]-1]=0 #1) remplacer le numéro du dernier joueur dans la case par un 0
    anim.aretour(l,c,historiquecoups[-1][0],historiquecoups[-1][1]) #2) exécuter la fonction d'animation qui efface le jeton qui vient d'être placé
    del historiquecoups[-1] #3) supprimer le dernier élément inscrit dans l'historique des coups
    to-=1 #4) soustraire de 1 le compteur de tours
    

    
def recommencer():
    
    """
    comme son nom l'indique, la fonction permet de recommencer une nouvelle partie. elle remet donc tous les paramètres du jeu comme ils l'étaient avant que celui-ci commence 
    """
    
    
    global tableau0, derniercoup, historiquecoups, to 
    
    #les variables de départ son remises à 0
    tableau0=tableaudepart(l,c)
    derniercoup=[0,0,0]
    historiquecoups=[[0,0,2]]
    
    #le programme d'animation affiche un nouveau plateau
    anim.plateaudepart(l,c)
    
    #on remet le compteur de tours à 0
    to=0
    
    
    
def homepage():
    
    """
    la fonction homepage gère les différentes commandes qui se présentent à l'entrée du jeu.
    elle pose un input, égal à A, B ou C qui débouche sur ces différentes options:
    
    A: commencement d'une nouvelle partie
    B: entrée sur la page de paramètres
    C: entrée sur la page du tableau des scores
    
    chacune renvoie à une fonction différente qui s'occupe de chacun de ces cas spécifiques; la fonction homepage ne fait qu'orienter vers la fonction appropriée en fonction de la commande choisie
    """
    
    
    anim.image('accueil') #on active l'affichage de la page d'accueil
    
    x=input("A: New game\nB: Parameters\nC: Scores\n\nChoose an option!\n")
    
    if x=='A':
        enpartie()
        
    elif x=='B':
        parametres()
        
    elif x=='C':
        tabscore()
        
    else:
        print("Wrong command") 
        homepage() #si la commande est incorrecte, la fonction est relancée
        
        

def enpartie():
    
    """
    la fonction enpartie organise les commandes dont on pourrait avoir besoin pendant la partie, c'est-à-dire celles qu'on pourrait essayer de communiquer au programme à travers le input mis à disposition à chaque tour de la partie 
    cela inclut naturellement le choix de colonne pour jouer, mais aussi les différentes options possibles, pour quitter le jeu, revenir en arrière ou recommencer une partie 
    """
    
    
    anim.plateaudepart(l,c) #il est tout de même nécessaire de faire afficher le plateau de départ 
    
    q=None #sans cette ligne, la boucle ne pourrait pas commencer, car q, l'entrée du input, doit être définie avant que la boucle commence. cepenant, étant encore neutre, on lui donne la valeur None
    
    while etat==0 and q!='A': #il y a deux possibilités pour que la boucle s'arrête, c'est-à-dire que la barre de communication avec le programme disparaisse: soit etat==1, auquel cas quelqu'un a gagné et le jeu est terminé, soit q=='A', auquel cas un des joueurs a inscrit qu'il désirait rejoindre le menu d'accueil, ce qui correspond bien à une coupure du système de communication input
        
        
        if to%2==0: #si le compteur de tours est un multiple de 2, on invite le joueur 1 à jouer, et le joueur 2 sinon. en fait, on aurait pu obtenir le même résultat en utilisant l'historique de coups plutôt que le compteur de tours
            q=input(f"Choose a column, {nj1}!")  #comme la requête de choisir une colonne se répète à chaque tour, il est nécessaire de l'ajouter à la boucle
        
        else:
            q=input(f"Choose a column, {nj2}!")
        
        
        if q.isdigit()==1: #communément aux deux cas précédents, on demande l'action du coup si q est un nombre, donc une colonne. en fait, il n'est plus nécessaire ici de différentier le cas du joueur 1 de celui du joueur 2, car ils sont déjà déterminés dans la fonction actio. les deux cas précédents ne servaient en fait que l'actionnement du message d'invitation à jouer en fonction du nom du joueur en question
            actio(int(q))
        
        elif q=='A': #cependant, comme q n'est défini qu'une fois l'évaluation du while passée, il est toujours possible d'entrer dans la boucle avec un q égal à A pour un dernier tour. ainsi, c'est tout de même dans la boucle qu'on va définir l'opération à exécuter si on entre A, ce qui n'est pas le cas de etat, qui lui, sera indirectement modifié par q, par l'intermédiaire de actio. ainsi, à la fin d'un tour, l'etat peut devenir 1 sans qu'un nouveau q soit demandé 
            homepage()  
        
        elif q=='B': 
            retour()

        elif q=='C':
            recommencer()
                    
        else:
            print("Incorrect command")
            q=None #nécessaire afin de revenir dans la boucle

    
    #le dernier cas possible est celui où etat==1. dans ce cas, on lance la fonction finpartie
    finpartie()
    
    
    
def parametres():
    
    """
    la fonction parametres organise toutes les commandes du menu des paramètres. en fait, l'affichage ne représente qu'une image où figurent les différents choix de paramètres. ceux-ci sont:
    
    A: changer le nom du joueur 1
    B: changer le nom du joueur 2
    C: changer le nombre de lignes dans la grille
    D: changer le nombre de colonnes dans la grille
    E: changer le nombre de jetons à aligner pour gagner
    R: revenir au menu d'accueil
    """
    
    
    global l, c, nj1,nj2, n, nbvic1, nbvic2, nbdef1, nbdef2 #chacune de ces variables risque d'être modifiées par les commandes du menu des paramètres, c'est pourquoi il est nécessaire de les mettre en global
    
    anim.image('parametres')
    
    p=None 
    

    while p!='R':
        p=input("Would you like:\nA: Change player 1's name\nB: Change player 2's name2\nC: Change number of lines\nD: Change number of columns\nE: Change number of tokens to align\nR: Return to homepage\n\n")
 
        
        if p=='A':
            nj1=input("What's player 1's name?")
            nbvic1=0 #lorsque le nom d'un joueur change, il est nécessaire de remettre à 0 ses statistiques de victoires et de défaites
            nbdef1=0
            
            
        elif p=='B':
            nj2=input("What's player 1's name?")
            nbvic2=0
            nbdef2=0
            
            
        elif p=='C':
            
            s=int(input("How many lines are there in your grid?"))
            
            if n>s and n>c: #il faut faire attention au cas où trop de jetons sont à aligner par rapport à la taille de la grille. si ce nombre dépasse celui de lignes ou de colonnes, c'est-à-dire qu'il n'est ni possible de les aligner dans une ligne, ni une colonne, ni une diagonale, un problème se présente. c'est pourquoi il faut l'anticiper et empêcher l'utilisateur d'entrer un nombre trop grand de jetons par rapport à la taille de la grille
                print("The size of the grid is too small compared to the number of tokens to align")
                s=int(input("How many lines are there in your grid?")) 
            
            else:
                l=s

  
        elif p=='D':
            
            s=int(input("How many columns are there in your grid?"))
            
            if n>s and n>l:
                print("The size of the grid is too small compared to the number of tokens to align")
                s=int(input("How many columns are there in your grid?"))
            
            else:
                c=s
                
                
        elif p=='E':
            
            s=int(input("Combien de jetons faut-il alignier pour gagner?"))
            
            if s>l and s>c:
                print("Il y a trop de jetons à aligner par rapport à la taille du plateau")
                s=int(input("Combien de jetons faut-il alignier pour gagner?"))
           
            else:
                n=s
         
        
        else: 
            print("Commande incorrecte") #si aucun des cas précédents n'est réalisé, il est indiqué que la commande était incorrecte, et la boucle reprend du début 
        
    
    homepage() #le seul cas possible ici est p=='R'
        
        
        
def tabscore():
    
    """
    la fonction tabscore affiche le tableau des scores, et pose un input pour permettre à l'utilisateur de revenir en arrière dans la page d'accueil
    """
    
    
    anim.tableauscores(nj1,nj2,nbvic1,nbvic2,nbdef1,nbdef2)
    
    z=input("Write R to return to the homepage")
    
    while z!='R':
        print("Incorrect command")
        z=input()

    homepage()
    
    
    
def finpartie():
    
    """
    sans trop de difficultés de cohérence, la fonction finpartie définit les opérations qui s'appliquent en fin de partie, lorsqu'un joueur gagne.
    celles-ci sont simplement:
    A: retour à la page d'accueil
    B: afficher le tableau des scores
    C: recommencer une partie, donc lancer la fonction de gestion d'une partie en cours
    """
    
    
    j=input("A: Home\nB: Scores\nC: Restart a new gane\nChoose an option!\n")
    
    if j=='A':
        homepage()
        
    elif j=='B':
        tabscore()

    elif j=='C':
        enpartie()
    
        


if __name__ == "__main__":  #lorsque le jeu est lancé, on allume les fonctions graphiques par la fonction anim.ecran, ce qui va afficher le menu d'accueil, et on lance homepage qui va introduire le début du programme 
    anim.ecran()
    homepage()