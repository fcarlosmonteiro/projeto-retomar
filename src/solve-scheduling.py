from deap import base
from deap import creator
from deap import tools

import random
import numpy
import time

import matplotlib.pyplot as plt
import seaborn as sns

import elitism
import stores
import LocalConfig

# problem constants:
HARD_CONSTRAINT_PENALTY = 10  # the penalty factor for a hard-constraint violation

# Genetic Algorithm constants:
POPULATION_SIZE = 300
P_CROSSOVER = 0.9  # probability for crossover
P_MUTATION = 0.3   # probability for mutating an individual
MAX_GENERATIONS = 10
HALL_OF_FAME_SIZE = 30

# set the random seed:
RANDOM_SEED = 10
random.seed(RANDOM_SEED)

toolbox = [base.Toolbox(),base.Toolbox(),base.Toolbox(),base.Toolbox()]

# create the store scheduling problem instance to be used:
nsp = [
    stores.StoreSchedulingProblem(HARD_CONSTRAINT_PENALTY,0),
    stores.StoreSchedulingProblem(HARD_CONSTRAINT_PENALTY,1),
    stores.StoreSchedulingProblem(HARD_CONSTRAINT_PENALTY,2),
    stores.StoreSchedulingProblem(HARD_CONSTRAINT_PENALTY,3)
]

# define a single objective, maximizing fitness strategy:
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))

# create the Individual class based on list:
creator.create("Individual", list, fitness=creator.FitnessMin)

# create an operator that randomly returns 0 or 1:
toolbox[0].register("zeroOrOne", random.randint, 0, 1)
toolbox[1].register("zeroOrOne", random.randint, 0, 1)
toolbox[2].register("zeroOrOne", random.randint, 0, 1)
toolbox[3].register("zeroOrOne", random.randint, 0, 1)

# create the individual operator to fill up an Individual instance:
toolbox[0].register("individualCreator", tools.initRepeat,
                 creator.Individual, toolbox[0].zeroOrOne, len(nsp[0]))
toolbox[1].register("individualCreator", tools.initRepeat,
                 creator.Individual, toolbox[1].zeroOrOne, len(nsp[1]))
toolbox[2].register("individualCreator", tools.initRepeat,
                 creator.Individual, toolbox[2].zeroOrOne, len(nsp[2]))
toolbox[3].register("individualCreator", tools.initRepeat,
                 creator.Individual, toolbox[3].zeroOrOne, len(nsp[3]))                
# create the population operator to generate a list of individuals:
toolbox[0].register("populationCreator", tools.initRepeat,
                 list, toolbox[0].individualCreator)
toolbox[1].register("populationCreator", tools.initRepeat,
                 list, toolbox[1].individualCreator)
toolbox[2].register("populationCreator", tools.initRepeat,
                 list, toolbox[2].individualCreator)
toolbox[3].register("populationCreator", tools.initRepeat,
                 list, toolbox[3].individualCreator)
# fitness calculation
def getCost0(individual):
    return nsp[0].getCost(individual),  # return a tuple
def getCost1(individual):
    return nsp[1].getCost(individual),  # return a tuple
def getCost2(individual):
    return nsp[2].getCost(individual),  # return a tuple
def getCost3(individual):
    return nsp[3].getCost(individual),  # return a tuple

toolbox[3].register("evaluate", getCost3)
toolbox[2].register("evaluate", getCost2)
toolbox[1].register("evaluate", getCost1)
toolbox[0].register("evaluate", getCost0)

# genetic operators:
toolbox[0].register("select", tools.selTournament, tournsize=5)
toolbox[0].register("mate", tools.cxTwoPoint)
toolbox[0].register("mutate", tools.mutFlipBit, indpb=1.0/len(nsp[0]))

toolbox[1].register("select", tools.selTournament, tournsize=5)
toolbox[1].register("mate", tools.cxTwoPoint)
toolbox[1].register("mutate", tools.mutFlipBit, indpb=1.0/len(nsp[1]))

toolbox[2].register("select", tools.selTournament, tournsize=5)
toolbox[2].register("mate", tools.cxTwoPoint)
toolbox[2].register("mutate", tools.mutFlipBit, indpb=1.0/len(nsp[2]))

toolbox[3].register("select", tools.selTournament, tournsize=5)
toolbox[3].register("mate", tools.cxTwoPoint)
toolbox[3].register("mutate", tools.mutFlipBit, indpb=1.0/len(nsp[3]))


# Genetic Algorithm flow:
def main(quadrante):
    start_time = time.time()

    # create initial population (generation 0):
    population = toolbox[quadrante].populationCreator(n=POPULATION_SIZE)

    # prepare the statistics object:
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", numpy.min)
    stats.register("avg", numpy.mean)

    # define the hall-of-fame object:
    hof = tools.HallOfFame(HALL_OF_FAME_SIZE)

    # perform the Genetic Algorithm flow with hof feature added:
    population, logbook = elitism.eaSimpleWithElitism(population, toolbox[quadrante], cxpb=P_CROSSOVER, mutpb=P_MUTATION,
                                                      ngen=MAX_GENERATIONS, stats=stats, halloffame=hof, verbose=True)

    time_execution = time.time() - start_time
    # print best solution found:
    best = hof.items[0]
    print("-- Time execution", time_execution)
    #print("-- Best Individual = ", best)
    print("-- Best Fitness = ", best.fitness.values[0])
    print()
    print("-- Schedule = ")
    nsp[quadrante].printScheduleInfo(best)
    arquivo = open('results'+LocalConfig.local+'/resultados.txt', 'w')
    arquivo.write("-- Time execution = "+ str(time_execution))
    arquivo.write("\n-- Best Fitness = "+ str(best.fitness.values[0]))
    arquivo.close()
    # extract statistics:
    minFitnessValues, meanFitnessValues = logbook.select("min", "avg")

    # plot statistics:
    sns.set_style("whitegrid")
    plt.plot(minFitnessValues, color='red')
    plt.plot(meanFitnessValues, color='green')
    plt.xlabel('Generation')
    plt.ylabel('Min / Average Fitness')
    plt.title('Min and Average fitness over Generations')
    plt.show()


if __name__ == "__main__":
    main(0)
