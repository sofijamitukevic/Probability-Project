import random
import matplotlib.pyplot as plt

def simulate_game():
    deck = list(range(1, 101))
    random.shuffle(deck)
    
    hits = 0
    for i in range(1, 101):
        if deck[i - 1] == i:
            hits += 1
    
    return hits

def simulate_multiple_games(num_simulations):
    total_hits = 0
    hits_list = []

    for _ in range(num_simulations):
        hits = simulate_game()
        total_hits += hits
        average_hits = total_hits / (len(hits_list) + 1)
        hits_list.append(average_hits)

    return hits_list

num_simulations = 10000
hits_over_simulations = simulate_multiple_games(num_simulations)

# Plotting the graph
plt.plot(range(1, num_simulations + 1), hits_over_simulations, label='Average Hits')

plt.xlabel('Number of Simulations')
plt.ylabel('Average Hits')
plt.title('Average Hits Over Simulations')
plt.legend()

plt.show()



