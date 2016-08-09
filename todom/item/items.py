from priority.priority import *
from tags.tag import Tag

class Item():
    """
    Definition for the items which are inserted into the list
    """

    def __init__(self, name="Default", location="Default", priority=P_Low):
        self._name = name
        self._location = location
        self._priority = priority
        self._tags = []
        self._sub_tasks = []
        self _completed = False

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

    def ChangePrioirty(self, priority):
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

    #TODO: Add functionality for:
            # removing tags
            # remove/acces/modify subtasks (probably just going to be another open and edit of tag)
