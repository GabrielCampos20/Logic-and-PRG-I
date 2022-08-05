def menu_principal(  ):
	print(" 1- sair do banco")
	print(" 2- fazer saque ")
	print(" 3- depositos")
	print(" 4- Tranferencias")
	
	
def saque( ):
	saque = int(input(" Valor que deseja sacar: "))
	qnt = saque
	nota = 50
	ttlnota = 0
	while True:
		if qnt >= nota:
			qnt = qnt - nota
			ttlnota = ttlnota + 1
		
		else:
			if ttlnota > 0:
				print("     ",ttlnota,"notas de",nota)
			if nota == 50:
				nota = 20
			elif nota == 20:
				nota = 10
			elif nota == 10:
				nota = 1
			ttlnota = 0
		

	else:
  	  print(" o programa finalizou")
	
  	  
def deposito( ):
	nome = input(" digite o nome do titular da conta:  ")
	CPF = int(input(" digite o numero do CPF do titular:  "))
	NBanco = int(input("digite o numero do banco: "))
	conta = int(input(" digite o numero da conta que vc ira realizar o deposito:   "))
	deposito = int(input(" Valor que deseja depositar: "))
	print(" Foi depositado a quantia de",deposito,"na conta de numero",conta)
	print("Dados do titular: nome:",nome,)
	print('÷' *40)
	print(" CPF:",CPF)
	qnt = deposito
	nota = 50
	ttlnota = 0
	while True:
		if qnt >= nota:
			qnt = qnt - nota
			ttlnota = ttlnota + 1
		
		else:
			if ttlnota > 0:
				print(" ",ttlnota,"notas de",nota)
			if nota == 50:
				nota = 20
			elif nota == 20:
				nota = 10
			elif nota == 10:
				nota = 1
			ttlnota = 0

	else:
  	  print(" o programa finalizou")	


def Transferencia( ):
	Deqm = input("Digite o nome completo do destinatario da transferencia:   ")
	qm = input("digite seu nome completo por gentileza:  ")
	agencia = int(input(" Digite a agencia do seu banco: "))
	tpconta = input("Sua conta é corrente ou poupanca?       ")
	NConta = int(input(" Digite o numeto da sua conta:   "))
	valor = int(input("Digite o valor a ser transferido: "))
	print(" o montante no valor de",valor," será trasnferida para",Deqm)
	x = int(input("Vc reconhece essa transferencia? Se sim, digite 1, caso não reconheca, digite 2 para q possamos cencelá-la. "))
	if x == 2:
		print("Transacao cancelada.")
		
	elif x == 1:
		print("Sua transacao esta em andamento")
		import time
		time.sleep(2)
	    
	print("transacao realizada com sucesso")
	    
	    


# agencia
# poupanca ou corrente 
# conta
# valor
# de fulano pra cicrano



def apresentacao( ):
	print("Seja bem vindo(a) ao Banco programar, o banco do CT.")
	menu_principal( )
	
apresentacao( )	
OP = int(input(" digite o numero da opcao desejada: "))
if OP == 1:
	print(" fim do atendimento. Volte sempre.")
if OP == 2:
	saque( )
if OP == 3:
	deposito( )
elif OP == 4:
	Transferencia( )