from priority import *

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

    def ChangeName(self, name):
        #TODO: make sure name is string
        self._name = name

    def ChangeLocation(self, location):
        self._location = location

    def ChangePrioirty(self, priority):
        #TODO: make sure correct type... this may not happen if just using constants
        self._prioirty = priority

    def AddTag(self, tag):
        #TODO: make sure tag is string (pr a tag object is that every gets made)
        self._tags.append(tag)
        #sort tags?

    def AddSubTasks(self, task):
        #TODO: make sure task is of Item type
        self._sub_tasks.append(task)

    #TODO: Add functionality for:
            # removing tags
            # remove/acces/modify subtasks (probably just going to be another open and edit of tag)
