import backendbind.Backend as Back

cmds = {"a" : add_item,
        "add-item" : add_item,
        "help" : hel,
        "exit" : ex}

def get_input():
    print(">> ")
    cmd = input()
    return cmd

def process(cmd):
    if cmd in cmds:
        cmd()
    else:
        print("unknown command")

def hel():
    print("Help: ")
    #TODO: finish this

def add_item():

def ex():
    exit()

def main():

if __name__ == "__main__":
    main()
