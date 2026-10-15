
# ==========================================
# CLINDONTO - SISTEMA DE CLINICA ODONTOLOGICA
# Projeto de Algoritmos
# Alunos(a):
# - João Vitor De Sousa Araujo
# - Graziele
# ==========================================

pacientes = []
administradores = []
dentistas = []
consultorios = []
consultas = []

especialidades = [
    'Ortodontia',
    'Implantodontia',
    'Endodontia',
    'Clinica Geral',
    'Dentistica',
    'Odontopediatria',
    'Protese Dentaria',
    'Estomatologia',
    'Harmonizacao Orofacial',
    'Bucomaxilo'
]


# ==========================================
# MENU PRINCIPAL
# ==========================================

while True:
    print('\n========== CLINDONTO ==========')
    print('1 - Cadastrar paciente')
    print('2 - Cadastrar secretaria')
    print('3 - Cadastrar odontologo')
    print('4 - Fazer login')
    print('5 - Sair')

    opcao = input('Escolha: ')

    # ======================================
    # CADASTRO DE PACIENTE
    # ======================================

    if opcao == '1':
        nome = input('Nome: ')
        usuario = input('Nome de usuario: ').lower()

        while True:
            cpf = input('CPF (11 digitos): ')

            if len(cpf) != 11 or not cpf.isdigit():
                print('CPF invalido!')
            else:
                break

        duplicado = False

        for i in range(len(pacientes)):
            if pacientes[i][2] == cpf:
                duplicado = True

        for i in range(len(administradores)):
            if administradores[i][3] == cpf:
                duplicado = True

        if duplicado:
            print('CPF ja cadastrado!')
            continue

        duplicado = False

        for i in range(len(pacientes)):
            if pacientes[i][1] == usuario:
                duplicado = True

        if duplicado:
            print('Nome de usuario ja cadastrado!')
            continue

        senha = input('Crie uma senha: ')
        telefone = input('Telefone: ')
        idade = input('Idade: ')

        pacientes.append([
            nome, usuario, cpf, senha,
            telefone, idade, ''
        ])

        print('Paciente cadastrado!')

    # ======================================
    # CADASTRO DE SECRETARIA
    # ======================================

    elif opcao == '2':
        nome = input('Nome da secretaria: ')
        usuario = input('Nome de usuario: ').lower()

        while True:
            cpf = input('CPF (11 digitos): ')

            if len(cpf) != 11 or not cpf.isdigit():
                print('CPF invalido!')
            else:
                break

        senha = input('Crie uma senha: ')

        while True:
            num_id = input('Numero de identificacao (5 digitos): ')

            if len(num_id) != 5 or not num_id.isdigit():
                print('Identificacao invalida!')
            else:
                break

        duplicado = False

        for i in range(len(administradores)):
            if (administradores[i][2] == usuario
                or administradores[i][3] == cpf
                or administradores[i][5] == num_id):
                duplicado = True

        if duplicado:
            print('Usuario, CPF ou identificacao ja cadastrado!')
        else:
            administradores.append([
                'secretaria', nome, usuario,
                cpf, senha, num_id
            ])
            print('Secretaria cadastrada!')

    # ======================================
    # CADASTRO DE ODONTOLOGO
    # ======================================

    elif opcao == '3':
        nome = input('Nome do odontologo: ')
        usuario = input('Nome de usuario: ').lower()

        while True:
            cpf = input('CPF (11 digitos): ')

            if len(cpf) != 11 or not cpf.isdigit():
                print('CPF invalido!')
            else:
                break

        senha = input('Crie uma senha: ')

        while True:
            cro = input('Numero do CRO: ')

            if not cro.isdigit() or len(cro) < 4 or len(cro) > 5:
                print('CRO invalido!')
            else:
                break

        print('\nEspecialidades:')

        for i in range(len(especialidades)):
            print(i + 1, '-', especialidades[i])

        escolha = int(input('Escolha a especialidade: '))

        if escolha < 1 or escolha > len(especialidades):
            print('Especialidade invalida!')
            continue

        especialidade = especialidades[escolha - 1]

        while True:
            num_id = input('Numero de identificacao (5 digitos): ')

            if len(num_id) != 5 or not num_id.isdigit():
                print('Identificacao invalida!')
            else:
                break

        duplicado = False

        for i in range(len(administradores)):
            if (administradores[i][2] == usuario
                or administradores[i][3] == cpf
                or administradores[i][5] == num_id):
                duplicado = True

        if duplicado:
            print('Usuario, CPF ou identificacao ja cadastrado!')
        else:
            dentistas.append([
                num_id, nome, cro, especialidade
            ])

            administradores.append([
                'dentista', nome, usuario,
                cpf, senha, num_id
            ])

            print('Odontologo cadastrado!')

    # ======================================
    # LOGIN
    # ======================================

    elif opcao == '4':
        print('\n1 - Paciente')
        print('2 - Administracao')

        tipo = input('Escolha: ')

        encontrou = False
        posicao = -1

        if tipo == '1':
            print('\n1 - Entrar com CPF')
            print('2 - Entrar com usuario')

            metodo = input('Escolha: ')

            if metodo == '1':
                identificador = input('CPF: ')
                pos = 2
            elif metodo == '2':
                identificador = input('Usuario: ').lower()
                pos = 1
            else:
                print('Opcao invalida!')
                continue

            senha = input('Senha: ')

            for i in range(len(pacientes)):
                if (pacientes[i][pos] == identificador
                    and pacientes[i][3] == senha):
                    encontrou = True
                    posicao = i
                    break

            if encontrou == False:
                print('CPF/usuario ou senha incorretos!')
                continue

            # ==================================
            # MENU DO PACIENTE
            # ==================================

            while True:
                print('\n===== MENU DO PACIENTE =====')
                print('1 - Ver corpo clinico')
                print('2 - Agendar consulta')
                print('3 - Minhas consultas')
                print('4 - Cancelar consulta')
                print('5 - Sair da conta')

                escolha = input('Escolha: ')

                if escolha == '1':
                    if len(dentistas) == 0:
                        print('Nenhum odontologo cadastrado.')
                    else:
                        for i in range(len(dentistas)):
                            print(
                                'ID:', dentistas[i][0],
                                '| Nome:', dentistas[i][1],
                                '| CRO:', dentistas[i][2],
                                '| Especialidade:', dentistas[i][3]
                            )

                elif escolha == '2':
                    if len(dentistas) == 0:
                        print('Nao existem odontologos cadastrados.')
                        continue

                    for i in range(len(dentistas)):
                        print(
                            dentistas[i][0],
                            '-', dentistas[i][1],
                            '-', dentistas[i][3]
                        )

                    id_dentista = input('ID do odontologo: ')
                    dentista_encontrado = False
                    nome_dentista = ''

                    for i in range(len(dentistas)):
                        if dentistas[i][0] == id_dentista:
                            dentista_encontrado = True
                            nome_dentista = dentistas[i][1]

                    if dentista_encontrado == False:
                        print('Odontologo nao encontrado!')
                        continue

                    data = input('Data (AAAA-MM-DD): ')
                    horario = input('Horario (HH:MM): ')

                    ocupado = False

                    for i in range(len(consultas)):
                        if (consultas[i][2] == id_dentista
                            and consultas[i][4] == data
                            and consultas[i][5] == horario):
                            ocupado = True

                    if ocupado:
                        print('Horario ocupado! Escolha outro.')
                    else:
                        consultas.append([
                            pacientes[posicao][2],
                            pacientes[posicao][0],
                            id_dentista,
                            nome_dentista,
                            data,
                            horario
                        ])
                        print('Consulta agendada!')

                elif escolha == '3':
                    encontrou_consulta = False

                    for i in range(len(consultas)):
                        if consultas[i][0] == pacientes[posicao][2]:
                            print(
                                'Dentista:', consultas[i][3],
                                '| Data:', consultas[i][4],
                                '| Horario:', consultas[i][5]
                            )
                            encontrou_consulta = True

                    if encontrou_consulta == False:
                        print('Voce nao possui consultas.')

                elif escolha == '4':
                    encontrou_consulta = False

                    for i in range(len(consultas)):
                        if consultas[i][0] == pacientes[posicao][2]:
                            print(
                                i, '- Dentista:', consultas[i][3],
                                '| Data:', consultas[i][4],
                                '| Horario:', consultas[i][5]
                            )
                            encontrou_consulta = True

                    if encontrou_consulta:
                        numero = int(input('Numero da consulta para cancelar: '))

                        if numero < 0 or numero >= len(consultas):
                            print('Numero invalido!')
                        elif consultas[numero][0] != pacientes[posicao][2]:
                            print('Essa consulta nao pertence a voce!')
                        else:
                            consultas.pop(numero)
                            print('Consulta cancelada!')
                    else:
                        print('Nenhuma consulta para cancelar.')

                elif escolha == '5':
                    break

                else:
                    print('Opcao invalida!')

        elif tipo == '2':
            print('\n1 - CPF')
            print('2 - Usuario')
            print('3 - Numero de identificacao')

            metodo = input('Como deseja entrar? ')

            if metodo == '1':
                identificador = input('CPF: ')
                pos = 3
            elif metodo == '2':
                identificador = input('Usuario: ').lower()
                pos = 2
            elif metodo == '3':
                identificador = input('Numero de identificacao: ')
                pos = 5
            else:
                print('Opcao invalida!')
                continue

            senha = input('Senha: ')

            for i in range(len(administradores)):
                if (administradores[i][pos] == identificador
                    and administradores[i][4] == senha):
                    encontrou = True
                    posicao = i
                    break

            if encontrou == False:
                print('Dados ou senha incorretos!')
                continue

            # ==================================
            # MENU ADMINISTRATIVO
            # ==================================

            while True:
                print('\n===== MENU ADMINISTRATIVO =====')
                print('1 - Cadastrar dentista')
                print('2 - Listar dentistas')
                print('3 - Buscar dentista')
                print('4 - Atualizar dentista')
                print('5 - Remover dentista')
                print('6 - Cadastrar consultorio')
                print('7 - Vincular dentista a consultorio')
                print('8 - Listar pacientes')
                print('9 - Buscar paciente')
                print('10 - Atualizar paciente')
                print('11 - Remover paciente')
                print('12 - Agenda geral')
                print('13 - Cancelar consulta')
                print('14 - Sair da conta')

                escolha = input('Escolha: ')

                # CADASTRAR DENTISTA
                if escolha == '1':
                    nome = input('Nome do dentista: ')
                    cro = input('CRO: ')

                    for i in range(len(especialidades)):
                        print(i + 1, '-', especialidades[i])

                    esp_num = int(input('Especialidade: '))

                    if esp_num < 1 or esp_num > len(especialidades):
                        print('Especialidade invalida!')
                        continue

                    id_dentista = str(len(dentistas) + 1)

                    dentistas.append([
                        id_dentista, nome, cro,
                        especialidades[esp_num - 1]
                    ])

                    print('Dentista cadastrado! ID:', id_dentista)

                # LISTAR DENTISTAS
                elif escolha == '2':
                    for i in range(len(dentistas)):
                        print(dentistas[i])

                    if len(dentistas) == 0:
                        print('Nenhum dentista cadastrado.')

                # BUSCAR DENTISTA
                elif escolha == '3':
                    busca = input('Digite o ID do dentista: ')
                    achou = False

                    for i in range(len(dentistas)):
                        if dentistas[i][0] == busca:
                            print(dentistas[i])
                            achou = True

                    if achou == False:
                        print('Dentista nao encontrado.')

                # ATUALIZAR DENTISTA
                elif escolha == '4':
                    busca = input('ID do dentista: ')
                    achou = False

                    for i in range(len(dentistas)):
                        if dentistas[i][0] == busca:
                            dentistas[i][1] = input('Novo nome: ')
                            dentistas[i][2] = input('Novo CRO: ')
                            print('Dentista atualizado!')
                            achou = True
                            break

                    if achou == False:
                        print('Dentista nao encontrado.')

                # REMOVER DENTISTA
                elif escolha == '5':
                    busca = input('ID do dentista: ')
                    achou = False

                    for i in range(len(dentistas)):
                        if dentistas[i][0] == busca:
                            dentistas.pop(i)
                            achou = True
                            break

                    if achou:
                        print('Dentista removido!')
                    else:
                        print('Dentista nao encontrado.')

                # CADASTRAR CONSULTORIO
                elif escolha == '6':
                    nome_sala = input('Nome do consultorio: ')
                    consultorios.append([nome_sala, ''])
                    print('Consultorio cadastrado!')

                # VINCULAR DENTISTA
                elif escolha == '7':
                    if len(consultorios) == 0 or len(dentistas) == 0:
                        print('Cadastre consultorios e dentistas primeiro.')
                        continue

                    for i in range(len(consultorios)):
                        print(i, '-', consultorios[i][0])

                    sala = int(input('Numero do consultorio: '))

                    if sala < 0 or sala >= len(consultorios):
                        print('Consultorio invalido!')
                        continue

                    for i in range(len(dentistas)):
                        print(dentistas[i][0], '-', dentistas[i][1])

                    id_dentista = input('ID do dentista: ')
                    achou = False

                    for i in range(len(dentistas)):
                        if dentistas[i][0] == id_dentista:
                            achou = True

                    if achou:
                        consultorios[sala][1] = id_dentista
                        print('Dentista vinculado!')
                    else:
                        print('Dentista nao encontrado.')

                # LISTAR PACIENTES
                elif escolha == '8':
                    for i in range(len(pacientes)):
                        print(
                            'Nome:', pacientes[i][0],
                            '| CPF:', pacientes[i][2],
                            '| Telefone:', pacientes[i][4],
                            '| Idade:', pacientes[i][5],
                            '| Observacoes:', pacientes[i][6]
                        )

                    if len(pacientes) == 0:
                        print('Nenhum paciente cadastrado.')

                # BUSCAR PACIENTE
                elif escolha == '9':
                    busca = input('Digite nome ou CPF: ').lower()
                    achou = False

                    for i in range(len(pacientes)):
                        if (pacientes[i][0].lower() == busca
                            or pacientes[i][2] == busca):
                            print(pacientes[i])
                            achou = True

                    if achou == False:
                        print('Paciente nao encontrado.')

                # ATUALIZAR PACIENTE
                elif escolha == '10':
                    busca = input('CPF do paciente: ')
                    achou = False

                    for i in range(len(pacientes)):
                        if pacientes[i][2] == busca:
                            pacientes[i][0] = input('Novo nome: ')
                            pacientes[i][4] = input('Novo telefone: ')
                            pacientes[i][5] = input('Nova idade: ')
                            pacientes[i][6] = input('Observacoes/alergias: ')
                            print('Paciente atualizado!')
                            achou = True
                            break

                    if achou == False:
                        print('Paciente nao encontrado.')

                # REMOVER PACIENTE
                elif escolha == '11':
                    busca = input('CPF do paciente: ')
                    achou = False

                    for i in range(len(pacientes)):
                        if pacientes[i][2] == busca:
                            pacientes.pop(i)
                            achou = True
                            break

                    if achou:
                        print('Paciente removido!')
                    else:
                        print('Paciente nao encontrado.')

                # AGENDA GERAL
                elif escolha == '12':
                    print('\n1 - Ver todas')
                    print('2 - Filtrar por dentista')
                    print('3 - Filtrar por data')

                    filtro = input('Escolha: ')

                    valor = ''

                    if filtro == '2':
                        valor = input('ID do dentista: ')
                    elif filtro == '3':
                        valor = input('Data (AAAA-MM-DD): ')

                    achou = False

                    for i in range(len(consultas)):
                        mostrar = False

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

                # CANCELAR CONSULTA
                elif escolha == '13':
                    for i in range(len(consultas)):
                        print(i, '-', consultas[i])

                    if len(consultas) > 0:
                        numero = int(input('Numero da consulta: '))

                        if numero >= 0 and numero < len(consultas):
                            consultas.pop(numero)
                            print('Consulta cancelada!')
                        else:
                            print('Numero invalido!')
                    else:
                        print('Nao existem consultas.')

                elif escolha == '14':
                    break

                else:
                    print('Opcao invalida!')

        else:
            print('Opcao invalida!')

    elif opcao == '5':
        print('Encerrando o ClinDONTO!')
        break

    else:
        print('Opcao invalida!')
