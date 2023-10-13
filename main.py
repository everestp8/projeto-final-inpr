import sys
import utils as u
import nodes 

def main() -> None:
    file_name: str = sys.argv[1]
    template: dict = u.read_json(file_name).get('body')
    if not template.get('type') == 'menu':
        raise Exception('Invalid file! Root node must be type menu.')
    nodes.match_node(template)

if __name__ == '__main__':
    main()
