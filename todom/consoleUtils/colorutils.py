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
    if('color' in kwargs) and ('bcolor' in kwargs) and ('style' in kwargs):
        t = _MakeFancyText(kwargs['color'], kwargs['bcolor'], kwargs['style'], kwargs['msg'])

    elif('color' in kwargs) and ('bcolor' in kwargs):
        t = _MakeTwoColorText(kwargs['color'], kwargs['bcolor'], kwargs['msg'])
    elif('color' in kwargs) and ('style' in kwargs):
        t = _MakeColorStyleText(kwargs['color'], kwargs['style'], kwargs['msg'])
    elif('bcolor' in kwargs) and ('style' in kwargs):
        t = _MakeBColorStyleText(kwargs['bcolor'], kwargs['style'], kwargs['msg'])
    elif('color' in kwargs):
        t = _MakeColorText(kwargs['color'], kwargs['msg'])
    elif('bcolor' in kwargs):
        t = _MakeBackColorText(kwargs['bcolor'], kwargs['msg'])
    elif('style' in kwargs):
        t = _MakeStyleText(kwargs['style'], kwargs['msg'])
    else:
        t = kwargs["msg"]
    return t

def _MakeTwoColorText(color, bcolor, msg):
    t = COLORS[color] + ";" + BACKGROUND_COLORS[bcolor]
    return _Decorate(t, msg)

def _MakeColorStyleText(color, style, msg):
    t = COLORS[color] + ";" + TEXT_STYLE[style]
    return _Decorate(t, msg)

def _MakeBColorStyleText(bcolor, style, msg):
    t = BACKGROUND_COLORS[bcolor] + ";" + TEXT_STYLE[style]
    return _Decorate(t, msg)

def _MakeFancyText( color, bcolor, style, msg):
    s = TEXT_STYLE[style] + ";" + COLORS[color] + ";" + BACKGROUND_COLORS[bcolor]
    return _Decorate(s, msg)

def _MakeStyleText(style, msg):
    s = TEXT_STYLE[style]
    return _Decorate(s, msg)

def _MakeBackColorText(color, msg):
    c = BACKGROUND_COLORS[color]
    return _Decorate(c, msg)

def _MakeColorText(color, msg):
    c = COLORS[color]
    return _Decorate(c, msg)

def _Decorate(fmt, msg):
    format_sequence = ESCAPE % fmt
    return format_sequence + msg + ENDC
