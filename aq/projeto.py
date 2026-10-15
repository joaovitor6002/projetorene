odonto_dados= []
secretaria_dados= []
paciente_dados= []
usuario_odonto= []
usuario_secretaria= []
usuario_paciente= []
esp=['ortodontia','implandontia','endodontia','clinica geral','dentistica','odontopediatria','implandontia','protese dentaria','estomalogia','harmonizaçao orofacial','bucomaxilo']
tent=0

while True:
    print('\n----MENU---- \n 1- CADASTRAR \n 2- FAZER O LOGIN \n 3- VOLTAR AO MENU PRNCIPAL ')
    op=int(input('\n Digite sua opçao: '))

    if op==1:
        print('\n PRIMEIRA INFORMAÇAO PARA O SEU CADASTRO  \n 1- PACIENTE \n 2- ADMINISTRADOR')
        adm_paci=int(input('\nDigite a sua opçao: '))

        if adm_paci==1:
            nome=input('\nDigite seu nome: \n').lower()
            idade=int(input('Digite sua idade: \n'))
            user=input('Digite um nome de usuario: \n').lower()
            while True:
                cpf = input('Digite seu CPF: \n')
                if len(cpf)!=11:
                    print('o CPF inserido esta incorreto, tente novamente!')
                else:
                    break
            while True:
                senha = input('Digite sua senha: \nA senha deve ter no maximo 6 digitos.')
                if len(senha)!=6:
                    print('A senha inserido esta incorreta, tente novamente!')
                else:
                    break
            while True:
                telefone=input('Digite seu numero de telefone: \n')
                if len(telefone)!=11:
                    print('telefone inserido esta incorreto, tente novamente!')
                else:
                    break

            usuario_paciente.append(nome)
            usuario_paciente.append(user)
            usuario_paciente.append(cpf)
            usuario_paciente.append(senha)
            paciente_dados.append(telefone)
            paciente_dados.append(idade)
            paciente_dados.append(usuario_paciente)

            print(usuario_paciente)

            print('USUARIO DO PACIENTE CADASTRADO COM SUCESSO')

        if adm_paci==2:
            print('\nVOCE VAI SE CADASTRAR COMO: \n1-GESTAO OU SECRETARIA \n2-ODONTOLOGO(A)')
            op=int(input('Qual sua opçao: '))
            if op==1:
                nome = input('\nDigite seu nome completo: \n').lower()
                user = input('Digite um nome de usuario: \n').lower()
                while True:
                    cpf = input('Digite seu CPF: \n')
                    if len(cpf) != 11:
                        print('o CPF inserido esta incorreto, tente novamente!')
                    else:
                        break
                while True:
                    senha = input('Digite sua senha: \nA senha deve ter no maximo 6 digitos.')
                    if len(senha) != 6:
                        print('A senha inserido esta incorreta, tente novamente!')
                    else:
                        break
                while True:
                    telefone = input('Digite seu numero de telefone: \n')
                    if len(telefone) != 11:
                        print('telefone inserido esta incorreto, tente novamente!')
                    else:
                        break
                while True:
                    num_id = input('Digite seu numero de identificaçao: \n')
                    if len(num_id) != 5:
                        print('telefone inserido esta incorreto, tente novamente!')
                    else:
                        break

                usuario_secretaria.append(nome)
                usuario_secretaria.append(user)
                usuario_secretaria.append(cpf)
                usuario_secretaria.append(senha)
                usuario_secretaria.append(num_id)
                secretaria_dados.append(telefone)
                secretaria_dados.append(usuario_secretaria)

                print(usuario_secretaria)

                print('USUARIO DA GESTAO/SECRETARIA CADASTRADO COM SUCESSO')

            elif op==2:
                nome=input('\nDigite seu nome completo: \n')
                user=input('Crie um nome de usuario: \n')
                while True:
                    cro =int(input('Digite o numero do seu CRO: \n'))
                    if len(cro)!=4 or len(cro)!=5:
                        print('O CRO inserido e invalido. Tente novamente!')
                    else:
                        break
                while True:
                    cpf=input('Digite o numero do seu CPF: \n: ')
                    if len(cpf)!=11:
                        print('CPF inserido esta incorreto. Tente novamente!')
                    else:
                        break
                while True:
                    senha=input('Crie uma senha: \n')
                    if len(senha)!=6:
                        print('A senha inserida e invalida. Tente novamente!')
                    else:
                        break
                while True:
                    num_id=input('Digite seu numero de identificaçao: \n')
                    if len(num_id)!=5:
                        print('O numero de identificaçao esta incorreto. Tente novamente!')
                    else:
                        break
                esp=input('Digite sua especialidade: \n').lower()
                if esp not in esp:
                    print('A especializaçao inserida esta incorreta. Tente novamente!')
                else:
                    break
                
                usuario_odonto.append(nome)
                usuario_odonto.append(user)
                usuario_odonto.append(cpf)
                usuario_odonto.append(senha)
                odonto_dados.append(num_id)
                odonto_dados.append(cro)
                odonto_dados.append(esp)
                odonto_dados.append(usuario_odonto)
                
                print(usuario_odonto)
                
                print('O USUARIO DO(A) ODONTOLOGO(A) CADASTRADO COM SUCESSO')