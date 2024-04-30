import numpy as np
class VetorNaoOrdenado:
	def __init__(self, capacidade):
		self.capacidade = capacidade
		self.ultima_posicao = -1
		self.valores = np.empty(self.capacidade, dtype=int)


	def imprime(self):
		if self.ultima_posicao == -1:
			print('O vetor está vazio')
		else:
			vetorTemp = self.bubbleSort()
			for i in range(self.ultima_posicao + 1):
				print(i, ' - ', vetorTemp[i])


	def insere(self, valor):
		if valor in self.valores:
			print('Valor já existe no vetor')
			return -1
		if self.ultima_posicao == self.capacidade - 1:
			print('Capacidade máxima atingida')
			return -1
		else:
			self.ultima_posicao += 1
			self.valores[self.ultima_posicao] = valor


	def pesquisar(self, valor):
		for i in range(self.ultima_posicao + 1):
			if valor == self.valores[i]:
				return i
		return -1


	def excluir(self, valor):
		posicao = self.pesquisar(valor)
		if posicao == -1:
			return -1
		else:
			for i in range(posicao, self.ultima_posicao):
				self.valores[i] = self.valores[i + 1]

			self.ultima_posicao -= 1
   
	def estaVazio(self):
		if self.ultima_posicao == -1:
			return True
		return False

	def bubbleSort(self):
		vetorTemp = self.valores.copy()
		if self.estaVazio():
			print('Vetor vazio')
			return
		for i in range (self.capacidade):
			for j in range(self.capacidade - 1):
				if vetorTemp[j] > vetorTemp[j + 1]:
					vetorTemp[j], vetorTemp[j + 1] = vetorTemp[j + 1], vetorTemp[j]
		return vetorTemp
    
	def pesquisaBinaria(self, valor):
		vetorTemp = self.bubbleSort()

		limiteInferior = 0
		limiteSuperior = self.ultima_posicao

		while True:
			posicaoAtual = int((limiteInferior + limiteSuperior) / 2)
			if vetorTemp[posicaoAtual] == valor:
				return posicaoAtual
			elif limiteInferior > limiteSuperior:
				return -1
			else:
				if vetorTemp[posicaoAtual] < valor:
					limiteInferior = posicaoAtual + 1
				else:
					limiteSuperior = posicaoAtual - 1
		

vetor = VetorNaoOrdenado(4)
vetor.insere(2)
vetor.insere(3)
vetor.insere(1)
vetor.insere(4)
print(vetor.excluir(1))
vetor.imprime()
