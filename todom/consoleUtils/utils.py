#color utils

#terminal escape codes for colors
ESCAPE = '\033[%sm'
ENDC = ESCAPE % '0'

BOLD = '1'
FAINT = '2'

COLORS = {
        'black': '30',
        'red': '31',
        'green': '32',
        'yellow': '33',
        'blue': '34',
        'magenta': '35',
        'cyan': '36',
        'white': '37',
}

#TODO: get faint/bold to work with colors

def MakeFaintText(msg):
    return _Decorate(FAINT, msg)

def MakeBoldText(msg):
    return _Decorate(BOLD, msg)

def MakeColorText(color, msg):
    c = COLORS[color]
    return _Decorate(c, msg)

def _Decorate(fmt, msg):
    format_sequence = ESCAPE % fmt
    return format_sequence + msg + ENDC


