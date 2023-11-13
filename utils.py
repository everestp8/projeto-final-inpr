import yaml
import textwrap
import io
import os

COLORS = {
    ':r:': '\033[91m',
    ':g:': '\033[92m',
    ':o:': '\033[93m',
    ':b:': '\033[94m',
    ':p:': '\033[95m',
    ':c:': '\033[96m',
    ':y:': '\033[93m',
    '::': '\033[0m'
}

def colorize(text: str) -> str:
    for color in COLORS.keys():
        text = text.replace(color, COLORS.get(color))
    return text

# def read_json(file_name: str) -> dict:
#     with io.open(file_name, mode='r', encoding='utf-8') as file:
#         return json.loads(file.read())

def read_file(file_name: str) -> dict:
    with io.open(file_name, mode='r', encoding='utf-8') as file:
        return yaml.safe_load(file)

def print_msgs(msgs: list, wrap=False) -> None:
    if wrap:
        for x in msgs:
            print(colorize('\n'.join(textwrap.wrap(x, 80, break_long_words=False))))
    else:
        for x in msgs:
            print(colorize(x))

def show_node_title(node_title: str) -> None:
    print('#', node_title, end='\n\n')

def show_menu_options(menu_nodes: list):
    for i in range(0, len(menu_nodes)):
        print(f'[{i}]: {menu_nodes[i].get("title")}')
    print('[r] Retornar')

def wait_enter(msg: str) -> None:
    try:
        input(colorize(f'\n:y:{msg}::\n'))
    except KeyboardInterrupt:
        exit()

def get_confimation(msg: str) -> bool:
    exit_opt = input(f'{msg} (s/n)\n> ')
    return exit_opt.lower() == 's'

def clear():
    if os.name == 'nt' or os.name == 'dos':
        os.system('cls')
    else:
        os.system('clear')
