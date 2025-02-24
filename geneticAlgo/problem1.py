import random
import numpy as np

# Example data for assets (returns, risk, and correlations)
returns = [0.1, 0.12, 0.14, 0.08, 0.18]  # Expected return for each asset
risks = [0.2, 0.15, 0.25, 0.1, 0.3]  # Standard deviation (risk) for each asset
correlation_matrix = np.array([
    [1.0, 0.2, 0.4, 0.1, 0.3],
    [0.2, 1.0, 0.3, 0.2, 0.4],
    [0.4, 0.3, 1.0, 0.5, 0.6],
    [0.1, 0.2, 0.5, 1.0, 0.3],
    [0.3, 0.4, 0.6, 0.3, 1.0]
])

# Define portfolio parameters
capital = 1.0  # Total available capital
n_assets = len(returns)

# Generate a random individual (portfolio)
def create_individual():
    return [random.randint(0, 1) for _ in range(n_assets)]

# Calculate the portfolio's return
def portfolio_return(individual):
    return sum(individual[i] * returns[i] for i in range(n_assets))

# Calculate the portfolio's risk (standard deviation)
def portfolio_risk(individual):
    selected_assets = [i for i in range(n_assets) if individual[i] == 1]
    if not selected_assets:
        return 0
    risk = 0
    for i in selected_assets:
        for j in selected_assets:
            risk += individual[i] * individual[j] * correlation_matrix[i][j]
    return np.sqrt(risk)

# Fitness function: Maximize return and minimize risk
def fitness(individual):
    total_return = portfolio_return(individual)
    total_risk = portfolio_risk(individual)
    return total_return - 0.5 * total_risk  # Penalizing for high risk

# Tournament selection (select two individuals based on fitness)
def tournament_selection(population):
    tournament = random.sample(population, 5)  # Choose 5 random individuals
    tournament.sort(key=lambda x: fitness(x), reverse=True)
    return tournament[0], tournament[1]  # Return the two best

# Crossover function (single-point crossover)
def crossover(parent1, parent2):
    crossover_point = random.randint(1, n_assets - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

# Mutation function (randomly flip one asset's inclusion)
def mutate(individual, mutation_rate=0.01):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]  # Flip the asset selection
    return individual

# Genetic Algorithm main function
def genetic_algorithm(pop_size, generations, mutation_rate):
    population = [create_individual() for _ in range(pop_size)]
    best_solution = None
    best_fitness = float('-inf')
    
    for generation in range(generations):
        new_population = []
        
        # Generate new population using crossover and mutation
        for _ in range(pop_size):
            parent1, parent2 = tournament_selection(population)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)
        
        population = new_population
        
        # Find the best solution in the current population
        for individual in population:
            current_fitness = fitness(individual)
            if current_fitness > best_fitness:
                best_fitness = current_fitness
                best_solution = individual
        
        print(f"Generation {generation+1}: Best Fitness = {best_fitness}")
    
    return best_solution

# Running the genetic algorithm to optimize portfolio selection
best_portfolio = genetic_algorithm(pop_size=100, generations=1000, mutation_rate=0.02)

# Display the best solution (portfolio)
print("\nBest Portfolio (Assets selected):")
for i, selected in enumerate(best_portfolio):
    if selected == 1:
        print(f"Asset {i+1}: Return = {returns[i]}, Risk = {risks[i]}")

print(f"Total Expected Return = {portfolio_return(best_portfolio)}")
print(f"Total Risk (Standard Deviation) = {portfolio_risk(best_portfolio)}")
