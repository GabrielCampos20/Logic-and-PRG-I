v = 0
def inscrição ():
    print("Seja bem vindo ao sitema do ColsPlay BJAnimax, o que deseja fazer?")
    print ("1 - Cadastro")
    print ("2 - Sair")  
    ação = int(input("Digite:"))
    if ação == 1:
        print ("Certo, então vamos lá!")
        categorias()
def categorias ():
    print ("primeiro escolha sua categoria:")
    print ("1 - Personagem Animax Favorito.")
    print ("2 - Melhor Traje.")
    print ("3 - Anime Legend.")
    print ("4 - ColsCreative.")
    print ("5 - Melhor Cosplay Geral.")
    categoria = int(input("Digite:"))
    if categoria == 1:
        print ("Certo, então agora me informe seus dados para que eu possa lhe colocar na competição.")
        nome = input("Nome:")
        idade = int(input("Idade:"))
        print ("Certo, então você se chama",nome,",tem",idade,"anos, e vai se inscrever em Personagem Animax Favorito, certo?Boa sorte",nome,"!!!")
    if categoria == 2:
        print ("Certo, então agora me informe seus dados para que eu possa lhe colocar na competição.")
        nome = input("Nome:")
        idade = int(input("Idade:"))
        print ("Certo, então você se chama",nome,",tem",idade,"anos, e vai se inscrever em Melhor Traje, certo?Boa sorte",nome,"!!!")
    if categoria == 3:
        print ("Certo, então agora me informe seus dados para que eu possa lhe colocar na competição.")
        nome = input("Nome:")
        idade = int(input("Idade:"))
        print ("Certo, então você se chama",nome,",tem",idade,"anos, e vai se inscrever em Melhor Anime Legend, certo?Boa sorte",nome,"!!!")
    if categoria == 4:
        print ("Certo, então agora me informe seus dados para que eu possa lhe colocar na competição.")
        nome = input("Nome:")
        idade = int(input("Idade:"))
        print ("Certo, então você se chama",nome,",tem",idade,"anos, e vai se inscrever em ColsCreative, certo?Boa sorte",nome,"!!!")
    if categoria == 5:
        print ("Certo, então agora me informe seus dados para que eu possa lhe colocar na competição.")
        nome = input("Nome:")
        idade = int(input("Idade:"))
        print ("Certo, então você se chama",nome,",tem",idade,"anos, e vai se inscrever em Melhor Cosplay Geral, certo?Boa sorte",nome,"!!!")
while v < 100:
    inscrição()
    v += 1
if v == 100:
    print ("Vagas totalmente preenchidas.")