import time
import copy
class Map():
    _intance = None
    @staticmethod
    def __init__(self):
        if (_intance == None):
            print("chargement de la map en cour...")
            time.sleep(10)
            #self.data = data
            print("chargement terminer")
            Map()
        else:
            copy.deepcopy(self)
            Map()
    

    def clone (self):
        return copy.deepcopy(self)

print("creation de la map")
map = Map()

print("\n clonnage de la map...")
map1 = map.clone()
print("clonage terminer")
map1 = Map()
print("dkdkdkd")
