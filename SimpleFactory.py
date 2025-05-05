class Enfant:
    def description(self):
        return "Enfant "

class JeuneAdulte:
    def description(self):
        return "Jeune Adulte"

class Adulte:
    def description(self):
        return "Adulte"

class PersonneFactory:
    @staticmethod
    def get_class(age):
        if 1 <= age <= 9:
            return Enfant()
        elif 10 <= age <19:
            return JeuneAdulte()
        elif age >= 20:
            return Adulte()
        else:
            raise ValueError("L'age doit etre positif et superieur a 0")

try:
    age = int(input("entrez votre age: "))
    person = PersonneFactory.get_class(age)
    print("vous apaertener a la categorie: ",  person.description())
except ValueError as e:
    print("Erreur : ", e)