
import Sorcier
from Monstres import Monstre
import random
def main(): 
    boucle_de_jeu()

def boucle_de_jeu():
    monstres = [Monstre("Zombi", 5), Monstre("Necromancien", 12), Monstre('Dragon', 80)]
    sorcier = Sorcier.Sorcier('Gadalf', 30)
    while True:
        monstre = random.choice(monstres)
        print(f"Un {monstre.nom} de niveau {monstre.niveau} apparait")
        print("Voulez vous {a}ttaquer, {f}uir ou {r}echercher")
        action = input()
        action = action.lower().strip()
        if action == 'a': 
            resultat = sorcier.attaquer(monstre)
            if resultat:
                print("Vous avez gagnés")
                monstres.remove(monstre)
                if len(monstres) == 0:
                    print("Vous avez gagné la partie")
                    break
            else:
                print("Vous avez perdu !!!!")
                break
        elif action == 'f':
            print("Vous fuyez")
        elif action == 'r':
            print("Vous observez les monstres de vous ")
            for mon in monstres: 
                print(f"Il y a un  {mon.nom} de niveau {mon.niveau}")
        else:
            print("On quitte le jeu")
            break

main()


