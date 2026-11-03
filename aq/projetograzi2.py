# dados q vc pediu pra por, pra n precisar cadastrar sempre
# secretaria = Joao Vitor', joaovitor, 66666666666, 123456, 10001, 83999990001
# secretaria = Graziela, graziela, 77777777777, 123456, 10002, 83999990002
# usuario = Joao Vitor, joaovitor, 66666666666, 123456, 10001
# usuario = Graziela, graziela, 77777777777, 123456, 10002


odonto_dados = []
secretaria_dados = []
paciente_dados = []
usuario_odonto = []
usuario_secretaria = []
usuario_paciente = []
consultorios = []
consultas = []

esp = ['ortodontia', 'implantodontia', 'endodontia', 'clinica geral',
       'dentistica', 'odontopediatria', 'protese dentaria',
       'estomatologia', 'harmonizacao orofacial', 'bucomaxilo']

# dados para testar o sistema
# as consultas e os cadastros ficam guardados nessas listas
odonto_dados.append(['1', 'Ana Lima', '12345', 'ortodontia', True])
odonto_dados.append(['2', 'Bruno Alves', '23456', 'implantodontia', True])
odonto_dados.append(['3', 'Carla Souza', '34567', 'endodontia', True])
odonto_dados.append(['4', 'Diego Rocha', '45678', 'clinica geral', True])
odonto_dados.append(['5', 'Eva Santos', '56789', 'odontopediatria', True])

usuario_odonto.append(['Ana Lima', 'ana', '11111111111', '123456', '1', True])
usuario_odonto.append(['Bruno Alves', 'bruno', '22222222222', '123456', '2', True])
usuario_odonto.append(['Carla Souza', 'carla', '33333333333', '123456', '3', True])
usuario_odonto.append(['Diego Rocha', 'diego', '44444444444', '123456', '4', True])
usuario_odonto.append(['Eva Santos', 'eva', '55555555555', '123456', '5', True])

secretaria_dados.append(['Joao Vitor', 'joaovitor', '66666666666', '123456', '10001', '83999990001', True])
secretaria_dados.append(['Graziela', 'graziela', '77777777777', '123456', '10002', '83999990002', True])
usuario_secretaria.append(['Joao Vitor', 'joaovitor', '66666666666', '123456', '10001', True])
usuario_secretaria.append(['Graziela', 'graziela', '77777777777', '123456', '10002', True])

paciente_dados.append(['Joao Adulto', 'joao', '88888888888', '123456', '83988880001', '25', '', True])
paciente_dados.append(['Lia Crianca', 'lia', '99999999999', '123456', '83988880002', '8', '', True])
usuario_paciente.append(paciente_dados[0])
usuario_paciente.append(paciente_dados[1])

