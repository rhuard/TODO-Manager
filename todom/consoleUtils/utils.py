#color utils

#terminal escape codes for colors
ESCAPE = '\033[%sm'
ENDC = ESCAPE % '0'


TEXT_STYLE = {
    'bold' : '1',
    'faint' : '2',
    'underscore' : '4',
    'reverse_color' : '7',
    'concealed': 8, #for passwords or something
}

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

BACKGROUND_COLORS = {
        'black' : '40',
        "red" : '41',
        'green': '42',
        'yellow' : '43',
        'blue' : '44',
        'magenta' : '45',
        'cyan':'46',
        'white':'47',
        }

def MakeDecoratedText(*args, **kwargs):
    if 'color' in kwargs:
        return MakeColorText(kwargs['color'], kwargs['msg'])


#TODO: get changing Background Color to work as well
#TODO: get multiple modifiers happening

def MakeStyleText(style, msg):
    s = TEXT_STYLE[style]
    return _Decorate(s, msg)

def MakeBackColor(color, msg):
    c = BACKGROUND_COLORS[color]
    return _Decorate(c, msg)

def MakeColorText(color, msg):
    c = COLORS[color]
    return _Decorate(c, msg)

def _Decorate(fmt, msg):
    format_sequence = ESCAPE % fmt
    return format_sequence + msg + ENDC
