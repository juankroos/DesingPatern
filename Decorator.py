from abc import ABC, abstractmethod


class Router:
    def url(self):
        return "https://"


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


class Routedecorator(Routeinterface):
    def __init__(self, router):
        self._router = router  

    def GetRoute(self, url):
        return self._router.url() + url
        
    def PostRoute(self, url):
        return self._router.url() + url
        
    def DeleteRoute(self, url):
        return self._router.url() + url


router = Router()  
decorated_router = Routedecorator(router)  

print(decorated_router.GetRoute("Getrouteurl//voila voila"))
print(decorated_router.PostRoute("Postrouteurl//hehehehehe"))
print(decorated_router.DeleteRoute("Deleterouteurl//inscroyable"))
