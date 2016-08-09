
class Tag():
    """
    Base class for tags
    """

    def __init__(self, name="default", forecolor="WHITE", backcolor="BLACK"):
       self._name = name
       self._forecolor = forecolor
       self._backcolor = backcolor

       def GetName(self):
           return self._name

       def GetColor(self):
           return (self._forecolor, self._backcolor)
