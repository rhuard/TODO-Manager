#contains the backend bindings for the UIs to import and use

from item.items import Item
from priority.priority import *
from tags.tag import Tag

class Backend():

    def __init__(self):
        self._items = []

    def AddItem(self, name="Default", location="Default", priority=P_Low):
        i = Item(name, location, priority)
        self._items.append(i)


    def GetItem(self):
        return self._items

