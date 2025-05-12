from abc import ABC, abstractmethod
from functools import wraps

class Routeinterface(ABC):
    @abstractmethod
    def GetRoute(self, url):
        pass
        
    @abstractmethod
    def PostRoute(self, url):
        pass
        
    @abstractmethod
    def DeleteRoute(self, url):
        pass

def route_method(func):
    @wraps(func)
    def wrapper(self, url):
        return self.url() + url
    return wrapper

class Router(Routeinterface):
    def url(self):
        return "https://"

    @route_method
    def GetRoute(self, url):
        pass

    @route_method
    def PostRoute(self, url):
        pass

    @route_method
    def DeleteRoute(self, url):
        pass

router = Router()
print(router.GetRoute("Getrouteurl//voila voila"))
print(router.PostRoute("Postrouteurl//hehehehehe"))
print(router.DeleteRoute("Deleterouteurl//inscroyable"))