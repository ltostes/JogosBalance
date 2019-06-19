import pandas as pd
import numpy as np
import random
from pyeasyga import pyeasyga

number_of_teams = 4

participants = [
        'Lucas Neno',
        'Bruno Mibielli',
        'Pedro Aquino',
        'Paulo Galeão',
        'João Pedro Castro',
        'Duda Magluta',
        'Lucas Tostes',
        'Gabriel Lessa',
        'Felipe Arêas',
        'Patrícia Telles',
        'Tito Labrunie',
        'Ilan Vale',
        'Roberto Soares',
        'Isadora Barretto',
        'Rafael Freitas',
        'Luaré'
    ]

modals_weigths = {  'Badminton'                 :2,
                    'Vôlei de grama'            :3,
                    'Ping pong de mesa'         :2,
                    'Beer pong'                 :3,
                    'Chute a garrafa'           :2,
                    'Baralho (Sueca, Truco...)' :1,
                    'Videogames'                :3,
                    'Imagem & Ação'             :2,
                    'Sobremesa'                 :1,
                    'Coregrafia'                :1,
                    'Boardgames'                :2
                    }

competencies_multipler = 1

competencies = [
        {'Badminton':2,'Vôlei de grama':4,'Ping pong de mesa':3,'Beer pong':3,'Chute a garrafa':1,'Baralho (Sueca, Truco...)':2,'Videogames':3,'Imagem & Ação':5,'Sobremesa':5,'Coregrafia':4,'Boardgames':5},
        {'Badminton':3,'Vôlei de grama':3,'Ping pong de mesa':3,'Beer pong':3,'Chute a garrafa':1,'Baralho (Sueca, Truco...)':0,'Videogames':5,'Imagem & Ação':5,'Sobremesa':3,'Coregrafia':3,'Boardgames':3},
        {'Badminton':0,'Vôlei de grama':0,'Ping pong de mesa':0,'Beer pong':1,'Chute a garrafa':0,'Baralho (Sueca, Truco...)':2,'Videogames':4,'Imagem & Ação':3,'Sobremesa':1,'Coregrafia':1,'Boardgames':3},
        {'Badminton':2,'Vôlei de grama':2,'Ping pong de mesa':2,'Beer pong':2,'Chute a garrafa':2,'Baralho (Sueca, Truco...)':0,'Videogames':2,'Imagem & Ação':2,'Sobremesa':2,'Coregrafia':2,'Boardgames':2},
        {'Badminton':4,'Vôlei de grama':3,'Ping pong de mesa':4,'Beer pong':5,'Chute a garrafa':1,'Baralho (Sueca, Truco...)':5,'Videogames':4,'Imagem & Ação':4,'Sobremesa':4,'Coregrafia':3,'Boardgames':4},
        {'Badminton':5,'Vôlei de grama':5,'Ping pong de mesa':5,'Beer pong':5,'Chute a garrafa':0,'Baralho (Sueca, Truco...)':3,'Videogames':1,'Imagem & Ação':2,'Sobremesa':4,'Coregrafia':3,'Boardgames':3},
        {'Badminton':5,'Vôlei de grama':4,'Ping pong de mesa':4,'Beer pong':4,'Chute a garrafa':5,'Baralho (Sueca, Truco...)':3,'Videogames':5,'Imagem & Ação':5,'Sobremesa':1,'Coregrafia':5,'Boardgames':5},
        {'Badminton':1,'Vôlei de grama':1,'Ping pong de mesa':2,'Beer pong':1,'Chute a garrafa':2,'Baralho (Sueca, Truco...)':0,'Videogames':3,'Imagem & Ação':1,'Sobremesa':0,'Coregrafia':1,'Boardgames':1},
        {'Badminton':3,'Vôlei de grama':3,'Ping pong de mesa':4,'Beer pong':2,'Chute a garrafa':3,'Baralho (Sueca, Truco...)':1,'Videogames':4,'Imagem & Ação':3,'Sobremesa':3,'Coregrafia':2,'Boardgames':3},
        {'Badminton':2,'Vôlei de grama':2,'Ping pong de mesa':1,'Beer pong':1,'Chute a garrafa':0,'Baralho (Sueca, Truco...)':0,'Videogames':1,'Imagem & Ação':0,'Sobremesa':2,'Coregrafia':2,'Boardgames':1},
        {'Badminton':4,'Vôlei de grama':5,'Ping pong de mesa':3,'Beer pong':5,'Chute a garrafa':2,'Baralho (Sueca, Truco...)':0,'Videogames':3,'Imagem & Ação':4,'Sobremesa':0,'Coregrafia':4,'Boardgames':3},
        {'Badminton':5,'Vôlei de grama':5,'Ping pong de mesa':5,'Beer pong':4,'Chute a garrafa':3,'Baralho (Sueca, Truco...)':5,'Videogames':3,'Imagem & Ação':5,'Sobremesa':1,'Coregrafia':5,'Boardgames':3},
        {'Badminton':2,'Vôlei de grama':2,'Ping pong de mesa':2,'Beer pong':2,'Chute a garrafa':2,'Baralho (Sueca, Truco...)':2,'Videogames':2,'Imagem & Ação':2,'Sobremesa':2,'Coregrafia':2,'Boardgames':2},
        {'Badminton':5,'Vôlei de grama':2,'Ping pong de mesa':1,'Beer pong':2,'Chute a garrafa':2,'Baralho (Sueca, Truco...)':2,'Videogames':1,'Imagem & Ação':5,'Sobremesa':5,'Coregrafia':2,'Boardgames':3},
        {'Badminton':5,'Vôlei de grama':5,'Ping pong de mesa':5,'Beer pong':4,'Chute a garrafa':5,'Baralho (Sueca, Truco...)':0,'Videogames':5,'Imagem & Ação':3,'Sobremesa':2,'Coregrafia':4,'Boardgames':5},
        {'Badminton':3,'Vôlei de grama':2,'Ping pong de mesa':2,'Beer pong':3,'Chute a garrafa':4,'Baralho (Sueca, Truco...)':3,'Videogames':3,'Imagem & Ação':3,'Sobremesa':2,'Coregrafia':4,'Boardgames':5}
    ]

