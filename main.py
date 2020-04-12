import random
villes = ['Oujda', 'Nador']

villes.append('casa') # insertion 
villes.insert(1, 'ahfir') # insertion après un index précis
villes.pop(3) # Supprimer un élément en prenant son index
villes.remove('Oujda') #Supprimer une valeur en présisant ça valeur
#print(villes.index('ahfir')) # afficher l'index de la valeur que vous voulez dans la liste
#villes[0] = 'Oujda'
pos = villes.index('ahfir')
villes[pos] = 'Oujda' # Modifier une valeur 
#print(villes)

#i = 0
#while i<10:
#    i += 1
    #print("valeur de i ", i)
#for ville in villes: 
    #print("ville ", ville)

#for i in range(10):
    #print("valeur de i", i)

#i = 0
#while i < len(villes): 
#    print(villes[i])
#    if villes[i] == "Oujda":
#        continue
#   i += 1

#pays = ["Maroc", "Mauritanie", "Mali", "Allemagne", "France"]

#compter le nombre des pays qui commence par M
#cmt = 0

#for country in pays: 
#    if country.startswith("M") == False : 
#        continue
#    cmt += 1
#print(cmt)

#Verification que l'utilisateur tape le bon mot de passe
#mdp = 'soleil'

#while True: 
#    essaie = input()
    
#    if essaie == mdp:
#        break
#    else:
#        print("mauvais  mot de passe")
#print("Vous avez trouvez le mdp")


#points = 5 
#lst = ["B", "R"]
"""
cnt = 0
print(lst[1])
while  True: 
    result = [random.randrange(0,2,1), random.randrange(0,2,1) , random.randrange(0,2,1)]
    print(result)
    x = input()
    if x == lst[result[0]]:
        cnt += 1
    if x == lst[result[1]]:
        cnt += 1
    if x == lst[result[2]]:
        cnt +=1
    if cnt <= 1:
        points -= 1
    else:
        points +=1
    if points >= 9:
        print("Vous avez gagné")
        break
    elif points <= 0:
        print("Vous avez perdu")
        break
#print(result)
"""

### Dictionnaire 

personne = {'prenom' : 'omar', 'nom': 'saidi', 'Nationalité': 'Marocaine', 'age': 12}
#print(personne["prenom"])

personne['localisation'] = 'Paris' ## Insertion d'une variable dans un dictionnaire 
#print(personne)

personne.pop('prenom') # Supprimer une valeur 
#print(personne)

#for k, i in personne.items(): 
    #print(k , i)
## Afficher juste les valeurs des varibles du dictionnaire 
#for valeur in personne.values(): 
    #print(valeur)


#Les tuples 
# La difference avec les listes, les tuples ils ne sont pas modifibles
tpl = (1, 2, 3, 4)

#Bastaa !!!!


### Les fonctions 
"""
def fonc():
    print("Hello")
fonc()
"""

def check_mdpp():
    mdp = input()
    if mdp == "omar":
        return True
    else:
        return False
#print(check_mdpp())

def verif_mdp(): 
    while True: 
        mdp = input()
        if mdp == "omar":
            print("Vrai mdp")
            break
        else: 
            print("Faux mdp")
#verif_mdp()

def fonction_avec_arguments(x, y):
    print("la multiplication de ", x, "et", y, "est : ", x*y)
#fonction_avec_arguments(2, 3)
"""
fichier = open('fichier.txt', 'r')
contenu = fichier.read()
contenu_ligne_par_ligne = fichier.readline()

print(fichier.readline()) 
print(fichier.readline()) 
print(contenu) 

file = open('fichier.txt', 'r+')
file.write("Salutt ")
print(file.readline())
"""



class Personnage: 
    def __init__(self, prenom, vie= 5, force= 12):
        self.prenom = prenom
        self.vie = vie
        self.force = force
        self.mort = False
    def attaquer(self, personnage): 
        personnage.vie -= self.force
        if personnage.vie <= 0:
            self.mort = True
    
    def soigner(self, personnage):
        if self.vie == 1:
            print("Impossible je n'ai pas assez de vie")
            return 
        personnage.vie += 3
        self.vie -= 1

perso1 = Personnage("Marie", 10, 15)
perso2 = Personnage("Staphane", 18, 10)
perso1.attaquer(perso2)
#print(perso2.vie)
perso1.soigner(perso2)
#print(perso2.vie)
#perso.Modifier("Jean")
#perso.Salutations()


#### Heritage 

class Soigneur(Personnage):  ## Soigneur hérite de Personnage 
    def __init__(self, prenom, vie = 5, force = 12 , magie= 10): 
        self.magie = magie 
        super().__init__(prenom, vie, force) # la classe enfant hérite les attributs de la classe mère

    def sort_soin(self, personnage): 
        if self.magie < 2: 
            print("Pas assez de magie")
            return 
        personnage.vie += 5
        self.magie -= 2

"""
perso1 = Personnage("Marie")
soigneur = Soigneur(20)
soigneur.sort_soin(perso1)
print(perso1.vie)
"""
#soigneur = Soigneur("Marie")
"""
from math import sqrt
import math
print(math.sqrt(3))
print(sqrt(3))
"""

### Alias 
"""
import random as rd 
print(rd)
"""

import module

perso = module.Personnage('Omar')
perso.presentation()












































