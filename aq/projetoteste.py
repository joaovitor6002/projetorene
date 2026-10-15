
odonto_dados = []
secretaria_dados = []
paciente_dados = []

usuario_odonto = []
usuario_secretaria = []
usuario_paciente = []

esp = [
    'ortodontia', 'implantodontia', 'endodontia',
    'clinica geral', 'dentistica', 'odontopediatria',
    'protese dentaria', 'estomatologia',
    'harmonizacao orofacial', 'bucomaxilo'
]

while True:
    print('\n---- MENU ----')
    print('1 - CADASTRAR')
    print('2 - FAZER O LOGIN')
    print('3 - SAIR')

    op = int(input('Digite sua opção: '))

    # CADASTRO
    if op == 1:
        print('\n1 - PACIENTE')
        print('2 - ADMINISTRADOR')

        adm_paci = int(input('Digite sua opção: '))

        # CADASTRO DO PACIENTE
        if adm_paci == 1:
            nome = input('Digite seu nome: ').lower()
            idade = int(input('Digite sua idade: '))
            user = input('Digite um nome de usuário: ').lower()

            while True:
                cpf = input('Digite seu CPF: ')

                if len(cpf) != 11 or not cpf.isdigit():
                    print('CPF incorreto! Digite novamente.')
                else:
                    break

            while True:
                senha = input('Crie sua senha (6 caracteres): ')

                if len(senha) != 6:
                    print('A senha deve ter 6 caracteres!')
                else:
                    break

            while True:
                telefone = input('Digite seu telefone: ')

                if len(telefone) != 11 or not telefone.isdigit():
                    print('Telefone incorreto! Digite novamente.')
                else:
                    break

            cadastro = [nome, user, cpf, senha]

            paciente_dados.append([telefone, idade, cadastro])
            usuario_paciente.append(cadastro)

            print('Paciente cadastrado com sucesso!')

        # CADASTRO ADMINISTRATIVO
        elif adm_paci == 2:
            print('\n1 - SECRETARIA/GESTÃO')
            print('2 - ODONTÓLOGO(A)')

            categoria = int(input('Digite sua opção: '))

            if categoria == 1:
                nome = input('Digite seu nome completo: ').lower()
                user = input('Digite um nome de usuário: ').lower()

                while True:
                    cpf = input('Digite seu CPF: ')

                    if len(cpf) != 11 or not cpf.isdigit():
                        print('CPF incorreto! Digite novamente.')
                    else:
                        break

                while True:
                    senha = input('Crie uma senha de 6 caracteres: ')

                    if len(senha) != 6:
                        print('A senha deve ter 6 caracteres!')
                    else:
                        break

                while True:
                    telefone = input('Digite seu telefone: ')

                    if len(telefone) != 11 or not telefone.isdigit():
                        print('Telefone incorreto! Digite novamente.')
                    else:
                        break

                while True:
                    num_id = input('Digite seu número de identificação: ')

                    if len(num_id) != 5 or not num_id.isdigit():
                        print('Identificação inválida! Digite novamente.')
                    else:
                        break

                cadastro = [nome, user, cpf, senha, num_id]

                secretaria_dados.append([telefone, cadastro])
                usuario_secretaria.append(cadastro)

                print('Secretaria cadastrada com sucesso!')

            elif categoria == 2:
                nome = input('Digite seu nome completo: ')
                user = input('Crie um nome de usuário: ').lower()

                while True:
                    cro = input('Digite o número do seu CRO: ')

                    if not cro.isdigit() or len(cro) < 4 or len(cro) > 5:
                        print('CRO inválido! Digite novamente.')
                    else:
                        break

                while True:
                    cpf = input('Digite seu CPF: ')

                    if len(cpf) != 11 or not cpf.isdigit():
                        print('CPF incorreto! Digite novamente.')
                    else:
                        break

                while True:
                    senha = input('Crie uma senha de 6 caracteres: ')

                    if len(senha) != 6:
                        print('Senha inválida! Digite novamente.')
                    else:
                        break

                while True:
                    num_id = input('Digite seu número de identificação: ')

                    if len(num_id) != 5 or not num_id.isdigit():
                        print('Identificação inválida! Digite novamente.')
                    else:
                        break

                print('\nEspecialidades disponíveis:')

                for i in range(len(esp)):
                    print(i + 1, '-', esp[i])

                escolha_esp = int(input('Escolha sua especialidade: '))

                if escolha_esp < 1 or escolha_esp > len(esp):
                    print('Especialidade inválida!')
                else:
                    especialidade = esp[escolha_esp - 1]

                    cadastro = [
                        nome, user, cpf, senha,
                        num_id, cro, especialidade
                    ]

                    odonto_dados.append(cadastro)
                    usuario_odonto.append(cadastro)

                    print('Odontólogo cadastrado com sucesso!')

            else:
                print('Opção inválida!')

        else:
            print('Opção inválida!')

    # LOGIN
    elif op == 2:
        print('\n---- LOGIN ----')
        print('1 - PACIENTE')
        print('2 - ADMINISTRADOR')

        tipo = int(input('Escolha seu tipo de usuário: '))

        if tipo == 1:
            print('\n1 - CPF')
            print('2 - Nome de usuário')

            escolha = int(input('Como deseja entrar? '))

            if escolha == 1:
                identificador = input('Digite seu CPF: ')
                pos = 2
            elif escolha == 2:
                identificador = input('Digite seu usuário: ').lower()
                pos = 1
            else:
                print('Opção inválida!')
                continue

            senha_login = input('Digite sua senha: ')
            encontrou = False

            for i in range(len(usuario_paciente)):
                if (usuario_paciente[i][pos] == identificador
                    and usuario_paciente[i][3] == senha_login):
                    encontrou = True
                    break

            if encontrou:
                print('Login do paciente realizado com sucesso!')
            else:
                print('CPF/usuário ou senha incorretos!')

        elif tipo == 2:
            print('\n1 - SECRETARIA/GESTÃO')
            print('2 - ODONTÓLOGO(A)')

            categoria = int(input('Escolha sua categoria: '))

            if categoria == 1:
                print('\n1 - CPF')
                print('2 - Nome de usuário')
                print('3 - Número de identificação')

                escolha = int(input('Como deseja entrar? '))

                if escolha == 1:
                    pos = 2
                elif escolha == 2:
                    pos = 1
                elif escolha == 3:
                    pos = 4
                else:
                    print('Opção inválida!')
                    continue

                identificador = input('Digite seu identificador: ')
                if escolha == 2:
                    identificador = identificador.lower()

                senha_login = input('Digite sua senha: ')
                encontrou = False

                for i in range(len(usuario_secretaria)):
                    if (usuario_secretaria[i][pos] == identificador
                        and usuario_secretaria[i][3] == senha_login):
                        encontrou = True
                        break

                if encontrou:
                    print('Login da secretaria realizado com sucesso!')
                else:
                    print('Dados ou senha incorretos!')

            elif categoria == 2:
                print('\n1 - CPF')
                print('2 - Nome de usuário')
                print('3 - Número de identificação')

                escolha = int(input('Como deseja entrar? '))

                if escolha == 1:
                    pos = 2
                elif escolha == 2:
                    pos = 1
                elif escolha == 3:
                    pos = 4
                else:
                    print('Opção inválida!')
                    continue

                identificador = input('Digite seu identificador: ')
                if escolha == 2:
                    identificador = identificador.lower()

                senha_login = input('Digite sua senha: ')
                encontrou = False

                for i in range(len(usuario_odonto)):
                    if (usuario_odonto[i][pos] == identificador
                        and usuario_odonto[i][3] == senha_login):
                        encontrou = True
                        break

                if encontrou:
                    print('Login do odontólogo realizado com sucesso!')
                else:
                    print('Dados ou senha incorretos!')

            else:
                print('Opção inválida!')

        else:
            print('Opção inválida!')

    elif op == 3:
        print('Encerrando o sistema ClinDONTO...')
        break

    else:
        print('Opção inválida!')