preferences = [
        {'Lucas Neno':0,'Bruno Mibielli':1,'Pedro Aquino':0,'Paulo Galeão':0,'João Pedro Castro':1,'Duda Magluta':0,'Lucas Tostes':1,'Gabriel Lessa':0,'Felipe Arêas':1,'Patrícia Telles':0,'Tito Labrunie':0,'Ilan Vale':1,'Roberto Soares':0,'Isadora Barretto':0,'Rafael Freitas':1,'Djavan':0,'Morgan Freeman':1,'Luaré':0,'Diogo':0,'Julia':0,'Nicko':0,'Novas pessoas':0},
        {'Lucas Neno':1,'Bruno Mibielli':1,'Pedro Aquino':1,'Paulo Galeão':1,'João Pedro Castro':1,'Duda Magluta':1,'Lucas Tostes':1,'Gabriel Lessa':1,'Felipe Arêas':0,'Patrícia Telles':0,'Tito Labrunie':0,'Ilan Vale':0,'Roberto Soares':1,'Isadora Barretto':1,'Rafael Freitas':1,'Djavan':1,'Morgan Freeman':0,'Luaré':0,'Diogo':0,'Julia':0,'Nicko':0,'Novas pessoas':0},
        {'Lucas Neno':1,'Bruno Mibielli':1,'Pedro Aquino':1,'Paulo Galeão':1,'João Pedro Castro':1,'Duda Magluta':1,'Lucas Tostes':1,'Gabriel Lessa':1,'Felipe Arêas':1,'Patrícia Telles':1,'Tito Labrunie':1,'Ilan Vale':1,'Roberto Soares':1,'Isadora Barretto':1,'Rafael Freitas':1,'Djavan':1,'Morgan Freeman':0,'Luaré':0,'Diogo':0,'Julia':0,'Nicko':0,'Novas pessoas':0},
        {'Lucas Neno':1,'Bruno Mibielli':1,'Pedro Aquino':1,'Paulo Galeão':0,'João Pedro Castro':1,'Duda Magluta':0,'Lucas Tostes':1,'Gabriel Lessa':1,'Felipe Arêas':0,'Patrícia Telles':0,'Tito Labrunie':1,'Ilan Vale':0,'Roberto Soares':1,'Isadora Barretto':1,'Rafael Freitas':1,'Djavan':0,'Morgan Freeman':0,'Luaré':1,'Diogo':1,'Julia':1,'Nicko':1,'Novas pessoas':1},
        {'Lucas Neno':0,'Bruno Mibielli':1,'Pedro Aquino':0,'Paulo Galeão':1,'João Pedro Castro':1,'Duda Magluta':0,'Lucas Tostes':1,'Gabriel Lessa':0,'Felipe Arêas':0,'Patrícia Telles':0,'Tito Labrunie':0,'Ilan Vale':1,'Roberto Soares':0,'Isadora Barretto':0,'Rafael Freitas':1,'Djavan':0,'Morgan Freeman':0,'Luaré':0,'Diogo':0,'Julia':0,'Nicko':0,'Novas pessoas':0},
        {'Lucas Neno':0,'Bruno Mibielli':0,'Pedro Aquino':1,'Paulo Galeão':0,'João Pedro Castro':0,'Duda Magluta':0,'Lucas Tostes':1,'Gabriel Lessa':1,'Felipe Arêas':0,'Patrícia Telles':0,'Tito Labrunie':0,'Ilan Vale':0,'Roberto Soares':1,'Isadora Barretto':1,'Rafael Freitas':1,'Djavan':0,'Morgan Freeman':0,'Luaré':0,'Diogo':0,'Julia':0,'Nicko':0,'Novas pessoas':0},
        {'Lucas Neno':1,'Bruno Mibielli':0,'Pedro Aquino':1,'Paulo Galeão':0,'João Pedro Castro':0,'Duda Magluta':0,'Lucas Tostes':0,'Gabriel Lessa':0,'Felipe Arêas':1,'Patrícia Telles':1,'Tito Labrunie':0,'Ilan Vale':0,'Roberto Soares':1,'Isadora Barretto':1,'Rafael Freitas':1,'Djavan':1,'Morgan Freeman':0,'Luaré':0,'Diogo':0,'Julia':0,'Nicko':0,'Novas pessoas':0},
        {'Lucas Neno':0,'Bruno Mibielli':1,'Pedro Aquino':0,'Paulo Galeão':1,'João Pedro Castro':0,'Duda Magluta':0,'Lucas Tostes':0,'Gabriel Lessa':0,'Felipe Arêas':0,'Patrícia Telles':1,'Tito Labrunie':0,'Ilan Vale':0,'Roberto Soares':1,'Isadora Barretto':0,'Rafael Freitas':1,'Djavan':1,'Morgan Freeman':0,'Luaré':0,'Diogo':0,'Julia':0,'Nicko':0,'Novas pessoas':0},
        {'Lucas Neno':0,'Bruno Mibielli':0,'Pedro Aquino':1,'Paulo Galeão':1,'João Pedro Castro':1,'Duda Magluta':0,'Lucas Tostes':1,'Gabriel Lessa':1,'Felipe Arêas':1,'Patrícia Telles':0,'Tito Labrunie':0,'Ilan Vale':0,'Roberto Soares':0,'Isadora Barretto':1,'Rafael Freitas':0,'Djavan':1,'Morgan Freeman':0,'Luaré':0,'Diogo':0,'Julia':0,'Nicko':0,'Novas pessoas':0},
        {'Lucas Neno':1,'Bruno Mibielli':0,'Pedro Aquino':1,'Paulo Galeão':1,'João Pedro Castro':0,'Duda Magluta':1,'Lucas Tostes':1,'Gabriel Lessa':0,'Felipe Arêas':0,'Patrícia Telles':0,'Tito Labrunie':0,'Ilan Vale':1,'Roberto Soares':0,'Isadora Barretto':0,'Rafael Freitas':1,'Djavan':0,'Morgan Freeman':0,'Luaré':0,'Diogo':0,'Julia':0,'Nicko':0,'Novas pessoas':0},
        {'Lucas Neno':1,'Bruno Mibielli':1,'Pedro Aquino':0,'Paulo Galeão':1,'João Pedro Castro':0,'Duda Magluta':0,'Lucas Tostes':1,'Gabriel Lessa':0,'Felipe Arêas':0,'Patrícia Telles':0,'Tito Labrunie':1,'Ilan Vale':1,'Roberto Soares':0,'Isadora Barretto':0,'Rafael Freitas':1,'Djavan':0,'Morgan Freeman':0,'Luaré':0,'Diogo':0,'Julia':0,'Nicko':0,'Novas pessoas':0},
        {'Lucas Neno':1,'Bruno Mibielli':1,'Pedro Aquino':0,'Paulo Galeão':0,'João Pedro Castro':0,'Duda Magluta':0,'Lucas Tostes':0,'Gabriel Lessa':0,'Felipe Arêas':0,'Patrícia Telles':1,'Tito Labrunie':0,'Ilan Vale':0,'Roberto Soares':1,'Isadora Barretto':1,'Rafael Freitas':1,'Djavan':1,'Morgan Freeman':0,'Luaré':0,'Diogo':0,'Julia':0,'Nicko':0,'Novas pessoas':0},
        {'Lucas Neno':1,'Bruno Mibielli':1,'Pedro Aquino':1,'Paulo Galeão':1,'João Pedro Castro':0,'Duda Magluta':1,'Lucas Tostes':1,'Gabriel Lessa':1,'Felipe Arêas':0,'Patrícia Telles':0,'Tito Labrunie':0,'Ilan Vale':0,'Roberto Soares':0,'Isadora Barretto':0,'Rafael Freitas':1,'Djavan':0,'Morgan Freeman':0,'Luaré':0,'Diogo':0,'Julia':0,'Nicko':0,'Novas pessoas':0},
        {'Lucas Neno':0,'Bruno Mibielli':1,'Pedro Aquino':0,'Paulo Galeão':1,'João Pedro Castro':0,'Duda Magluta':1,'Lucas Tostes':1,'Gabriel Lessa':0,'Felipe Arêas':0,'Patrícia Telles':0,'Tito Labrunie':0,'Ilan Vale':0,'Roberto Soares':1,'Isadora Barretto':1,'Rafael Freitas':1,'Djavan':1,'Morgan Freeman':0,'Luaré':0,'Diogo':0,'Julia':0,'Nicko':0,'Novas pessoas':0},
        {'Lucas Neno':0,'Bruno Mibielli':0,'Pedro Aquino':0,'Paulo Galeão':0,'João Pedro Castro':0,'Duda Magluta':0,'Lucas Tostes':0,'Gabriel Lessa':0,'Felipe Arêas':0,'Patrícia Telles':0,'Tito Labrunie':0,'Ilan Vale':0,'Roberto Soares':0,'Isadora Barretto':0,'Rafael Freitas':0,'Djavan':0,'Morgan Freeman':0,'Luaré':0,'Diogo':0,'Julia':0,'Nicko':0,'Novas pessoas':0},
        {'Lucas Neno':0,'Bruno Mibielli':0,'Pedro Aquino':0,'Paulo Galeão':0,'João Pedro Castro':0,'Duda Magluta':0,'Lucas Tostes':0,'Gabriel Lessa':0,'Felipe Arêas':0,'Patrícia Telles':0,'Tito Labrunie':0,'Ilan Vale':0,'Roberto Soares':0,'Isadora Barretto':0,'Rafael Freitas':0,'Djavan':0,'Morgan Freeman':0,'Luaré':0,'Diogo':0,'Julia':0,'Nicko':0,'Novas pessoas':0}
    ]

