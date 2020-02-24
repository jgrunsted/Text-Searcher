import tkinter as tk
from population import population


class window(tk.Canvas):
	def __init__(self):
		super().__init__(width=1600, height=900, background="white", highlightthickness=0)
		self.target = "magnificent"  # target phrase
		self.max_pop = 500  # maximum population
		self.mutation_rate = 0.01 # % chance of a mutation


		self.population = population(target=self.target, mutation_rate=self.mutation_rate, pop_max=self.max_pop)
		self.display()
		self.after(10, self.perform_actions)

	def perform_actions(self):
		self.population.selection()
		self.population.generate()
		self.population.calc_fitness(len(self.target))
		self.update_ui()
		if not self.population.finish:
			self.after(10, self.perform_actions)

	def display(self):
		self.create_text(75, 75, text=f"Target Phrase: {self.target}", fill="black", font=("Helvetica", 20), anchor="w")
		self.create_text(600, 475, text=f"All Phrases: \n {self.population.all_phrases()}", tag="everything", fill="black", font=("Helvetica", 14), anchor="w")
		self.create_text(75, 100, text=f"Best Phrase: {self.population.get_best().phrase}", tag="best", fill="black", font=("Helvetica", 25), anchor="w")
		self.create_text(75, 125, text=f"Generation: {self.population}", tag="gen", fill="black", font=("Helvetica", 20), anchor="w")
		self.create_text(75, 145, text=f"Average fitness: {self.population.avg_fit()}", tag="avg", fill="black", font=("Helvetica", 20), anchor="w")

	def update_ui(self):
		all = self.find_withtag("everything")
		self.itemconfigure(all, text=f"All Phrases: \n {self.population.all_phrases()}", tag="everything")
		best = self.find_withtag("best")
		self.itemconfigure(best, text=f"Best Phrase: {self.population.get_best().phrase}", tag="best")
		g = self.find_withtag("gen")
		self.itemconfigure(g, text=f"Generation: {self.population.generations}", tag="gen")
		a = self.find_withtag("avg")
		self.itemconfigure(a, text=f"Average fitness: {self.population.avg_fit()}", tag="avg")

root = tk.Tk()
root.title("genetic text searcher")
root.resizable(True, False)

wn = window()
wn.pack()

root.mainloop()
