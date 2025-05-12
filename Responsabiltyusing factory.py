from abc import ABC, abstractmethod

# Interface abstraite pour les gestionnaires
class Interface(ABC):
    @abstractmethod
    def verification(self, n):
        pass

# Classe générique pour les gestionnaires
class Handler(Interface):
    def __init__(self, num, name, next_handler=None):
        self.num = num
        self.name = name
        self.next_handler = next_handler
    
    def verification(self, n):
        if self.num == n:
            print(f"C'est moi la classe {self.name}")
            return True
        elif self.next_handler:
            return self.next_handler.verification(n)
        return False

# Factory pour créer la chaîne de responsabilité
class HandlerFactory:
    @staticmethod
    def create_chain():
        # Configuration des gestionnaires (numéro, nom)
        handlers_config = [
            (1, "A"), (2, "B"), (3, "C"), (4, "D"), (5, "E"),
            (6, "F"), (7, "G"), (8, "H"), (9, "I"), (10, "J")
        ]
        
        # Création des gestionnaires et construction de la chaîne
        handlers = [Handler(num, name) for num, name in handlers_config]
        for i in range(len(handlers) - 1):
            handlers[i].next_handler = handlers[i + 1]
        
        return handlers[0] if handlers else None

# Classe pour parcourir la chaîne
class Responsibility:
    def __init__(self, handler):
        self.handler = handler

    def ParcourChaine(self, n):
        if not self.handler.verification(n):
            print("Aucun élément de la chaîne n'a pu traiter la requête domage.... hehehehe")

# Création de la chaîne via la factory
chain = HandlerFactory.create_chain()
res = Responsibility(chain)

# Entrée utilisateur
inp = input("Entrez un nombre entre 1 et 10: ")

if inp.isdigit():
    inp = int(inp)
    if 1 <= inp <= 10:
        res.ParcourChaine(inp)
    else:
        print("Le nombre doit être entre 1 et 10.")
else:
    print("Veuillez entrer un nombre valide.")