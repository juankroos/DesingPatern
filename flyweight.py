class Flyweight:
    def __init__(self):
        self.indexworker = None
        
    def chargement(dir,list):
        file = open(dir,"r")
        for i in list:
            if file == i:
                self.indexworker +=1

    def decrement():
        self.indexworker -=1
        
    def dechargement():
        if indexworker >= 0:
            file.close()

    def Systemedegestion():
        pass
        

class worker:
    _timelife = None
    _starttime = None
    
    def __inint__(self,name,timelife,starttime,Flywieght):
        self.name = name
        self._timelife = timelife
        self._starttime = starttime
        self.fin = True
        self.flyW = Flyweight()

    def LifeTime():
        for i in range(1, duree + 1):
            print(f"Seconde {i}")
            time.sleep(1)
            if i == self._timelife:
                return True
                break

    def startTime():
        time.sleep(self.starttime)
        
    def ecriture_last():
    #file = ouverture(filename,'a')
        print("enter nothing to stop   O____O ")
        while True:
            txt = input(print("->"))
            if txt == "":
                decrement()
                self.fin = False
                break
            self.file.write(txt)
        #file.close()




filename = "dataset.txt"
fly = Flyweight()
#n = input(print("entre le nombre de worker"))
worker1 = worker()
worker1.ecriture_last()



        

    
