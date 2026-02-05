import numpy as np

# Number of times dice will roll
rolls = 1000

#stimulate dice rolls (value 1 to 6)
dice = np.random.randint(1,7,rolls)

print("Dice Rolls:\n",dice)

#count frequency of each face

for i in range(1,7):
    count = np.sum(dice==i)
    probability = count / rolls

    print(f"Face {i} --> Count: {count}, Probability: {probability:.3f}")