import os
os.system("color")
colors = ['grey','red','green','yellow','blue','magenta','cyan','white',]

colorsWithValues = {color:num for color, num in zip(colors, range(30, 30+len(colors)))}

resetString = '\033[0m'


def color(text, color=None):
    if os.getenv('ANSI_COLORS_DISABLED') is None:
        formatStr = '\033[%dm%s'
        if color is not None:
            text = formatStr % (colorsWithValues[color], text)
        text += resetString
    return text