# menu principal
while True:
    print('\n---- CLINDONTO ----')
    print('1 - CADASTRAR')
    print('2 - FAZER LOGIN')
    print('3 - SAIR')
    op = input('Digite sua opcao: ')

    if op == '1':
        print('\n1 - PACIENTE')
        print('2 - ADMINISTRADOR')
        adm_paci = input('Digite sua opcao: ')

        if adm_paci == '1':
            nome = input('Digite seu nome: ').lower()
            idade = input('Digite sua idade: ')
            user = input('Digite seu nome de usuario: ').lower()

            while True:
                cpf = input('Digite seu CPF (11 numeros): ')
                if len(cpf) != 11:
                    print('CPF incorreto!')
                else:
                    break

            senha = input('Crie uma senha de 6 caracteres: ')
            while len(senha) != 6:
                print('A senha deve ter 6 caracteres!')
                senha = input('Crie uma senha: ')

            telefone = input('Digite seu telefone: ')
            cadastro = [nome, user, cpf, senha, telefone, idade, '', True]
            paciente_dados.append(cadastro)
            usuario_paciente.append(cadastro)
            print('Paciente cadastrado com sucesso!')

        elif adm_paci == '2':
            print('\n1 - GESTAO/SECRETARIA')
            print('2 - ODONTOLOGO')
            categoria = input('Escolha: ')

            if categoria == '1':
                nome = input('Nome: ').lower()
                user = input('Usuario: ').lower()
                cpf = input('CPF (11 numeros): ')
                senha = input('Senha (6 caracteres): ')
                num_id = input('Numero de identificacao: ')
                telefone = input('Telefone: ')
                cadastro = [nome, user, cpf, senha, num_id, telefone, True]
                secretaria_dados.append(cadastro)
                usuario_secretaria.append(cadastro)
                print('Secretaria cadastrada!')

            elif categoria == '2':
                nome = input('Nome: ')
                user = input('Usuario: ').lower()
                cpf = input('CPF: ')
                senha = input('Senha (6 caracteres): ')
                num_id = input('Numero de identificacao: ')
                cro = input('CRO: ')
                print('\nEspecialidades:')
                for i in range(len(esp)):
                    print(i + 1, '-', esp[i])
                escolha = input('Escolha a especialidade: ')

                if escolha and int(escolha) >= 1 and int(escolha) <= len(esp):
                    especialidade = esp[int(escolha) - 1]
                    odonto_dados.append([num_id, nome, cro, especialidade, True])
                    usuario_odonto.append([nome, user, cpf, senha, num_id, True])
                    print('Odontologo cadastrado!')
                else:
                    print('Especialidade invalida!')

            else:
                print('Opcao invalida!')
        else:
            print('Opcao invalida!')

    elif op == '2':
        print('\n1 - PACIENTE')
        print('2 - GESTAO/SECRETARIA')
        print('3 - ODONTOLOGO')
        tipo = input('Tipo de usuario: ')

        # login e painel do paciente
        if tipo == '1':
            identificador = input('CPF ou usuario: ').lower()
            senha = input('Senha: ')
            pos = -1
            for i in range(len(usuario_paciente)):
                if (usuario_paciente[i][2] == identificador or usuario_paciente[i][1] == identificador) and usuario_paciente[i][3] == senha and usuario_paciente[i][7] == True:
                    pos = i
                    break

            if pos == -1:
                print('Dados incorretos!')
                continue

            print('Bem-vindo(a),', usuario_paciente[pos][0])
            while True:
                print('\n---- PAINEL DO PACIENTE ----')
                print('1 - Agendar consulta')
                print('2 - Minhas consultas')
                print('3 - Cancelar consulta')
                print('4 - Remarcar consulta')
                print('5 - Ver corpo clinico')
                print('6 - Sair da conta')
                escolha = input('Escolha: ')

                if escolha == '1':
                    print('\nEspecialidades:')
                    for i in range(len(esp)):
                        print(i + 1, '-', esp[i])
                    num_esp = input('Escolha a especialidade: ')

                    if not num_esp or int(num_esp) < 1 or int(num_esp) > len(esp):
                        print('Especialidade invalida!')
                        continue
                    especialidade = esp[int(num_esp) - 1]

                    if especialidade == 'odontopediatria': 
                        if int(usuario_paciente[pos][5]) > 12:
                            print('Odontopediatria atende somente pacientes ate 12 anos.')
                            continue

                    achou = False
                    for i in range(len(odonto_dados)):
                        if odonto_dados[i][3] == especialidade and odonto_dados[i][4] == True:
                            print(odonto_dados[i][0], '-', odonto_dados[i][1], '-', odonto_dados[i][3])
                            achou = True
                    if achou == False:
                        print('Nao tem dentista ativo nessa especialidade.')
                        continue

                    id_dentista = input('ID do dentista: ')
                    nome_dentista = ''
                    dentista_ativo = False
                    for i in range(len(odonto_dados)):
                        if odonto_dados[i][0] == id_dentista and odonto_dados[i][3] == especialidade and odonto_dados[i][4] == True:
                            nome_dentista = odonto_dados[i][1]
                            dentista_ativo = True

                    if dentista_ativo == False:
                        print('Dentista nao encontrado nessa especialidade!')
                        continue

                    data = input('Dia da consulta (DD/MM/AAAA): ')
                    horario = input('Horario (HH:MM): ')
                    ocupado = False
                    for i in range(len(consultas)):
                        if consultas[i][2] == id_dentista and consultas[i][4] == data and consultas[i][5] == horario and consultas[i][6] == True:
                            ocupado = True

                    if ocupado:
                        print('Esse dentista ja tem consulta nesse dia e horario!')
                    else:
                        consultas.append([usuario_paciente[pos][2], usuario_paciente[pos][0], id_dentista, nome_dentista, data, horario, True])
                        print('Consulta agendada!')

                elif escolha == '2':
                    achou = False
                    for i in range(len(consultas)):
                        if consultas[i][0] == usuario_paciente[pos][2] and consultas[i][6] == True:
                            print(i, '-', consultas[i][3], '|', consultas[i][4], '|', consultas[i][5])
                            achou = True
                    if achou == False:
                        print('Voce nao tem consultas marcadas.')

                elif escolha == '3' or escolha == '4':
                    achou = False
                    for i in range(len(consultas)):
                        if consultas[i][0] == usuario_paciente[pos][2] and consultas[i][6] == True:
                            print(i, '-', consultas[i][3], '|', consultas[i][4], '|', consultas[i][5])
                            achou = True
                    if achou == False:
                        print('Voce nao tem consultas marcadas.')
                        continue

                    numero = input('Numero da consulta: ')
                    if not numero or int(numero) < 0 or int(numero) >= len(consultas):
                        print('Numero invalido!')
                        continue
                    numero = int(numero)

                    if consultas[numero][0] != usuario_paciente[pos][2] or consultas[numero][6] == False:
                        print('Essa consulta nao esta disponivel para voce!')
                        continue

                    if escolha == '3':
                        consultas[numero][6] = False
                        print('Consulta cancelada!')
                    else:
                        data = input('Nova data (DD/MM/AAAA): ')
                        horario = input('Novo horario (HH:MM): ')
                        ocupado = False
                        for i in range(len(consultas)):
                            if i != numero and consultas[i][2] == consultas[numero][2] and consultas[i][4] == data and consultas[i][5] == horario and consultas[i][6] == True:
                                ocupado = True
                        if ocupado:
                            print('Horario ocupado! A consulta antiga continua marcada.')
                        else:
                            consultas[numero][6] = False
                            consultas.append([usuario_paciente[pos][2], usuario_paciente[pos][0], consultas[numero][2], consultas[numero][3], data, horario, True])
                            print('Consulta remarcada!')
                elif escolha== '5':
                    achou= False

                    for i in range(len(odonto_dados)):
                        if odonto_dados[i][4] == True:
                            print(odonto_dados[i][4], '-', odonto_dados[i][3])
                            achou= True
                            
                    if achou == False:
                        print('Nenhum dentista disponivel')

                elif escolha == '6':
                    break
                else:
                    print('Opcao invalida!')

        # painel da gestao e da secretaria
        elif tipo == '2':
            identificador = input('CPF, usuario ou identificacao: ').lower()
            senha = input('Senha: ')
            pos = -1
            for i in range(len(usuario_secretaria)):
                if (usuario_secretaria[i][2] == identificador or usuario_secretaria[i][1] == identificador or usuario_secretaria[i][4] == identificador) and usuario_secretaria[i][3] == senha and usuario_secretaria[i][5] == True:
                    pos = i
                    break
            if pos == -1:
                print('Dados incorretos!')
                continue

            while True:
                print('\n---- PAINEL DA GESTAO ----')
                print('1 - Cadastrar dentista')
                print('2 - Listar dentistas')
                print('3 - Atualizar dentista')
                print('4 - Remover dentista')
                print('5 - Cadastrar sala')
                print('6 - Vincular dentista a sala')
                print('7 - Listar pacientes')
                print('8 - Buscar paciente')
                print('9 - Atualizar paciente/observaçoes')
                print('10 - Agenda geral')
                print('11 - Cancelar consulta')
                print('12 - Sair')
                escolha = input('Escolha: ')

                if escolha == '1':
                    nome = input('Nome: ')
                    cro = input('CRO: ')
                    for i in range(len(esp)):
                        print(i + 1, '-', esp[i])
                    num = input('Especialidade: ')
                    if num and int(num) >= 1 and int(num) <= len(esp):
                        id_dentista = str(len(odonto_dados) + 1)
                        especialidade = esp[int(num) - 1]
                        user = input('Nome de usuario do dentista: ').lower()
                        cpf = input('CPF do dentista: ')
                        senha = input('Senha do dentista: ')
                        odonto_dados.append([id_dentista, nome, cro, especialidade, True])
                        usuario_odonto.append([nome, user, cpf, senha, id_dentista, True])
                        print('Dentista cadastrado com ID', id_dentista)
                    else:
                        print('Especialidade invalida!')

                elif escolha == '2':
                    for i in range(len(odonto_dados)):
                        if odonto_dados[i][4] == True:
                            print(odonto_dados[i][0], odonto_dados[i][1], odonto_dados[i][2], odonto_dados[i][3])
                    print('Fim da lista.')

                elif escolha == '3' or escolha == '4':
                    id_dentista = input('ID do dentista: ')
                    achou = False
                    for i in range(len(odonto_dados)):
                        if odonto_dados[i][0] == id_dentista and odonto_dados[i][4] == True:
                            achou = True
                            if escolha == '3':
                                odonto_dados[i][1] = input('Novo nome: ')
                                odonto_dados[i][2] = input('Novo CRO: ')
                                for j in range(len(usuario_odonto)):
                                    if usuario_odonto[j][4] == id_dentista:
                                        usuario_odonto[j][0] = odonto_dados[i][1]
                                for j in range(len(esp)):
                                    print(j + 1, '-', esp[j])
                                num = input('Nova especialidade: ')
                                if num and int(num) >= 1 and int(num) <= len(esp):
                                    odonto_dados[i][3] = esp[int(num) - 1]
                                    print('Dentista atualizado!')
                                else:
                                    print('Especialidade invalida. Nome e CRO foram atualizados.')
                            else:
                                odonto_dados[i][4] = False
                                for j in range(len(usuario_odonto)):
                                    if usuario_odonto[j][4] == id_dentista:
                                        usuario_odonto[j][5] = False
                                print('Dentista removido da lista de ativos!')
                            break
                    if achou == False:
                        print('Dentista nao encontrado.')

                elif escolha == '5':
                    nome_sala = input('Nome da sala: ')
                    consultorios.append([nome_sala, '', True])
                    print('Sala cadastrada!')

                elif escolha == '6':
                    if len(consultorios) == 0:
                        print('Cadastre uma sala primeiro.')
                        continue
                    for i in range(len(consultorios)):
                        if consultorios[i][2] == True:
                            print(i, '-', consultorios[i][0])
                    sala = input('Numero da sala: ')
                    if not sala or int(sala) < 0 or int(sala) >= len(consultorios):
                        print('Sala invalida!')
                        continue
                    id_dentista = input('ID do dentista: ')
                    achou = False
                    for i in range(len(odonto_dados)):
                        if odonto_dados[i][0] == id_dentista and odonto_dados[i][4] == True:
                            achou = True
                    if achou:
                        consultorios[int(sala)][1] = id_dentista
                        print('Dentista vinculado a sala!')
                    else:
                        print('Dentista nao encontrado!')

                elif escolha == '7':
                    for i in range(len(paciente_dados)):
                        if paciente_dados[i][7] == True:
                            print(paciente_dados[i][0], '| CPF:', paciente_dados[i][2], '| Telefone:', paciente_dados[i][4], '| Idade:', paciente_dados[i][5], '| Obs:', paciente_dados[i][6])

                elif escolha == '8':
                    busca = input('Nome ou CPF: ').lower()
                    achou = False
                    for i in range(len(paciente_dados)):
                        if paciente_dados[i][0].lower() == busca or paciente_dados[i][2] == busca:
                            print(paciente_dados[i])
                            achou = True
                    if achou == False:
                        print('Paciente nao encontrado.')

                elif escolha == '9':
                    busca = input('CPF do paciente: ')
                    achou = False
                    for i in range(len(paciente_dados)):
                        if paciente_dados[i][2] == busca and paciente_dados[i][7] == True:
                            paciente_dados[i][0] = input('Novo nome: ')
                            paciente_dados[i][4] = input('Novo telefone: ')
                            paciente_dados[i][5] = input('Nova idade: ')
                            paciente_dados[i][6] = input('Observacoes/alergias: ')
                            print('Paciente atualizado!')
                            achou = True
                            break
                    if achou == False:
                        print('Paciente nao encontrado.')

                elif escolha == '10':
                    print('\n1 - Ver todas')
                    print('2 - Filtrar por dentista')
                    print('3 - Filtrar por data')
                    filtro = input('Escolha: ')
                    valor = ''
                    if filtro == '2':
                        valor = input('ID do dentista: ')
                    elif filtro == '3':
                        valor = input('Data (DD/MM/AAAA): ')
                    achou = False
                    for i in range(len(consultas)):
                        mostrar = False
                        if consultas[i][6] == True:
                            if filtro == '1':
                                mostrar = True
                            elif filtro == '2' and consultas[i][2] == valor:
                                mostrar = True
                            elif filtro == '3' and consultas[i][4] == valor:
                                mostrar = True
                        if mostrar:
                            print(consultas[i])
                            achou = True
                    if achou == False:
                        print('Nenhuma consulta encontrada.')

                elif escolha == '11':
                    for i in range(len(consultas)):
                        if consultas[i][6] == True:
                            print(i, '-', consultas[i])
                    numero = input('Numero da consulta: ')
                    if numero and int(numero) >= 0 and int(numero) < len(consultas) and consultas[int(numero)][6] == True:
                        consultas[int(numero)][6] = False
                        print('Consulta cancelada!')
                    else:
                        print('Consulta invalida!')

                elif escolha == '12':
                    break
                else:
                    print('Opcao invalida!')

        # tela do dentista com as consultas dele
        elif tipo == '3':
            identificador = input('CPF, usuario ou identificacao: ').lower()
            senha = input('Senha: ')
            pos = -1
            for i in range(len(usuario_odonto)):
                if (usuario_odonto[i][2] == identificador or usuario_odonto[i][1] == identificador or usuario_odonto[i][4] == identificador) and usuario_odonto[i][3] == senha and usuario_odonto[i][5] == True:
                    pos = i
                    break
            if pos == -1:
                print('Dados incorretos!')
                continue

            id_dentista = usuario_odonto[pos][4]
            print('Bem-vindo(a),', usuario_odonto[pos][0])
            print('\n---- CONSULTAS DO DENTISTA ----')
            achou = False
            for i in range(len(consultas)):
                if consultas[i][2] == id_dentista and consultas[i][6] == True:
                    print('Paciente:', consultas[i][1], '| Data:', consultas[i][4], '| Horario:', consultas[i][5])
                    achou = True
            if achou == False:
                print('Voce nao tem consultas marcadas.')

        else:
            print('Opcao invalida!')

    elif op == '3':
        print('Encerrando o sistema ClinDONTO...')
        break
    else:
        print('Opcao invalida!')