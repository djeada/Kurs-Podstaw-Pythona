import random
import math
import matplotlib.pyplot as plt


def box_muller(N):
    Z = []
    for _ in range(N // 2):
        U1 = random.random()
        U2 = random.random()
        Z0 = math.sqrt(-2.0 * math.log(U1)) * math.cos(2.0 * math.pi * U2)
        Z1 = math.sqrt(-2.0 * math.log(U1)) * math.sin(2.0 * math.pi * U2)
        Z.append(Z0)
        Z.append(Z1)
    
    # If N is odd, generate one more number
    if N % 2 != 0:
        U1 = random.random()
        U2 = random.random()
        Z0 = math.sqrt(-2.0 * math.log(U1)) * math.cos(2.0 * math.pi * U2)
        Z.append(Z0)
    
    return Z

# Generate 1000 random numbers using the Box-Muller transform
result_box_muller = box_muller(1000)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.hist(result_box_muller, bins=30, edgecolor='black', alpha=0.7)
plt.title('Histogram of 1000 Random Numbers Generated by Box-Muller Transform')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
