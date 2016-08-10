#contains the backend bindings for the UIs to import and use

from priority.priority import *
from item.items import Item

class Backend():

    def __init__(self):
        self._items = []

    def AddItem(self, name="Default", location="Default", priority=P_Low):
        index = len(self._items)
        i = Item(index, name, location, priority)
        self._items.append(i)


    def GetItem(self):
        return self._items

    def ListItems(self):
        for i in range(len(self._items)):
            if not  self._items[i].Completed():
                self._items[i].PrintItem()

    def ListAllItems(self):
        for i in range(len(self._items)):
            self._items[i].PrintItem()

    def CompleteItem(self, index):
        self._items[index].Complete()
