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
    u.print_msgs(text_obj.get('values'), wrap=True)
    u.wait_enter('pressione enter para retornar')
    u.clear()

# Handles the occurrence of Quizz nodes
def handle_quizz(quizz_obj: dict):
    # Quizz headers
    u.clear()
    u.show_node_title(quizz_obj.get('title'))
    ## Show all messages, if any
    if quizz_obj.get('msg'):
        u.print_msgs(quizz_obj.get('msg'))
    u.wait_enter('pressione enter para continuar')
    
    qlen = len(quizz_obj.get('questions'))
    score = 0
    for i, q in enumerate(quizz_obj.get('questions')):
        u.clear()
        print(f'# Questão ({i+1}/{qlen})\n')
        u.print_msgs(q.get('text'), wrap=True)
        print()
        u.print_msgs(q.get('answers'), wrap=True)
        
        quizz_exit = False
        while True:
            try:
                user_opt = input('> ').lower()
            except KeyboardInterrupt:
                exit()
            
            if user_opt == 'r':
                if u.get_confimation('- Quer mesmo parar o exercício?'):
                    quizz_exit = True 
                    break
            
            isright = False
            for i, ans in enumerate(q.get('answers')):
                if user_opt == ans[0]:
                    isright = i == q.get('correct_answer')
                    break
            else:
                print('- Opção inválida! Digite R para sair do exercício.')
                continue

            if isright:
                print(u.colorize(':g:- Parabéns! Você acertou!::'))
                score += 1
            else:
                print(u.colorize(':r:- Que pena! Você errou :(::'))
            u.wait_enter('pressione enter para continuar')
            break
        if quizz_exit: break
    
    u.clear()
    print('# Pontuação\n')
    print(u.colorize(f'- Você acertou acertou :g:{score}:: de :g:{qlen}:: questôes!'))    
    u.wait_enter('pressione enter para retornar')

# Handles the occurrence of Menu nodes
def handle_menu(menu_obj: dict):
    # Menu headers
    u.clear()
    u.show_node_title(menu_obj.get('title'))
    if menu_obj.get('msg'):
        u.print_msgs(menu_obj.get('msg'))
    print()
    u.show_menu_options(menu_obj.get('nodes'))
    
    # Input loop
    while True:
        # get user input
        try:
            user_opt = input('> ').lower()
        except:
            exit()
        
        if user_opt == 'r': # Return
            if not menu_obj.get('root'):
                break
            if u.get_confimation('- Deseja mesmo sair do programa?'):
                break
            else:
                continue
        if user_opt == 'm': # Show menu
            print('- Opções:')
            u.show_menu_options(menu_obj.get('nodes'))
            continue
        if not user_opt.isdecimal(): # Raise error if the option is negative
            print('- Opção inválida! Digite M para ver as opções ou R para retornar.')
            continue
        if int(user_opt) < 0:
            print('- Opção inválida! Digite M para ver as opções ou R para retornar.')
            continue
        
        # Get the child node chosen by the option
        node_chosen = menu_obj.get('nodes')[int(user_opt)]
        match_node(node_chosen)

        # Remostra o cabeçalho do menu ao retornar de outro node
        u.clear()
        u.show_node_title(menu_obj.get('title'))
        if menu_obj.get('msg'):
            u.print_msgs(menu_obj.get('msg'))
        print()
        u.show_menu_options(menu_obj.get('nodes'))
    

