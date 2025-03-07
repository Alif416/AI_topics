import random
historical_prices = [100, 102, 98, 105, 95, 110, 120, 115, 118, 125] 
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
    initial_capital=1000
    capital=initial_capital

    stop_loss=chromosome[0]/100
    take_profit=chromosome[1]/100
    trade_size=chromosome[2]/100

    position=None  #No Active Trade

    for price in range(len(historical_prices)-1):
        current_price=historical_prices[price]
        next_day_price=historical_prices[price+1]

        if position is None:
            position= (capital * trade_size)/current_price
            entry_price = current_price 

        else:
            change= (next_day_price-current_price)/current_price

            if change<0:
                capital -= capital*trade_size
                if  
                position=None
            elif change>=take_profit:
              capital += (capital*take_profit)
              position=None
    return (capital-initial_capital)








test_chromosome = [20, 45, 30]  # Stop-Loss=10%, Take-Profit=20%, Trade-Size=50%
print("Fitness Score (Profit):", fitness_function(test_chromosome))





