import numpy as np
import random
import matplotlib.pyplot as plt
from SIR_model import *
from feasible_region import *

class Virus:
    def __init__(self,alpha,beta):
        self.alpha=alpha
        self.beta=beta
        self.sol=solve(alpha,beta)
        self.fitness=fitness(self.sol)
    
    def __str__(self):
        return f"alpha:{self.alpha}, beta:{self.beta}, fitness:{self.fitness}"
  

# GA setting
hypothesis = {1:"Avirulence", 2:"Trade-off"}[2]
pop_size=100
mutation_rate=0.1
mutation_range=0.02
max_gen=50
seed=1
random.seed(seed)

def get_random(hypothesis):
    while True:
        alpha = random.uniform(0,1)
        beta = random.uniform(0,1)
        if is_feasible(hypothesis, alpha, beta):
            return Virus(alpha, beta)
    

def fitness(sol):
    return sol.y[1][-1]
    
def mutate(virus,hypothesis,mutation_rate,mutation_range):
    alpha=virus.alpha
    beta=virus.beta
    if random.random()<mutation_rate:
        while True:
            new_alpha=alpha+random.uniform(-mutation_range,mutation_range)
            new_beta=beta+random.uniform(-mutation_range,mutation_range)
            if(is_feasible(hypothesis,new_alpha,new_beta)):
                return Virus(new_alpha,new_beta)
    else:
        return Virus(alpha,beta)

def ga(hypothesis,pop_size,mutation_rate,mutation_range,max_gen):
    # initialize a random population
    population = []
    best_viruses = []
    generation = 0
    while len(population) < pop_size:
        population.append(get_random(hypothesis))

    while True:
        generation += 1
        nextgen_pop=[]

        # make next generation with mutation
        for parent in population:
            child=mutate(parent,hypothesis,mutation_rate,mutation_range)
            nextgen_pop.append(child)

        # generational selection
        combined = []
        combined.extend(population)
        combined.extend(nextgen_pop)


        population = sorted(combined, key=lambda x: x.fitness, reverse=True)[:pop_size]
        best_viruses.append(population[0])

        # terminate if stop condition is met
        if generation==max_gen:
            return best_viruses

def plot_evolution(best_viruses,hypothesis):
    fig, ax = plt.subplots(figsize=(6,6))
    x = np.linspace(0, 1, 100)
    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    ax.set_xlabel("Virulence")
    ax.set_ylabel("Transmission rate")
    if hypothesis=="Avirulence":
        ax.fill_between(x, alpha_bound, 1, color='blue', alpha=0.3)
        ax.plot(x, [alpha_bound]*100, '--', color='blue')
    else:
        y= slope * x
        y = np.clip(y, 0, 1)
        ax.fill_between(x, y, 1, color='blue', alpha=0.3)
        ax.plot(x, y, '--', color='blue')
    alphas = [v.alpha for v in best_viruses]
    betas = [v.beta for v in best_viruses]
    plt.scatter(betas, alphas, c=range(len(best_viruses)), cmap='viridis', s=50, edgecolor='k')
    plt.colorbar(label='Generation')
    plt.title("Evolution of Alpha-Beta over Generations")
    plt.show()


best_viruses=ga(hypothesis,pop_size,mutation_rate,mutation_range,max_gen)
plot_evolution(best_viruses,hypothesis)
plot_model(best_viruses[0].sol)