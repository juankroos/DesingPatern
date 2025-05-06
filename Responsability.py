from abc import ABC, abstractmethod


class Interface(ABC):
    @abstractmethod
    def verification(self, n):
        pass


class A(Interface):
    def __init__(self, next_handler=None):
        self.num = 1
        self.next_handler = next_handler  
    
    def verification(self, n):
        if self.num == n:
            print("C'est moi la classe A")
            return True
        elif self.next_handler:  
            return self.next_handler.verification(n)
        return False

class B(Interface):
    def __init__(self, next_handler=None):
        self.num = 2
        self.next_handler = next_handler
    
    def verification(self, n):
        if self.num == n:
            print("C'est moi la classe B")
            return True
        elif self.next_handler:
            return self.next_handler.verification(n)
        return False

class C(Interface):
    def __init__(self, next_handler=None):
        self.num = 3
        self.next_handler = next_handler
    
    def verification(self, n):
        if self.num == n:
            print("C'est moi la classe C")
            return True
        elif self.next_handler:
            return self.next_handler.verification(n)
        return False

class D(Interface):
    def __init__(self, next_handler=None):
        self.num = 4
        self.next_handler = next_handler
    
    def verification(self, n):
        if self.num == n:
            print("C'est moi la classe D")
            return True
        elif self.next_handler:
            return self.next_handler.verification(n)
        return False

class E(Interface):
    def __init__(self, next_handler=None):
        self.num = 5
        self.next_handler = next_handler
    
    def verification(self, n):
        if self.num == n:
            print("C'est moi la classe E")
            return True
        elif self.next_handler:
            return self.next_handler.verification(n)
        return False

class F(Interface):
    def __init__(self, next_handler=None):
        self.num = 6
        self.next_handler = next_handler
    
    def verification(self, n):
        if self.num == n:
            print("C'est moi la classe F")
            return True
        elif self.next_handler:
            return self.next_handler.verification(n)
        return False

class G(Interface):
    def __init__(self, next_handler=None):
        self.num = 7
        self.next_handler = next_handler
    
    def verification(self, n):
        if self.num == n:
            print("C'est moi la classe G")
            return True
        elif self.next_handler:
            return self.next_handler.verification(n)
        return False

class H(Interface):
    def __init__(self, next_handler=None):
        self.num = 8
        self.next_handler = next_handler
    
    def verification(self, n):
        if self.num == n:
            print("C'est moi la classe H")
            return True
        elif self.next_handler:
            return self.next_handler.verification(n)
        return False

class I(Interface):
    def __init__(self, next_handler=None):
        self.num = 9
        self.next_handler = next_handler
    
    def verification(self, n):
        if self.num == n:
            print("C'est moi la classe I")
            return True
        elif self.next_handler:
            return self.next_handler.verification(n)
        return False

class J(Interface):
    def __init__(self, next_handler=None):
        self.num = 10
        self.next_handler = next_handler
    
    def verification(self, n):
        if self.num == n:
            print("C'est moi la classe J")
            return True
        elif self.next_handler:
            return self.next_handler.verification(n)
        return False


class Responsibility:
    def __init__(self, handler):
        self.handler = handler

    def ParcourChaine(self, n):
        if not self.handler.verification(n):
            print("Aucun élément de la chaîne n'a pu traiter la requête domage.... hehehehe")


a = A()
b = B(a)
c = C(b)
d = D(c)
e = E(d)
f = F(e)
g = G(f)
h = H(g)
i = I(h)
j = J(i)

res = Responsibility(a)
inp = input("Entrez un nombre entre 1 et 10: ")


if inp.isdigit():
    inp = int(inp)
    if 1 <= inp <= 10:
        res.ParcourChaine(inp)
    else:
        print("Le nombre doit être entre 1 et 10.")
else:
    print("Veuillez entrer un nombre valide.")