history_multiplier = 1

history = [
    {'Lucas Neno':0,'Bruno Mibielli':1,'Pedro Aquino':1,'Paulo Galeão':2,'João Pedro Castro':1,'Duda Magluta':1,'Lucas Tostes':0,'Gabriel Lessa':0,'Felipe Arêas':0,'Patrícia Telles':0,'Tito Labrunie':1,'Ilan Vale':0,'Roberto Soares':0,'Isadora Barretto':1,'Rafael Freitas':1,'Luaré':1},
    {'Lucas Neno':1,'Bruno Mibielli':0,'Pedro Aquino':0,'Paulo Galeão':0,'João Pedro Castro':0,'Duda Magluta':0,'Lucas Tostes':1,'Gabriel Lessa':1,'Felipe Arêas':1,'Patrícia Telles':0,'Tito Labrunie':1,'Ilan Vale':0,'Roberto Soares':0,'Isadora Barretto':0,'Rafael Freitas':0,'Luaré':0},
    {'Lucas Neno':1,'Bruno Mibielli':0,'Pedro Aquino':0,'Paulo Galeão':1,'João Pedro Castro':0,'Duda Magluta':1,'Lucas Tostes':0,'Gabriel Lessa':0,'Felipe Arêas':0,'Patrícia Telles':1,'Tito Labrunie':0,'Ilan Vale':0,'Roberto Soares':0,'Isadora Barretto':0,'Rafael Freitas':1,'Luaré':0},
    {'Lucas Neno':2,'Bruno Mibielli':0,'Pedro Aquino':1,'Paulo Galeão':0,'João Pedro Castro':2,'Duda Magluta':1,'Lucas Tostes':1,'Gabriel Lessa':1,'Felipe Arêas':0,'Patrícia Telles':0,'Tito Labrunie':0,'Ilan Vale':1,'Roberto Soares':0,'Isadora Barretto':1,'Rafael Freitas':0,'Luaré':1},
    {'Lucas Neno':1,'Bruno Mibielli':0,'Pedro Aquino':0,'Paulo Galeão':2,'João Pedro Castro':0,'Duda Magluta':2,'Lucas Tostes':1,'Gabriel Lessa':0,'Felipe Arêas':0,'Patrícia Telles':0,'Tito Labrunie':0,'Ilan Vale':2,'Roberto Soares':0,'Isadora Barretto':1,'Rafael Freitas':1,'Luaré':0},
    {'Lucas Neno':1,'Bruno Mibielli':0,'Pedro Aquino':1,'Paulo Galeão':1,'João Pedro Castro':2,'Duda Magluta':0,'Lucas Tostes':1,'Gabriel Lessa':0,'Felipe Arêas':0,'Patrícia Telles':1,'Tito Labrunie':1,'Ilan Vale':1,'Roberto Soares':0,'Isadora Barretto':0,'Rafael Freitas':1,'Luaré':0},
    {'Lucas Neno':0,'Bruno Mibielli':1,'Pedro Aquino':0,'Paulo Galeão':1,'João Pedro Castro':1,'Duda Magluta':1,'Lucas Tostes':0,'Gabriel Lessa':1,'Felipe Arêas':0,'Patrícia Telles':0,'Tito Labrunie':1,'Ilan Vale':1,'Roberto Soares':0,'Isadora Barretto':0,'Rafael Freitas':0,'Luaré':1},
    {'Lucas Neno':0,'Bruno Mibielli':1,'Pedro Aquino':0,'Paulo Galeão':1,'João Pedro Castro':0,'Duda Magluta':0,'Lucas Tostes':1,'Gabriel Lessa':0,'Felipe Arêas':0,'Patrícia Telles':0,'Tito Labrunie':1,'Ilan Vale':0,'Roberto Soares':0,'Isadora Barretto':0,'Rafael Freitas':0,'Luaré':1},
    {'Lucas Neno':0,'Bruno Mibielli':1,'Pedro Aquino':0,'Paulo Galeão':0,'João Pedro Castro':0,'Duda Magluta':0,'Lucas Tostes':0,'Gabriel Lessa':0,'Felipe Arêas':0,'Patrícia Telles':0,'Tito Labrunie':0,'Ilan Vale':1,'Roberto Soares':0,'Isadora Barretto':0,'Rafael Freitas':2,'Luaré':0},
    {'Lucas Neno':0,'Bruno Mibielli':0,'Pedro Aquino':1,'Paulo Galeão':0,'João Pedro Castro':0,'Duda Magluta':1,'Lucas Tostes':0,'Gabriel Lessa':0,'Felipe Arêas':0,'Patrícia Telles':0,'Tito Labrunie':0,'Ilan Vale':0,'Roberto Soares':0,'Isadora Barretto':0,'Rafael Freitas':1,'Luaré':0},
    {'Lucas Neno':1,'Bruno Mibielli':1,'Pedro Aquino':0,'Paulo Galeão':0,'João Pedro Castro':0,'Duda Magluta':1,'Lucas Tostes':1,'Gabriel Lessa':1,'Felipe Arêas':0,'Patrícia Telles':0,'Tito Labrunie':0,'Ilan Vale':0,'Roberto Soares':0,'Isadora Barretto':0,'Rafael Freitas':0,'Luaré':0},
    {'Lucas Neno':0,'Bruno Mibielli':0,'Pedro Aquino':0,'Paulo Galeão':1,'João Pedro Castro':2,'Duda Magluta':1,'Lucas Tostes':1,'Gabriel Lessa':0,'Felipe Arêas':1,'Patrícia Telles':0,'Tito Labrunie':0,'Ilan Vale':0,'Roberto Soares':0,'Isadora Barretto':0,'Rafael Freitas':0,'Luaré':0},
    {'Lucas Neno':0,'Bruno Mibielli':0,'Pedro Aquino':0,'Paulo Galeão':0,'João Pedro Castro':0,'Duda Magluta':0,'Lucas Tostes':0,'Gabriel Lessa':0,'Felipe Arêas':0,'Patrícia Telles':0,'Tito Labrunie':0,'Ilan Vale':0,'Roberto Soares':0,'Isadora Barretto':0,'Rafael Freitas':0,'Luaré':0},
    {'Lucas Neno':1,'Bruno Mibielli':0,'Pedro Aquino':0,'Paulo Galeão':1,'João Pedro Castro':1,'Duda Magluta':0,'Lucas Tostes':0,'Gabriel Lessa':0,'Felipe Arêas':0,'Patrícia Telles':0,'Tito Labrunie':0,'Ilan Vale':0,'Roberto Soares':0,'Isadora Barretto':0,'Rafael Freitas':0,'Luaré':0},
    {'Lucas Neno':1,'Bruno Mibielli':0,'Pedro Aquino':1,'Paulo Galeão':0,'João Pedro Castro':1,'Duda Magluta':1,'Lucas Tostes':0,'Gabriel Lessa':0,'Felipe Arêas':2,'Patrícia Telles':1,'Tito Labrunie':0,'Ilan Vale':0,'Roberto Soares':0,'Isadora Barretto':0,'Rafael Freitas':0,'Luaré':1},
    {'Lucas Neno':1,'Bruno Mibielli':0,'Pedro Aquino':0,'Paulo Galeão':1,'João Pedro Castro':0,'Duda Magluta':0,'Lucas Tostes':1,'Gabriel Lessa':1,'Felipe Arêas':0,'Patrícia Telles':0,'Tito Labrunie':0,'Ilan Vale':0,'Roberto Soares':0,'Isadora Barretto':0,'Rafael Freitas':1,'Luaré':0},]

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

