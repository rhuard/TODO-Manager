from priority.priority import *
from tags.tag import Tag

class Item():
    """
    Definition for the items which are inserted into the list
    """

    def __init__(self, index, name="Default", location="Default", priority=P_Low):
        self.name = name
        self.location = location
        self.priority = priority
        self.tags = []
        self.sub_tasks = []
        self.completed = False
        self.index = index

    def ChangeName(self, name):
        successfull = False
        if True == isinstance(name, str):
            self._name = name
            successfull = True
        return successfull

    def ChangeLocation(self, location):
        successfull = False
        if True == isinstance(name, str):
            self._location = location
            successfull = True
        return successfull

    def ChangePriority(self, priority):
        #TODO: make sure correct type... this may not happen if just using constants
        self._prioirty = priority

    def AddTag(self, tag):
        successfull = False
        if True == isinstance(tag, Tag):
            if tag not in self._tags:
                self._tags.append(tag)
            successfull = True
        return successfull

    def AddSubTasks(self, task):
        successfull = False
        if True == isinstance(task, Item):
            if task not in self._sub_tasks:
                self._sub_tasks.append(task)
            successfull = True
        return successfull

    def Complete(self):
        self._completed = True

    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, p):
        self.__priority = p

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, index):
        self.__index = index

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, loc):
        self.__location = loc

    @property
    def completed(self):
        return self.__completed

    @completed.setter
    def completed(self,completed):
        self.__completed = completed

    @property
    def tags(self):
        return self.__tags

    @tags.setter
    def tags(self, tags):
        self.__tags = tags

    #TODO: Add functionality for:
            # removing tags
            # remove/acces/modify subtasks (probably just going to be another open and edit of tag)
