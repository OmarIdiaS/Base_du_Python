class Personnage:
    def __init__(self, prenom):
        self.prenom = prenom
    
    def presentation(self):
        print(f"Salut je suis {self.prenom}")