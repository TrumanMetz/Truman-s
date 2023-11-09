# This minimalistic tool performs mathematical operations on Data recieved from a Thorlabs Intensity Noise Analyzer (PNA1). 
# Including rescaling the data and plotting it for a different Vdc value and performing integration over the frequency domain. A peakfinder algorithm using scipy was also added to help with further analysis. 
# 
# Disclaimer: This tool assumes the CSV being read is of the same format as those saved by the PNA1. This script will not function properly if any modifactions were made to the CSV beforehand. 
import time
import os
import sys
import scipy as sp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.signal import find_peaks


def main():
    # Grabs and formats data from excel document.

    global Frequency_array
    global PSD_array
    global RIN_array
    global Converted_RIN

    pd.options.display.max_rows = 9999
    DataSheet = pd.read_csv('PNA-10.06.2023 14.27.36.csv',header = None, names = 
                            ['Frequency (Hz)', 'Mag^2 (V^2 / Hz)', 'PSD (dBV^2 / Hz)', 'RIN (dBc / Hz)', 'Integrated Volts RMS', 'Integrated RIN (%RMS)'], 
                            usecols=['Frequency (Hz)','Mag^2 (V^2 / Hz)','PSD (dBV^2 / Hz)','RIN (dBc / Hz)'], skiprows = [0,1,2,3,4,5,6], nrows= 9000)
   
    Frequency_array = DataSheet['Frequency (Hz)']
    PSD_array = DataSheet['PSD (dBV^2 / Hz)']
    RIN_array = DataSheet['RIN (dBc / Hz)']
    Converted_RIN = DataSheet['Mag^2 (V^2 / Hz)']

    print(DataSheet)

    
    plt.figure()
    plt.plot(Frequency_array, RIN_array)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('RIN (dBc / Hz)')
    plt.title('RIN vs Frequency')
    plt.grid()
    plt.show()
    
    # Rescale RIN data using different Vdc values. Set the Vdc value you would like to use here. 
    ##################################################################################
    Vdc_Scaling(.7985)

    # Convert to phase noise. 
    ##################################################################################

    Phase_Noise_array = []

    Slope_of_Descriminator_Curve = 2.0 # Should be in units of V/Hz.
    
    for x in Converted_RIN:
        Phase_Noise_array.append(np.sqrt(x)/Slope_of_Descriminator_Curve)


    plt.figure()
    plt.plot(Frequency_array, Phase_Noise_array)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Phase Noise (Hz / rtHz)')
    plt.title('Phase Noise vs Frequency')
    plt.grid()
    plt.show()

    # Background subtraction. Convert RIN to V^2/Hz then subtract.
    ################################################################################## 
    Background = pd.read_csv('Background-10.06.2023 14.26.38.csv',header = None, names = ['Frequency (Hz)', 'Mag^2 (V^2 / Hz)', 'PSD (dBV^2 / Hz)', 'RIN (dBc / Hz)', 'Integrated Volts RMS', 'Integrated RIN (%RMS)'], usecols=['Frequency (Hz)','Mag^2 (V^2 / Hz)','PSD (dBV^2 / Hz)','RIN (dBc / Hz)'], skiprows = [0,1,2,3,4,5,6], nrows= 9000)

    Background_PSD_array = Background['PSD (dBV^2 / Hz)']

    Background_RIN_array = Background['RIN (dBc / Hz)']


    Converted_RIN_Background = Background['Mag^2 (V^2 / Hz)']

    Actual_RIN_array = []

    for i in range(len(RIN_array)):
         Actual_RIN_array.append(np.absolute(Converted_RIN[i] - Converted_RIN_Background[i])) 

    
    plt.figure()
    plt.plot(Frequency_array, Actual_RIN_array)
    plt.xscale('log')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('RIN (V^2 / Hz)')
    plt.title('RIN vs Frequency')
    plt.grid()
    plt.show()
    


    # Integration of RIN in V^2/Hz from frequency A to B and integration of RIN in V^2/THz from frequency A to B. Change range in for loop to the frequency bounds you want to set.
    ##################################################################################
    Integrated_RIN_array = []
    Sum = 0.0
    Integrated_RIN_array.append(0.0)
    Integrated_rtHz_array = []
    Sum_rtHz = 0.0
    Integrated_rtHz_array.append(0.0)

    for i in range(1, len(Actual_RIN_array)):
        Sum += (Frequency_array[i] + Frequency_array[i-1]) * (Actual_RIN_array[i] - Actual_RIN_array[i - 1]) / 2.0
        Integrated_RIN_array.append(Sum)
        Sum_rtHz += (Frequency_array[i] + Frequency_array[i-1]) * ((np.sqrt(Actual_RIN_array[i]) - np.sqrt(Actual_RIN_array[i - 1])))/ 2.0
        Integrated_rtHz_array.append(Sum_rtHz)

    
    print('Integrated RIN values:\n', Integrated_RIN_array)
    print('Integrated RIN in rtHz:\n', Integrated_rtHz_array)
    
    # Peak finder. Uses the peakfinder algorithm from Scipy. You can change the height of the points considered peaks and the distance between data points of accepted peaks.
    ##################################################################################
    Numpy_array = np.asarray(Actual_RIN_array)

    plt.figure()
    plt.plot(Actual_RIN_array)
    peaks, _ = find_peaks(Actual_RIN_array, height = 10**-9 , distance = 10)
    plt.plot(peaks, Numpy_array[peaks], "X")
    plt.xscale('log')
    plt.xlabel('Counts')
    plt.ylabel('RIN (V^2 / Hz)')
    plt.title('RIN vs Counts')
    plt.grid()
    plt.show()


def Vdc_Scaling (Vdc):
     # Convert PSD back to V^2/Hz then calculate (10^PSD/10), then convert RIN value RINdBc/Hz = 10log(RIN).
    New_Vdc_RIN_array = []
    for x in PSD_array:
        x = 10**(x/10)
        New_Vdc_RIN_array.append( 10*np.log10(x / (Vdc * Vdc)))
        
   
    plt.figure()
    plt.plot(Frequency_array, RIN_array, label = "not scaled")
    plt.plot(Frequency_array, New_Vdc_RIN_array, label = "scaled to new Vdc")
    plt.legend()
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('RIN (dBc / Hz)')
    plt.title('Scaled RIN vs Frequency')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()
