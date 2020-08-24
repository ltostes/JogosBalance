import pandas as pd
import numpy as np
import random
import json
from pyeasyga import pyeasyga

# Run params

number_of_teams = 4

competencies_multipler = 1
history_multiplier = 1

participants_path = 'example_data/participants.json'
modalweights_path = 'example_data/modal_weights.json'

# Loading participants
participants = {}

with open(participants_path,'r') as f:
    participants = json.load(f)

participants_list = list(participants.keys())

# Loading modal weights
modals_weigths = {}

with open(modalweights_path,'r') as f:
    modals_weigths = json.load(f)

# Loading participants info
competencies = [it['Competencies'] for it in participants.values()]
preferences = [it['Preferences'] for it in participants.values()]
history = [it['History'] for it in participants.values()]


# Model functions
def create_individual(data):
    remainder = list(data)[:]

    individual = [[] for i in range(0,number_of_teams)]
    
    team_num = 0

    while remainder:
        individual[team_num].append(remainder.pop())

        team_num += 1
        if team_num == 4: team_num = 0

    return individual

def crossover(parent_1, parent_2):
    crossover_index = random.randrange(1, len(parent_1))

    child_1 = parent_1[:crossover_index] + parent_2[crossover_index:]
    child_2 = parent_2[:crossover_index] + parent_1[crossover_index:]
    
    return child_1, child_2

def mutate(individual):
    mutate_1_team, mutate_2_team = random.sample(range(1,len(individual)),2)
    
    mutate_1_member = random.sample(range(1,len(individual[mutate_1_team])),1)[0]
    mutate_2_member = random.sample(range(1,len(individual[mutate_2_team])),1)[0]
    
    individual[mutate_1_team][mutate_1_member], individual[mutate_2_team][mutate_2_member] = individual[mutate_2_team][mutate_2_member], individual[mutate_1_team][mutate_1_member] 

def selection(population):
    return random.choice(population)

def fitness(individual, data):
    fitness = 0

    # preference fitness
    for team in individual:
        for member in team:

            colleagues = team[:]
            colleagues.remove(member)

            for colleague in colleagues:
                
                # if preferred, increase fitness
                fitness += data[member][1][colleague]
    
    # balance fitness
    modals_total_weight = sum(modals_weigths.values())
    for modal in list(modals_weigths):
        team_scores = []
        for team in individual:
            team_score = 0
            for member in team:
                team_score += data[member][0][modal]
            team_scores.append(team_score)
        
        # if discrepancy in levels is too bad, decrease fitness
        fitness -= competencies_multipler * (max(team_scores) - min(team_scores)) * (modals_weigths[modal] / modals_total_weight)

    # history fitness
    for team in individual:
        for member in team:

            colleagues = team[:]
            colleagues.remove(member)

            for colleague in colleagues:
                
                # if preferred, increase fitness
                fitness -= history_multiplier * data[member][2][colleague]

    return fitness

# Running

data = dict(dict(zip(participants,zip(competencies,preferences,history))))

ga = pyeasyga.GeneticAlgorithm(data,
                               population_size=100,
                               generations=500,
                               crossover_probability=0.0,
                               mutation_probability=0.2,
                               elitism=True,
                               maximise_fitness=True)

ga.create_individual = create_individual

ga.crossover_function = crossover

ga.mutate_function = mutate

ga.selection_function = selection

ga.fitness_function = fitness

ga.run()

results = ga.best_individual()

print('Score: ', results[0])

print('')

for team_num in range(0,len(results[1])):
    print("Team ",team_num + 2)
    for member in results[1][team_num]:
        print(member)
    print("")

for individual in ga.last_generation():
    print(individual)

