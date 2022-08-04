# Import needed libraries (WHERE IS NUMPY?)
import random;
import statistics;

# Make array of 100 random integers.
Rarray = [random.randrange(0, 100,1) for _ in range(100)]

# Make Median function
def get_median(Rarray):
    ar_sorted = Rarray.sort()

    if len(Rarray) % 2 !=0:
        median = int((len(Rarray)+1)/2 - 1)
        return Rarray[median]
    else:
        median1 = int(len(Rarray)/2 - 1)
        median2 = int(len(Rarray)/2)
        return (Rarray[median1] + Rarray[median2])/2


# Get wanted values from array.
maxValue = max(Rarray)
minValue = min(Rarray)
meanValue = statistics.mean(Rarray) 


# Print array and values to console. 
print (Rarray)
print ("The Maximum value is ", maxValue, "The minimum value is ", minValue, "The Average value is ", meanValue, "The Median value is", get_median(Rarray))