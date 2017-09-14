import os

class Velha():
	
	def __init__(self):
		self.turno = 1                                         #serve para identificar se quem vai jogar vai ser o player1 ou o player2
		self.t1 = "1"
		self.t2 = "2"
		self.t3 = "3"
		self.t4 = "4"
		self.t5 = "5"
		self.t6 = "6"
		self.t7 = "7"
		self.t8 = "8"
		self.t9 = "9"
		self.disponiveis = [self.t1,self.t2,self.t3,           #lista de quadrados disponiveis para serem jogados
                            self.t4,self.t5,self.t6,
				            self.t7,self.t8,self.t9]
		self.sets_p1 = [[1,2,3],[4,5,6],[7,8,9],               #lista das combinacoes possiveis para o player1 ganhar
					    [1,4,7],[2,5,8],[3,6,9],
					    [1,5,9],[3,5,7]]
		self.sets_p2 = [[1,2,3],[4,5,6],[7,8,9],               #lista das combinacoes possiveis para o player2 ganhar
                        [1,4,7],[2,5,8],[3,6,9],
                        [1,5,9],[3,5,7]]

	def show_turno_board(self):                                #checa o turno e retorna uma string correspondente
		if self.turno == 1:
			return "Turno do Player 1"
		else:
			return "Turno do Player 2"
	
	def board(self):                                           #imprime tabuleiro
		print("\n "+self.t1+" | "+self.t2+" | "+self.t3)
		print("-----------")
		print(" "+self.t4+" | "+self.t5+" | "+self.t6)
		print("-----------")
		print(" "+self.t7+" | "+self.t8+" | "+self.t9)
		print("\nP1 = O")
		print("P2 = X")
		print("\n"+self.show_turno_board())
		
	def board_string(self):
		return "\n "+self.t1+" | "+self.t2+" | "+self.t3+"\n-----------"+"\n "+self.t4+" | "+self.t5+" | "+self.t6+"\n-----------"+"\n "+self.t7+" | "+self.t8+" | "+self.t9+"\n\nP1 = O"+"\nP2 = X"+"\n\n"+self.show_turno_board()

	def refresh(self):                                         #refresh no console
		os.system('cls' if os.name == 'nt' else 'clear')       #serve para limpar o console no windows e linux
		self.board()                                           #imprime o tabileiro novamente

	def contabilizar_bola(self,tile):                          #contabiliza jogada player1
		if tile in self.disponiveis:                           #checa na lista de disponiveis se o quadrado esta disponivel
			self.disponiveis.remove(tile)                      #remove da lista dos disponiveis
			tile = int(tile)                                   #necessario pois o tile eh uma string
			for x in self.sets_p1:                             #percorrer a lista de combinacoes possiveis onde x tambem eh uma lista(combinacao)
				if tile in x:                                  #previne que o passo abaixo nao gere um erro
					x.remove(tile)                             #remove o quadrado de todas as combinacoes onde ele aparece. Ex: tile = 1, x = [1,2,3] -----> x = [2,3] 
			return True                                        #retorna True para sinalizar que tudo ocorreu certo
		else: return False                                     #caso nao esteja disponivel retorna False

	def contabilizar_x(self,tile):                             #contabiliza jogada layer2, fazendo igual ao player1
		if tile in self.disponiveis:
			self.disponiveis.remove(tile)
			tile = int(tile)
			for x in self.sets_p2:
				if tile in x:
					x.remove(tile)
			return True
		else: return False

	def casa_invalida(self):                                   #sera usada caso a funcao de contabilizar retorne False
		self.turno = -self.turno                               #faz com que posteriormente o turno permaneca do mesmo jogador, para que ele possa selecionar um quadrado valido
		print("Casa invalida")

	def traduzir(self,entrada,player):                         #traduz a entrada de uma string para o atributo da classe que representa as casas, chama as funcoes para contabilizar direto
		sinal = ""
		contabilizar = None
		if player == 1:
			sinal = "O"                                        #como convencionado, player1 eh bola
			contabilizar = self.contabilizar_bola 
		else:
			sinal = "X"                                        #como convencionado, player2 eh x
			contabilizar = self.contabilizar_x

		if entrada == "1": 
			if contabilizar(self.t1) == True:                  #checa se foi possivel contabilizar, se sim:
				self.t1 = sinal                                #troca a string do numero para o sinal do jogador (O ou X)
				self.refresh() 
			else:                                              #caso a casa ja tenha sido usada
				self.casa_invalida()
		elif entrada == "2": 
			if contabilizar(self.t2) == True:
				self.t2 = sinal
				self.refresh()
			else: 
				self.casa_invalida()
		elif entrada == "3": 
			if contabilizar(self.t3) == True:
				self.t3 = sinal
				self.refresh()
			else: 
				self.casa_invalida()
		elif entrada == "4": 
			if contabilizar(self.t4) == True:
				self.t4 = sinal
				self.refresh()
			else: 
				self.casa_invalida()
		elif entrada == "5": 
			if contabilizar(self.t5) == True:
				self.t5 = sinal
				self.refresh()
			else: 
				self.casa_invalida()
		elif entrada == "6": 
			if contabilizar(self.t6) == True:
				self.t6 = sinal
				self.refresh()
			else: 
				self.casa_invalida()
		elif entrada == "7": 
			if contabilizar(self.t7) == True:
				self.t7 = sinal
				self.refresh()
			else: 
				self.casa_invalida()
		elif entrada == "8": 
			if contabilizar(self.t8) == True:
				self.t8 = sinal
				self.refresh()
			else: 
				self.casa_invalida()
		elif entrada == "9": 
			if contabilizar(self.t9) == True:
				self.t9 = sinal
				self.refresh()
			else: 
				self.casa_invalida()
		else: 
			self.casa_invalida()
			return False 

	def escolher_p1(self,entrada):                             #recebe do usuario a string da casa que ele quer jogar, nesse caso do player1
		self.traduzir(entrada,1) 
		self.turno = -self.turno                               #inverte o turno, possibilitando o outro player jogar

	def escolher_p2(self,entrada):
		self.traduzir(entrada,2)
		self.turno = -self.turno

	def p1_ganhou(self):                                       #checa se alguma lista no conjunto de lista do player esta vazia
		for x in self.sets_p1:
				if x == []:
					return True                                #retorna True, caso ache alguma lista vazia, significa que o player ganhou
		return False

	def p2_ganhou(self):
		for x in self.sets_p2:
				if x == []:
					return True
		return False
		
	def jogar(self,entrada):

		if self.disponiveis == [] and self.p1_ganhou() == False and self.p2_ganhou() == False:  #primeiro checa se nao ha nenhuma possibilidade de jogada e nenhum player ganhou-
			print("\nDEU VELHA!")                                                      #-ou seja, deu velha
			return 3

		if self.turno == 1:                                                               #caso Velha().turno == 1, significa que eh a vez do player1 de jogar                                                
			self.escolher_p1(entrada)                                                     #chama o metodo de escolher passando como parametro a entrada que foi imediatamente recebida
			if self.p1_ganhou() == True:                                                  #checa toda vez se o player ganhou
				print("\nP1 GANHOU!")
				return 1
			return False
		else:                                                                          #caso Velha().turno != 1, significa que eh a vez do player2, e o processo se repete
			self.escolher_p2(entrada)
			if self.p2_ganhou() == True:
				print("\nP2 GANHOU!")
				return 2
			return False


