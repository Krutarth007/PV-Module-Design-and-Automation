import random as rd

solar_cell_e = [10,11,13]
solar_cell_c = [50,60,70]
budget = 110

def generate_population(n=10):
	i=0
	population = []
	while i<n:
		population.append(rd.randint(0,len(solar_cell_e)-1))
		i = i + 1
	return population

def score(solar_type):
	if solar_cell_c[solar_type] > budget:
		return 0
	return budget - solar_cell_c[solar_type]


