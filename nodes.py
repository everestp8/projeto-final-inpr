import utils as u

# Handles the type of a node and passes it on to its proper function
def match_node(unmatched_node: dict) -> int:
    match unmatched_node.get('type'):
        case 'menu':
            handle_menu(unmatched_node)
        case 'text':
            handle_text(unmatched_node)
        case 'quizz':
            handle_quizz(unmatched_node)
        case _:
            return -1

# Handles the occurrence of Text nodes
def handle_text(text_obj: dict):
    u.clear()
    u.show_node_title(text_obj.get('title'))
    u.print_msgs(text_obj.get('values'))
    while True:
        try:
            user_opt = input('> ').lower()
            if user_opt == 'r':
                break 
            else: 
                print('Opção inválida! Digite R para retornar ao menu.')
        except KeyboardInterrupt:
            break

# Handles the occurrence of Quizz nodes
def handle_quizz(quizz_obj: dict):
    # Menu headers
    u.clear()
    u.show_node_title(quizz_obj.get('title'))
    ## Show all messages, if any
    if quizz_obj.get('msg'):
        u.print_msgs(quizz_obj.get('msg'))
    ## Show options automatcally, if required
    if quizz_obj.get('show_opts'):
        u.show_menu_options(quizz_obj.get('nodes'))

# Handles the occurrence of Menu nodes
def handle_menu(menu_obj: dict):
    # Menu headers
    u.clear()
    u.show_node_title(menu_obj.get('title'))
    ## Show all messages, if any
    if menu_obj.get('msg'):
        u.print_msgs(menu_obj.get('msg'))
    print()
    ## Show options automatcally
    u.show_menu_options(menu_obj.get('nodes'))
    
    # Input loop
    while True:
        try:
            # get user input
            user_opt = input('> ').lower()
            if user_opt == 'q' and menu_obj.get('exit_with_q'): # Quit
                break 
            if user_opt == 'r' and not menu_obj.get('exit_with_q'): # Return
                break 
            if user_opt == 'm': # Show menu
                print('Opções:')
                u.show_menu_options(menu_obj.get('nodes'))
                continue
            if int(user_opt) < 0: # Raise error if the option is negative
                raise ValueError
            
            # Get the child node chosen by the option
            node_chosen = menu_obj.get('nodes')[int(user_opt)]
            match_node(node_chosen)

            # Handles return from other nodes
            u.clear()
            u.show_node_title(menu_obj.get('title'))
            if menu_obj.get('msg'):
                u.print_msgs(menu_obj.get('msg'))
            print()
            u.show_menu_options(menu_obj.get('nodes'))
        except (IndexError, ValueError) as _:
            print('Opção inválida! Digite M para abrir o menu de opções', end='')
            if not menu_obj.get('exit_with_q'):
                print(' ou R para retornar.')
            else:
                print(' ou Q para sair.')
        except KeyboardInterrupt:
            break

