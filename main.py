import sys
import utils as u
import nodes 

def main() -> None:
    file_name  = sys.argv[1]
    template = u.read_file(file_name)
    nodes.match_node(template.get('body'))

if __name__ == '__main__':
    main()
