from core.utils import clear
from importlib import import_module
import isdigit

class Config:
    parent =[]
    status_sign_in= None
    file_select = []

def back(level:int=1):
    for _ in range(level-1):
        Config.parent.pop(-1)
    Config.parent.pop(-1).run()
class CallBack:
    """
        ...
    """

    def __init__(self, package, function, *args, **kwargs):
        self.function = getattr(import_module(package), function)
        self.args = args
        self.kwargs = kwargs

    def call(self):
        return self.function(*self.args, **self.kwargs)


class Route:

    def __init__(self, name, description=None, callback: CallBack = None, children=()) -> None:
        self.name = name
        self.description = description
        self.callback = callback
        # ...
        self.children = None
        if not callback: 
            self.children = children

    def run(self):
        clear()
        print(self.name)
        print(self.description or "\n")
        res = None
        if self.callback:
            self.callback:CallBack
            res= self.callback.call()
        elif (children := self.children) and res!='0':
            id_list= []
            Config.parent.append(self)
            for child in children:
                child: Route
                if (isinstance(child , private) and not Config.status_sign_in) or (isinstance(child , public)and Config.status_sign_in):
                    continue
                print(f"{children.index(child) + 1}. {child.name}")
                id_list.append(str(children.index(child) +1))
            index = (input("\n>> "))
            if index.isdigit() and index in id_list:
                index = int(index)-1
                children[index]: Route
                children[index].run()
            else:
                self.run()
        else:
            self.callback: CallBack
            self.callback.call()
        if Config.parent:
            input("Press enter to back menu ")
            back()
class private(Route):
    pass
class public(Route):
    pass

class Router:
    """
        ...
    """

    def __init__(self, name: str, route: Route) -> None:
        self.name = name
        self.route = route

    def generate(self) -> None:
        clear()
        self.route.run()
        
