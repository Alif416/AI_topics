# Main Genetic Algorithm loop
def genetic_algorithm(pop_size, generations, mutation_rate):
    population = create_population(pop_size)
    best_route = None
    best_fitness = float('-inf')
    
    for generation in range(generations):
        # Select parents and generate new population
        new_population = []
        
        for _ in range(pop_size):
            parent1, parent2 = tournament_selection(population)
            child = order_crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)
        
        population = new_population
        
        # Find the best solution in the current population
        for route in population:
            current_fitness = fitness(route)
            if current_fitness > best_fitness:
                best_fitness = current_fitness
                best_route = route
                
        print(f"Generation {generation+1}: Best Fitness = {best_fitness}")
    
    return best_route

# Running the genetic algorithm
best_route = genetic_algorithm(pop_size=100, generations=1000, mutation_rate=0.02)

# Plotting the best route
best_route_coords = cities[best_route]
plt.plot(best_route_coords[:, 0], best_route_coords[:, 1], 'o-')
plt.title('Best Route Found by Genetic Algorithm')
plt.show()

# Display the total distance of the best route
print("Best route:", best_route)
print("Total distance:", total_distance(best_route))
