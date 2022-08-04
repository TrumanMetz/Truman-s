# Import needed libraries (WHERE IS NUMPY?)
import random;
import statistics;

# Make array of 100 random integers.
Rarray = [random.randrange(0, 100,1) for _ in range(100)]

# Get wanted values from array.
maxValue = max(Rarray)
minValue = min(Rarray)
meanValue = statistics.mean(Rarray) 

# Print array and values to console. 
print (Rarray)
print ("The Maximum value is ", maxValue, "The minimum value is ", minValue, "The Average value is ", meanValue)