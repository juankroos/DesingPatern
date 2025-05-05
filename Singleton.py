class singleton:
    _instance = 'juan'
    @staticmethod
    def getInstance():
        if singleton._instance == 'juan':
            singleton()
        return singleton._instance
    def __init__(self):
        if singleton._instance != 'juan':
            raise Execption("oula")
        else:
            singleton._instance = self
if __name__ == "__main__":
    objet = singleton()
    print(objet)
    objet = singleton.getInstance()
    print(objet)