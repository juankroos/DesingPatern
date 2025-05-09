class Nombres:
    def Nom_classe():
        print("classe cree apres verification du proxy")
    
class NombreProxy:
    
    
    
    def __init__(self):
        self.liste = []
        self.liste1 = []
        self.index = 0  
    def __iter__(self):
        return self 

    def __next__(self):
        if self.index < len(self.liste):
            item = self.liste[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration  
    
    def Proxy(self,a):
        #self.liste1 = []
        if a % 2 == 0:
            self.liste1.append(a)
    def printt(self):
        for i in self.liste1:
            print(i)

a = NombreProxy() 
b = iter(a)

while True:
    data = int(input("entrer un nombre: >... "))
    b.Proxy(data) 
    if data == 0: 
        break

b.printt()