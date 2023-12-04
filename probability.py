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
 plt.figure(figsize=(10, 6))
 sns.histplot(hits_data, bins=range(0, 101), kde=True, color='skyblue')
 plt.title('Distribution of Total Hits in 10,000 Simulations')
 plt.xlabel('Total Hits')
 plt.ylabel('Frequency')
 plt.grid(True)
 plt.show()

# Plot the cumulative distribution function (CDF)
 plt.figure(figsize=(10, 6))
 sns.ecdfplot(hits_data)
 plt.title('Cumulative Distribution of Total Hits')
 plt.xlabel('Total Hits')
 plt.ylabel('Cumulative Probability')
 plt.grid(True)
 plt.show()



# Plot the distribution of total hits
plt.figure(figsize=(10, 6))
sns.histplot(hits_data, bins=range(0, 101), kde=True, color='skyblue')
plt.title('Distribution of Total Hits in 10,000 Simulations')
plt.xlabel('Total Hits')
plt.ylabel('Probability')
plt.grid(True)
plt.show()



