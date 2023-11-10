import json
import io
import os

def read_json(file_name: str) -> dict:
    with io.open(file_name, mode='r', encoding='utf-8') as file:
        return json.loads(file.read())

def print_msgs(msgs: list) -> None:
    for x in msgs: print(x)

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
