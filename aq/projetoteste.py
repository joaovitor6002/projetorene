# com login agr, coloquei aq so pra salvar no git e eu saber klakakakak :) eu n mudei o codigo so adicionei a parte de login,
# tive q add uma variavel nova, 'categoria' para conferir o CPF ou usuário, e 
# a senha e o tipo de conta
odonto_dados = []
secretaria_dados = []
paciente_dados = []
usuario_odonto = []
usuario_secretaria = []
usuario_paciente = []
esp=['ortodontia','implandontia','endodontia','clinica geral','dentistica','odontopediatria','implandontia','protese dentaria','estomalogia','harmonizaçao orofacial','bucomaxilo']
tent=0

while True:
    print('\n----MENU---- \n 1- CADASTRAR \n 2- FAZER O LOGIN \n 3- VOLTAR AO MENU PRINCIPAL ')
    op = input('\nDigite sua opcao: ')

    if op == '1':
        print('\nPRIMEIRA INFORMACAO PARA O SEU CADASTRO \n1- PACIENTE \n2- ADMINISTRADOR')
        adm_paci = input('\nDigite sua opcao: ')

        if adm_paci == '1':
            nome = input('\nDigite seu nome: \n').lower()
            idade = input('Digite sua idade: \n')
            user = input('Digite um nome de usuario: \n').lower()
            while True:
                cpf = input('Digite seu CPF: \n')
                if len(cpf) != 11:
                    print('O CPF inserido esta incorreto, tente novamente!')
                else:
                    break
            while True:
                senha = input('Digite sua senha (6 caracteres): ')
                if len(senha) != 6:
                    print('A senha inserida esta incorreta, tente novamente!')
                else:
                    break
            while True:
                telefone = input('Digite seu numero de telefone: \n')
                if len(telefone) != 11:
                    print('Telefone inserido esta incorreto, tente novamente!')
                else:
                    break

            
            usuario_paciente.append(nome)
            usuario_paciente.append(user)
            usuario_paciente.append(cpf)
            usuario_paciente.append(senha)
            paciente_dados.append(telefone)
            paciente_dados.append(idade)

            print(usuario_paciente)

            print('USUARIO DO PACIENTE CADASTRADO COM SUCESSO')

        elif adm_paci == '2':
            print('\nVOCE VAI SE CADASTRAR COMO: \n1-GESTAO OU SECRETARIA \n2-ODONTOLOGO(A)')
            categoria = input('Qual sua opcao: ')
            if categoria == '1':
                nome = input('\nDigite seu nome completo: \n').lower()
                user = input('Digite um nome de usuario: \n').lower()
                while True:
                    cpf = input('Digite seu CPF: \n')
                    if len(cpf) != 11:
                        print('O CPF inserido esta incorreto, tente novamente!')
                    else:
                        break
                while True:
                    senha = input('Digite sua senha (6 caracteres): ')
                    if len(senha) != 6:
                        print('A senha inserida esta incorreta, tente novamente!')
                    else:
                        break
                while True:
                    telefone = input('Digite seu numero de telefone: \n')
                    if len(telefone) != 11:
                        print('Telefone inserido esta incorreto, tente novamente!')
                    else:
                        break
                while True:
                    num_id = input('Digite seu numero de identificacao: \n')
                    if len(num_id) != 5:
                        print('Numero de identificacao incorreto, tente novamente!')
                    else:
                        break

                
                usuario_secretaria.append(nome)
                usuario_secretaria.append(user)
                usuario_secretaria.append(cpf)
                usuario_secretaria.append(senha)
                usuario_secretaria.append(num_id)
                secretaria_dados.append(telefone)
                
                print(usuario_secretaria)

                print('USUARIO DA GESTAO/SECRETARIA CADASTRADO COM SUCESSO')

            elif categoria == '2':
                nome = input('\nDigite seu nome completo: \n')
                user = input('Crie um nome de usuario: \n').lower()
                while True:
                    cro = input('Digite o numero do seu CRO: \n')
                    if len(cro) < 4 or len(cro) > 5:
                        print('O CRO inserido e invalido. Tente novamente!')
                    else:
                        break
                while True:
                    cpf = input('Digite o numero do seu CPF: \n')
                    if len(cpf) != 11:
                        print('CPF inserido esta incorreto. Tente novamente!')
                    else:
                        break
                while True:
                    senha = input('Crie uma senha de 6 caracteres: \n')
                    if len(senha) != 6:
                        print('A senha inserida e invalida. Tente novamente!')
                    else:
                        break
                while True:
                    num_id = input('Digite seu numero de identificacao: \n')
                    if len(num_id) != 5:
                        print('O numero de identificacao esta incorreto. Tente novamente!')
                    else:
                        break

                print('\nEspecialidades:')
                for i in range(len(esp)):
                    print(i + 1, '-', esp[i])

                escolha_esp = input('Escolha o numero da sua especialidade: ')
                if escolha_esp not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
                    print('Especialidade invalida! Cadastro cancelado.')
                    continue

                especialidade = esp[int(escolha_esp) - 1]

                
                usuario_odonto.append(nome)
                usuario_odonto.append(user)
                usuario_odonto.append(cpf)
                usuario_odonto.append(senha)
                usuario_odonto.append(num_id)
                odonto_dados.append(num_id)
                odonto_dados.append(cro)
                odonto_dados.append(especialidade)

                print('O USUARIO DO(A) ODONTOLOGO(A) CADASTRADO COM SUCESSO')

            else:
                print('Opcao invalida!')

        else:
            print('Opcao invalida!')

    #aqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq o login
    elif op == '2':
        print('\n---- FAZER LOGIN ----')
        print('1 - PACIENTE')
        print('2 - SECRETARIA/GESTAO')
        print('3 - ODONTOLOGO(A)')
        tipo = input('Escolha seu tipo de usuario: ')

        if tipo == '1':
            print('\n1 - Entrar com CPF')
            print('2 - Entrar com nome de usuario')
            metodo = input('Escolha: ')

            if metodo == '1':
                identificador = input('Digite seu CPF: ')
                pos = 2
            elif metodo == '2':
                identificador = input('Digite seu usuario: ').lower()
                pos = 1
            else:
                print('Opcao invalida!')
                continue

            senha_login = input('Digite sua senha: ')
            encontrou = False

            # Cada paciente ocupa 4 posicoes: nome, usuario, CPF e senha.
            for i in range(0, len(usuario_paciente), 4):
                if usuario_paciente[i + pos] == identificador and usuario_paciente[i + 3] == senha_login:
                    encontrou = True
                    break

            if encontrou:
                print('Login do paciente realizado com sucesso!')
            else:
                print('CPF/usuario ou senha incorretos!')

        elif tipo == '2':
            print('\n1 - Entrar com CPF')
            print('2 - Entrar com nome de usuario')
            print('3 - Entrar com numero de identificacao')
            metodo = input('Escolha: ')

            if metodo == '1':
                identificador = input('Digite seu CPF: ')
                pos = 2
            elif metodo == '2':
                identificador = input('Digite seu usuario: ').lower()
                pos = 1
            elif metodo == '3':
                identificador = input('Digite seu numero de identificacao: ')
                pos = 4
            else:
                print('Opcao invalida!')
                continue

            senha_login = input('Digite sua senha: ')
            encontrou = False

            # Cada secretaria ocupa 5 posicoes na lista.
            for i in range(0, len(usuario_secretaria), 5):
                if usuario_secretaria[i + pos] == identificador and usuario_secretaria[i + 3] == senha_login:
                    encontrou = True
                    break

            if encontrou:
                print('Login da secretaria realizado com sucesso!')
            else:
                print('Dados ou senha incorretos!')

        elif tipo == '3':
            print('\n1 - Entrar com CPF')
            print('2 - Entrar com nome de usuario')
            print('3 - Entrar com numero de identificacao')
            metodo = input('Escolha: ')

            if metodo == '1':
                identificador = input('Digite seu CPF: ')
                pos = 2
            elif metodo == '2':
                identificador = input('Digite seu usuario: ').lower()
                pos = 1
            elif metodo == '3':
                identificador = input('Digite seu numero de identificacao: ')
                pos = 4
            else:
                print('Opcao invalida!')
                continue

            senha_login = input('Digite sua senha: ')
            encontrou = False

            # Cada odontologo ocupa 5 posicoes na lista.
            for i in range(0, len(usuario_odonto), 5):
                if usuario_odonto[i + pos] == identificador and usuario_odonto[i + 3] == senha_login:
                    encontrou = True
                    break

            if encontrou:
                print('Login do odontologo realizado com sucesso!')
            else:
                print('Dados ou senha incorretos!')

        else:
            print('Opcao invalida!')

    elif op == '3':
        print('Encerrando o sistema ClinDONTO...')
        break
    else:
        print('Opcao invalida!')