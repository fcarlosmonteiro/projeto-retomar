from random import random
from operator import itemgetter
import pandas as pd

bd = pd.read_csv('database.csv')

global iterations
global max_open

max_open = 4

dados = []
for i in range(13):
    dados.append(bd.iloc[i, 0:2])


def create_solution():
    current = []
    for i in range(max_open):
        id = 0+int(11*random())
        current.append(id)
    sol = check_clone(current)
    print("current solution: ", sol)
    return sol


def check_clone(solution):
    sol = []
    for id in solution:
        if id not in sol:
            sol.append(id)
        else:
            sol.append(0+int(11*random()))
    return sol


def fitness_function(solution):
    unfulfilled = 0
    for id in solution:
        if dados[id].loc['Distancias'] <= 2:
            unfulfilled += 1
    print("unfufilled = ", unfulfilled)
    return unfulfilled


def extends_neighborhood(current):

    # neighbor1
    neighbor1_temp = current.copy()
    neighbor1_temp[0] = neighbor1_temp[0]+1
    neighbor1 = check_clone(neighbor1_temp)

    # neighbor2
    neighbor2_temp = current.copy()
    neighbor2_temp[1] = neighbor2_temp[1]+1
    neighbor2 = check_clone(neighbor2_temp)

    # neighbor3
    neighbor3_temp = current.copy()
    neighbor3_temp[2] = neighbor3_temp[2]+1
    neighbor3 = check_clone(neighbor3_temp)

    # neighbor4
    neighbor4_temp = current.copy()
    neighbor4_temp[3] = neighbor4_temp[3]+1
    neighbor4 = check_clone(neighbor4_temp)

    neighborhood = [neighbor1, neighbor2, neighbor3, neighbor4]
    print(neighborhood)

    return neighborhood


def hc_process(iterations):
    c = 0
    best_solution = []
    best_fit = -1
    current = create_solution()
    while (c < iterations):
        neighborhood = extends_neighborhood(current)
        for sol in neighborhood[0:len(neighborhood)]:
            fit_current = fitness_function(current)
            fit_neighbor = fitness_function(sol)
            print("current solution:", current, " fit:", str(fit_current))
            print("neighbor", sol, " fit:", str(fit_neighbor))
            if (fit_neighbor <= fit_current):
                current = sol.copy()
                best_solution = current
                best_fit = fit_neighbor
            else:
                current
        c = c+1
    print("The best solution:", best_solution, "fitness:", best_fit)
    return current


hc_process(100)
