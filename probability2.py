import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Function to simulate one repetition of the game
def simulate_one_game():
    deck = np.arange(1, 101)  # Create a deck of 100 cards
    np.random.shuffle(deck)  # Shuffle the deck
    hits = np.sum(deck == np.arange(1, 101))  # Count the hits
    return hits

# Function to simulate multiple repetitions of the game
def simulate_multiple_games(num_repetitions):
    total_hits = np.zeros(num_repetitions)
    for i in range(num_repetitions):
        total_hits[i] = simulate_one_game()
    return total_hits

# Set the seed for reproducibility
np.random.seed(42)

# Simulate 10,000 repetitions of the game
num_repetitions = 10000
hits_data = simulate_multiple_games(num_repetitions)

# Calculate expectation and variance
expectation = np.mean(hits_data)
variance = np.var(hits_data)

print('expectations', expectation)
print('variance', variance)

# Plot the distribution of total hits
# plt.figure(figsize=(10, 6))
# sns.histplot(hits_data, bins=range(0, 101), kde=True, color='skyblue')
# plt.title('Distribution of Total Hits in 10,000 Simulations')
# plt.xlabel('Total Hits')
# plt.ylabel('Frequency')
# plt.grid(True)
# plt.show()

# Plot the cumulative distribution function (CDF)
# plt.figure(figsize=(10, 6))
# sns.ecdfplot(hits_data)
# plt.title('Cumulative Distribution of Total Hits')
# plt.xlabel('Total Hits')
# plt.ylabel('Cumulative Probability')
# plt.grid(True)
# plt.show()


plt.figure(figsize=(10, 6))
sns.kdeplot(hits_data, color='skyblue')
plt.title('Kernel Density Estimation (KDE) Plot of Total Hits in 10,000 Simulations')
plt.xlabel('Total Hits')
plt.grid(True)
plt.show()


import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

NUM_SIMULATIONS = 10000
NUM_CARDS = 100

def initialize_deck():
    return list(range(1, NUM_CARDS + 1))

def calculate_variance(results):
    variance_sum = 0
    average_value = sum(results) / len(results)
    for i in range(len(results)):
        variance_sum += np.power(results[i] - average_value, 2)
    return variance_sum / len(results)

# Simulation using numpy
np.random.seed(42)
hits_data = np.zeros(NUM_SIMULATIONS)

for i in range(NUM_SIMULATIONS):
    deck = np.arange(1, NUM_CARDS + 1)
    np.random.shuffle(deck)
    hits_data[i] = np.sum(deck == np.arange(1, NUM_CARDS + 1))

# Calculate expectation and variance using numpy
expectation_np = np.mean(hits_data)
variance_np = np.var(hits_data)

print('Expectation (numpy):', expectation_np)
print('Variance (numpy):', variance_np)

# Simulation using random module
simulation_results = []
mean_values = []
variability_values = []

for i in range(NUM_SIMULATIONS):
    match_counter = 0
    card_deck = initialize_deck()
    random.shuffle(card_deck)

    for j in range(len(card_deck)):
        if (card_deck[j] - 1) == j:
            match_counter += 1

    simulation_results.append(match_counter)
    mean_values.append(np.mean(simulation_results))
    variability_values.append(calculate_variance(simulation_results))

# Calculate expectation and variance using random module
expectation_random = np.mean(simulation_results)
variance_random = np.var(simulation_results)

print('Expectation (random):', expectation_random)
print('Variance (random):', variance_random)

# Plot the average changes over the simulations for both methods
plt.plot(range(1, NUM_SIMULATIONS + 1), mean_values, label='Random Module')
plt.plot(range(1, NUM_SIMULATIONS + 1), hits_data.cumsum() / np.arange(1, NUM_SIMULATIONS + 1), label='Numpy')
plt.xlabel("Number of Simulations")
plt.ylabel("Average")
plt.title("How the Average Changes Over the Simulations")
plt.legend()
plt.savefig('combined_mean_simulation_plot.png', dpi=300, bbox_inches='tight')
plt.show()