import random

escapes = {'hex': '\x1b[', 'uni':'\u001b[', 'oct': '\033['}
styles = {'normal':0, 'bold':1,'light':2, 'italic':3, 'underline':4,'blink':5}
colors = {'black': 30, 'red': 31, 'green': 32, 'yellow': 33, 'blue': 34, 'purple': 35, 'cyan': 36, 'white':37}
bgs = {'black': 40, 'red': 41, 'green': 42, 'yellow': 43, 'blue': 44, 'purple': 45, 'cyan': 46, 'white':47}
def set_format(esc: str, style: str, color: str, bg: str):
    format = [escapes.get(esc), ';', str(styles.get(style)), ';', str(colors.get(color)), ';', str(bgs.get(bg)), 'm']
    return "".join(format)


def Color(text: str,format: str):
    ending = '\033[0;0m'
    return format + " " + text + " " + ending

def puke(text: str):
    result = ""
    for c in text:
        format = set_format("oct",random.choice(list(styles.values())),random.choice(list(colors.values())),random.choice(list(bgs.values())))
        result += Color(c,format)
    return result