from math import floor

from dna import member
from random import randint

class population:
	def __init__(self, target, mutation_rate, pop_max):
		self.target_phrase = target
		self.mutation_rate = mutation_rate
		self.pop_max = pop_max
		self.pop = []
		self.finish = False
		self.generations = 0
		self.mating_pool = []

		for i in range(1, self.pop_max):
			self.pop.append(member(length=len(self.target_phrase)))

		self.calc_fitness(len(self.target_phrase))

	def calc_fitness(self, length):
		for i in range(0, len(self.pop), 1):
			self.pop[i].get_fitness(self.target_phrase)

	def selection(self):
		self.mating_pool.clear()
		self.max_fitness = 0
		for item in self.pop:
			if item.fitness > self.max_fitness:
				self.max_fitness = item.fitness

		for item in self.pop:
			fitness = (item.fitness / self.max_fitness)
			n = floor(fitness * 100)
			i = 0

			while i < n:
				self.mating_pool.append(item)
				i += 1

	def generate(self):

		for i in range(0, self.pop_max - 1, 1):
			a = randint(0, len(self.mating_pool) - 1)
			b = randint(0, len(self.mating_pool) - 1)
			parent_a = self.mating_pool[a]
			parent_b = self.mating_pool[b]

			child = parent_a.crossover(parent_b)
			child.mutate(self.mutation_rate)
			child.phrase = child.get_phrase()
			self.pop[i] = child

#			print(child.phrase)

		self.generations += 1

#		print("\n \n \n")
#		print(self.generations)
#		print("\n \n \n")

		self.finished()

	def finished(self):
		for word in self.pop:
			if word.phrase == self.target_phrase:
				self.finish = True

	def all_phrases(self):
		self.everything = ""
		display_limit = min(self.pop_max, 40)

		for i in range(0, display_limit):
			self.everything += f"{self.pop[i].phrase} \n"

		return self.everything

	def get_best(self):
		best_fit = 0
		best_one = self.pop[0]
		for members in self.pop:
			if members.fitness > best_fit:
				best_fit = members.fitness
				best_one = members

		return best_one

	def avg_fit(self):
		n = 0
		for members in self.pop:
			n += members.fitness
		return n / len(self.pop)
