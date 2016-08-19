from TODOManager.todom.backendbind import Backend as Back
from TODOManager.todom.priority.priority import *

def test_insert():
    b = Back()
    b.AddItem()
    l = b.GetItem()
    assert 1 == len(l)
    assert "Default" == l[0]._name
    assert "Default" == l[0]._location
    assert P_Low == l[0]._priority
