
odonto = []
paciente = []
usuario_odonto = []
usuario_paciente = []

while True:
    print('----MENU---- \n 1- CADASTRAR \n 2- FAZER O LOGIN \n 3- VOLTAR AO MENU PRINCIPAL')
    cad = int(input('Qual a sua opção? '))

    if cad == 1:
        print('\n PRIMEIRA INFORMAÇÃO PARA O SEU CADASTRO \n 1- ADMINISTRADOR \n 2- PACIENTE')
        adm_paci = int(input('Digite a sua opção: '))

        if adm_paci == 1:
            nome = input('Digite seu nome: ')
#eu meio q descobri oq era pra ser feito, tem q criar outro while true
            while True:
                cpf = input('Digite seu CPF: ')    #aq continua a msm pergunta

                if len(cpf) != 11:  #mas aq inves de len, ele vai ler oq foi digitado no campo do cpf e comparar se é 11, se for indiferente vai para o print e repete, caso n ele da break e passa a seguinte, mas n sei fazer caso alguem digite letra 
                    print('CPF incorreto! Digite novamente.')
                else:
                    break

            senha = input('Digite sua senha: ')
            numero = input('Digite seu telefone: ')

            usuario_odonto.append(nome)
            odonto.append(cpf)
            odonto.append(senha)
            odonto.append(numero)

            print('Cadastro realizado!')

        elif adm_paci == 2:
            nome = input('Digite seu nome: ')

            while True:
                cpf = input('Digite seu CPF: ') #msm coisa aq, p os 2 1-adm e 2-pac

                if len(cpf) != 11:
                    print('CPF incorreto! Digite novamente.')
                else:
                    break

            senha = input('Digite sua senha: ')
            numero = input('Digite seu telefone: ')

            usuario_paciente.append(nome)
            paciente.append(cpf)
            paciente.append(senha)
            paciente.append(numero)

            print('Cadastro realizado!')

        else:
            print('Opção inválida!')

    