list_vacinacao = []

def cadastrar():
    print('-----------------------------------------')
    print("~ Agendamento Vacina COVID-19 ~")
    dados = []
    dados.append(input("Nome completo: "))
    dados.append(input("RG: "))
    dados.append(input("CPF: ")) 
    dados.append(input("Data de nascimento: "))
    dados.append(input("Telefone para contato: "))
    list_vacinacao.append(dados)
    print(">> Cadastro realizado com sucesso! Ligaremos para informar data e local.")
    print('-----------------------------------------')
    
def listar(): 
    for dados in list_vacinacao:
        print('\nOs dados cadastrados são:')
        print(">Nome:" ,dados[0], "-RG:" ,dados[1], "-CPF:" ,dados[2], "-Nascimento:" ,dados[3], "-Telefone:" ,dados[4])
        print('-----------------------------------------')
    
def alterar():
    print('\n-----------------------------------------')
    nome = input("Informe o CPF de cadastro para a alteracao: ")
    for dados in list_vacinacao:
        if nome == dados[2]:
            dados[0] = input("Novo nome: ")
            dados[1] = input("Novo RG: ")
            dados[2] = input("Novo CPF: ")
            dados[3] = input("Nova Data de Nascimento: ")
            dados[4] = input("Novo número de telefone: ")

def deletar():
    print('\n-----------------------------------------')
    cpf = input("Digite o CPF de cadastro: ")
    for i in range(len(list_vacinacao)):
        if cpf == list_vacinacao[i][2]:
            del(list_vacinacao[i])
            print(">> Cadastro de vacinção deletado!")
            break 

def funcao_menu(op): 
    if op == 1: 
        cadastrar()
    elif op == 2: 
        listar()
    elif op == 3: 
        alterar()
    elif op == 4: 
        deletar()

def opcoes():
    op = 1
    while op != 0:
        print("\n[1] Cadastro de Vacinação")
        print("[2] Listar dados")
        print("[3] Alterar dados")
        print("[4] Deletar dados")
        print("\nO que você deseja?")
        op = int(input(">> "))
        funcao_menu(op)

print('~ Campanha de Vacinação Cloroquina - CVC ~')
opcoes()