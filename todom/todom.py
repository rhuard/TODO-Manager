import backendbind as Back
from priority.priority import *

B = Back.Backend()

def add_item():
    name = input("name: ")
    location = input("location: ")
    priority = input("priority: ")
    priority = CheckPriority(priority)
    B.AddItem(name, location, priority)

def get_input():
    print(">>", end = " ")
    cmd = input()
    return cmd

def list_items():
    B.ListItems()

def hel():
    print("h [help]: -> prints this message")
    print("a [add-item] -> starts new item wizard and creates new item for list")
    print("l [list] -> list items")
    print("exit -> exits program")

def ex():
    #TODO: put a save in here?
    exit()

cmds = {"a" : add_item,
        "add-item" : add_item,
        "h" : hel,
        "help" : hel,
        "l" : list_items,
        "list" : list_items,
        "exit" : ex}

def process(cmd):
    if cmd in cmds:
        cmds[cmd]()
    else:
        print("unknown command try h for help")

def main():
    while True:
        cmd = get_input()
        process(cmd)

if __name__ == "__main__":
    main()
