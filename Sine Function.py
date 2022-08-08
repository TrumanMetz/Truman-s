#Import needed libraries
import numpy as np;
import matplotlib.pyplot as plt;
import csv;

#Make arrays to hold values
in_array = np.linspace(-np.pi, np.pi, 100)
out_array = np.sin(in_array)
together = np.stack((in_array, out_array), axis=1) 
header = ['Position', 'Sine Value']
    
#Print values
print("in_array : ", in_array)
print("\nout_array : ", out_array)
print(together)
 
# Plot curve
plt.plot(in_array, out_array, color = 'red', marker = "o")
plt.title("numpy.sin()")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


with open('Sine data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(together)
