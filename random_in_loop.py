import random
from collections import Counter

# Generate 100 random integers between 1 and 20
random_numbers = [random.randint(1, 20) for _ in range(100)]

# Determine the mode
frequency = Counter(random_numbers)
mode = max(frequency, key=frequency.get)

# Display the result
print("Random Numbers:", random_numbers)
print("Mode (Most Repeating Number):", mode)
print("Frequency of Mode:", frequency[mode])