import random
popolation_size=4

def create_chromosome():
    return [
        random.randint(1,99),
        random.randint(1,99),
        random.randint(1,99),
    ]

def initialize_population(popolation_size):
    return [create_chromosome() for _ in range(popolation_size)]
def fitness_function(chromosome):
    initial_capital = 1000
    price_changes = [-1.2, 3.4, -0.8, 2.1, -2.5, 1.7, -0.3, 5.8, -1.1, 3.5]

    stop_loss = chromosome[0] / 100
    take_profit = chromosome[1] / 100
    trade_size_percentage = chromosome[2] / 100

    capital = initial_capital

    for change in price_changes:
        trade_size = capital * trade_size_percentage
        profit_loss = trade_size * (change / 100)

        if change <= -stop_loss:
            capital=capital-abs(profit_loss)
        elif change >= take_profit:
            capital=capital+profit_loss

    return (capital - initial_capital)

# Example usage:
chromosome = [2, 5, 20]  # 2% stop-loss, 5% take-profit, 20% trade size
fitness = fitness_function(chromosome)
print(f"The fitness score is: {fitness}")













