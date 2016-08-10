import backendbind as Back

B = Back.Backend()

def add_item():
    B.AddItem()

def get_input():
    print(">>", end = " ")
    cmd = input()
    return cmd

def hel():
    print("Help: ")
    #TODO: finish this

def ex():
    exit()

cmds = {"a" : add_item,
        "add-item" : add_item,
        "help" : hel,
        "exit" : ex}

def process(cmd):
    if cmd in cmds:
        cmds[cmd]()
    else:
        print("unknown command")

def main():
    while True:
        cmd = get_input()
        process(cmd)

if __name__ == "__main__":
    main()
