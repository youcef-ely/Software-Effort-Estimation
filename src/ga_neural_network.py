import random
import matplotlib.pyplot as plt 
from neural_network import NeuralNetwork 
import time
import metrics
class GeneticAlgorithm:
        
  def __init__(self, parameters_ranges: dict, X_train, y_train, size_of_population: int, fitness_limit, time_limit, probability: float = 0.1, mutation_number: int = 1, metrics = metrics):
    self.parameters_ranges = parameters_ranges
    self.X_train = X_train
    self.y_train = y_train
    self.size_of_population = size_of_population
    self.probability = probability
    self.mutation_number = mutation_number
    self.fitness_limit = fitness_limit
    self.scores = []
    self.best_indiv_per_gen = []
    self.time_limit = time_limit
    self.metrics = metrics
  "----------------------------------------------------------    Utils     ------------------------------------------------"
  def get_scores(self):
    return self.scores
  
  def get_mean_scores(self):
      return self.mean_score
  
  def generate_chromosome(self):
    return {list(self.parameters_ranges.keys())[i]: random.choices(list(self.parameters_ranges.values())[i])[0] for i in range(len(self.parameters_ranges))}


  def plot_generations_scores(self, title = ''):
    scores = self.get_scores()
    fig = plt.figure(figsize = (15, 10))
    plt.plot(scores, c = 'seagreen', label = 'Max score per generation')
    plt.xlabel('Generation')
    plt.ylabel('5K FOLD cv score')
    plt.title(title)
    plt.legend()
    plt.show()
    fig.savefig('/content/'+title+'.pdf')
  

  

  "------------------------------------------------------------------------------------------------------"



  "-----------------------------------------GA algorithm functions-------------------------------------------------------------"
  def generate_population(self):
    return [self.generate_chromosome() for i in range(self.size_of_population)]
  
  def fitness_function(self, chromosome): 
    model = NeuralNetwork(chromosome, self.X_train, self.y_train, 3000)
    return model.cv_scores(self.metrics)['r2'].mean()

  def selection_pair(self, population):
    return self.sort_population(population)[0: 2]

  def uniform_crossover(self, chromosome1, chromosome2):
    new_chromosome1 = chromosome1.copy()
    new_chromosome2 = chromosome2.copy()
    if len(chromosome1) != len(chromosome2):
      raise ValueError('Chromosomes must have the same length')
    if len(chromosome1) < 2 or len(chromosome2) < 2:
      return new_chromosome1, new_chromosome2
    param_names = [key for key in self.parameters_ranges.keys() if random.choices([0, 1], weights = [0.5, 0.5], k = 1)[0] == 0]
    for param in param_names:
      new_chromosome1[param], new_chromosome2[param] = new_chromosome2[param], new_chromosome1[param]
    return new_chromosome1, new_chromosome2

  def mutation(self, chromosome):
    mutant_chromosome = chromosome.copy()
    for _ in range(self.mutation_number):
          param_name = random.choices(list(self.parameters_ranges.keys()))[0]
          if random.uniform(0, 1) > self.probability :
            mutant_chromosome[param_name] = random.choices(list(self.parameters_ranges[param_name]))[0]
    return mutant_chromosome

  #Sort population
  def sort_population(self, population):
    return sorted(population, key = lambda chromosome: self.fitness_function(chromosome), reverse = True)

  def evolution(self):
    start_time = time.time()
    population = self.generate_population()
    population = self.sort_population(population)
    while(self.fitness_limit > self.fitness_function(population[0]) and time.time() - start_time < self.time_limit*60):
      # Selection Pair
      parent1, parent2 = self.selection_pair(population)
      next_generation = [parent1, parent2]
      # Cross over
      off_spring1, off_spring2 = self.uniform_crossover(parent1, parent2)
      next_generation += [off_spring1, off_spring2]
      # Mutation
      off_spring1, off_spring2 = self.mutation(off_spring1), self.mutation(off_spring2)
      next_generation += [off_spring1, off_spring2]
      # Next generation
      population = next_generation
      population = self.sort_population(population)

      # To store the evolution of the score
      self.best_indiv_per_gen.append(population[0]) 

    population = self.sort_population(population)
    return population



    "------------------------------------------------------------------------------------------------------"

