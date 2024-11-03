import os

print('Bem vindo a lista de contatos ...')

lista_de_contatos = [{'id' : 321182, 'nome' : 'Alex', 'atividade' : 'Estudante', 'telefone' : 123456789}]

def limpador_de_tela():
    """
    Função responsável por limpar as informações na tela.
    """
    if os.name == 'nt':
        os.system('cls')
    
    else:
        os.system('clear')

def verificar_id_existente(id_contato):
    """
    Função responsável por verificar se o id de um contato já está em uso.
    """
    for contato in lista_de_contatos:
        if contato['id'] == id_contato:
            return True
    return False

def cadastrar_contato():
    """
    Função responsável por registrar um novo contato.
    """
    menu = 'MENU CADASTRAR CONTATO'

    if menu:
        print('-' * len(menu))
        print(menu)

    while True:
        try:
            id_contato = int(input('\nId do contato: '))

            # Verifica se o Id do contato já existe.
            if verificar_id_existente(id_contato):
                limpador_de_tela()
                print(f'O id {id_contato} já está cadastrado. Por favor, tente um id diferente.\n')
                continue

            nome_contato = input('Por favor entre com o nome do contato: ').capitalize()
            atividade_contato = input('Por favor entre com a atividade do contato: ').capitalize()
            telefone_contato = int(input('Por favor entre com o telefone do contato: '))

            novo_contato = {'id' : id_contato, 
                            'nome' : nome_contato, 
                            'atividade' : atividade_contato, 
                            'telefone' : telefone_contato}

            lista_de_contatos.append(novo_contato)

            continuar =input('\nDeseja cadastrar mais um contato (S/N)? ').upper()

            if continuar != 'S':
                limpador_de_tela()
                break

        except ValueError:
            limpador_de_tela()
            print('O valor digitado não corresponde a um valor númerico, por favor tente novamente.\n')

def consultar_contatos():
    """
    Função responsável por listar os contatos.
    """
    menu = 'MENU CONSULTAR CONTATOS'

    if menu:
        print('-' * len(menu))
        print(menu)

    while True:
        reposta = input('\n1. Consultar todos os contatos\n'
                        '2. Consultar contato por id\n'
                        '3. Consultar contato(s) por atividade\n'
                        '4. Retornar'
                        '>>')
        
        try:
            resposta_int = int(reposta)
            
            if resposta_int not in [1,2,3,4]:
                limpador_de_tela()
                print('Opção inválida, tente novamente.\n')
                continue

            if resposta_int == 1:
                limpador_de_tela()
                for contatos in lista_de_contatos:
                    print()

                    for chave, valor in contatos.items():
                        print(f'{chave}: {valor}')

            elif resposta_int == 2:
                limpador_de_tela()
                consulta_id = input('\nDigite o id do contato: ')

                consulta_id_int = int(consulta_id)

                # Verifica se o id existe em algum contato da lista.
                contato_encontrado = False

                for contatos in  lista_de_contatos:
                    if contatos['id'] == consulta_id_int:
                        contato_encontrado = True
                        print()

                        for chave, valor in contatos.items():
                            print(f'{chave}: {valor}')

                if not contato_encontrado:
                    print('\nNenhum contato encontrado com esse id.')
                
            elif resposta_int == 3:
                limpador_de_tela()
                consulta_atividade = input('\nDigite a atividade do(s) contato(s): ').capitalize()

                # Verifica se a atividade existe em algum contato da lista.
                contato_encontrado = False

                for contatos in lista_de_contatos:
                    if contatos['atividade'] == consulta_atividade:
                        contato_encontrado = True
                        print()

                        for chave, valor in contatos.items():
                            print(f'{chave}: {valor}')

                if not contato_encontrado:
                    print('\nNenhum contato encontrado com essa atividade.')

            else:
                limpador_de_tela()
                break


        except ValueError:
            limpador_de_tela()
            print('O valor digitado não corresponde a um valor númerico, por favor tente novamente.\n')

def remover_contato():
    """
    Função responsável por remover os contatos.
    """
    menu = 'MENU REMOVER CONTATOS'

    if menu:
        print('-' * len(menu))
        print(menu)

    while True:

        consulta_id = input('\nDigite o id do contato a ser removido: ')

        try:
            consulta_id_int = int(consulta_id)

            # Verifica se o id existe em algum contato da lista.
            id_encontrato = False

            for contatos in lista_de_contatos:
                if contatos['id'] == consulta_id_int:
                    id_encontrato = True

                    lista_de_contatos.remove(contatos)
                    print(f'\nO contato de id: {consulta_id_int}, foi removido com sucesso.')

            if not id_encontrato:
                print('\nNenhum contato encontrado com esse id.')

            continuar = input('\nDeseja remover mais algum contato (S/N)? ').upper()

            if continuar != 'S':
                limpador_de_tela()
                break

        except ValueError:
            limpador_de_tela()
            print('O valor digitado não corresponde a um valor númerico, por favor tente novamente.\n')

if __name__ == '__main__':
    while True:
        menu = 'MENU PRINCIPAL'

        if menu:
            print('-' * len(menu))
            print(menu)

        escolha_usuario = input('\nEscolha a opção desejada:\n'
                                '1. Cadastrar contato\n'
                                '2. Consultar contato(s)\n'
                                '3. Remover contato(s)\n'
                                '4. Sair'
                                '>>')
        
        try:
            escolha_usuario_int = int(escolha_usuario)

            if escolha_usuario_int not in [1,2,3,4]:
                limpador_de_tela()
                print('Opção inválida, tente novamente.\n')
                continue

            if escolha_usuario_int == 1:
                limpador_de_tela()
                cadastrar_contato()

            elif escolha_usuario_int == 2:
                limpador_de_tela()
                consultar_contatos()

            elif escolha_usuario_int == 3:
                limpador_de_tela()
                remover_contato()

            else:
                limpador_de_tela()
                break

        except ValueError:
            limpador_de_tela()
            print('O valor digitado não corresponde a um valor númerico, por favor tente novamente.\n')