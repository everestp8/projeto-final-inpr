import json
import textwrap
import io
import os

COLORS = {
    ':r:': '\033[31m',
    ':bla:': '\033[30m',
    ':g:': '\033[32m',
    ':o:': '\033[33m',
    ':blu:': '\033[34m',
    ':pur:': '\033[35m',
    ':c:': '\033[36m',
    ':y:': '\033[93m',
    ':pin:': '\033[95m',
    '::': '\033[0m'
}

def colorize(text: str) -> str:
    for color in COLORS.keys():
        text = text.replace(color, COLORS.get(color))
    return text

def read_json(file_name: str) -> dict:
    with io.open(file_name, mode='r', encoding='utf-8') as file:
        return json.loads(file.read())

def print_msgs(msgs: list) -> None:
    for x in msgs: print(colorize('\n'.join(textwrap.wrap(x, 80, break_long_words=False))))

def show_node_title(node_title: str) -> None:
    print('#', node_title, end='\n\n')

def show_menu_options(menu_nodes: list):
    for i in range(0, len(menu_nodes)):
        print(f'[{i}]: {menu_nodes[i].get("title")}')

def  clear():
    if os.name == 'nt' or os.name == 'dos':
        os.system('cls')
    else:
        os.system('clear')
