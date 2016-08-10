import backendbind as Back

B = Back.Backend()

def add_item():
    B.AddItem()

def get_input():
    print(">>", end = " ")
    cmd = input()
    return cmd

def hel():
    print("h [help]: -> prints this message")
    print("a [add-item] -> starts new item wizard and creates new item for list")
    print("exit -> exits program")

def ex():
    #TODO: put a save in here?
    exit()

cmds = {"a" : add_item,
        "add-item" : add_item,
        "h" : hel,
        "help" : hel,
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
