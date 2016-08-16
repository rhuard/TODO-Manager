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


    def GetAllItems(self):
        return self._items

    def GetItems(self):
        items = []
        for i in self._items:
            if False == i.completed:
                items.append(i)
        return items

    def CompleteItem(self, index):
        self._items[index].Complete()
