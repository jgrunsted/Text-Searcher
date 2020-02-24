import random
from random import randint


class member:
	def __init__(self, length):
		self.target_length = length
		self.fitness = 0

		self.genes = []
		for i in range(0, self.target_length, 1):
			self.genes.append(chr(randint(32, 122)))

		self.phrase = self.get_phrase()

	def get_fitness(self, target):
		self.score = 0
		for i in range(0, self.target_length, 1):
			if target[i] == self.genes[i]:
				self.score += 1

		self.fitness = self.score / self.target_length

	def crossover(self, partner):
		child = member(self.target_length)

		midpoint = randint(0, self.target_length)

		for i in range(0, self.target_length):
			if i > midpoint:
				child.genes[i] = self.genes[i]
			else:
				child.genes[i] = partner.genes[i]

		return child

	def mutate(self, mutation_rate):
		for i in range(0, self.target_length):
			if random.random() < mutation_rate:
				self.genes[i] = chr(randint(32, 122))

	def get_phrase(self):
		word = ""
		for w in self.genes:
			word += w

		return word
