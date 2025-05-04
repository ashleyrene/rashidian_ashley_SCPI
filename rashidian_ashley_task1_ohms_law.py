"""
This program simulates the verification of Ohm’s Law by generating voltage values,
computing their currents through a 1kΩ resistor, and plotting the I-V curve.
It also fits a line to the data and calculates the best fit resistance using linear regression.
"""
import numpy as np      #import NumPy for math functions
import matplotlib.pyplot as plt     #import Matplotlib for plotting
from scipy.stats import linregress  #import linear regression function

voltages = np.arange(0, 5.5, 0.5)  #create array of voltages from 0V to 5V in 0.5V steps
resistance = 1000  #define resistor value 1k ohms
currents = voltages / resistance  #calculate current at each voltage using ohm's law V=IR

#find line of best fit using linear regression
slope, intercept, r_value, p_value, std_err = linregress(voltages, currents)

#plot measured data points
plt.plot(voltages, currents, 'o', label='Measured Data')

#plot best fit line using calculated slope and intercept
plt.plot(voltages, slope * voltages + intercept, '-', label=f'Fit: I={slope:.4f}V + {intercept:.4f}')

#label X and Y axes
plt.xlabel("Voltage (V)")
plt.ylabel("Current (A)")

#add title and grid to plot
plt.title("Ohm's Law: I-V Curve")
plt.grid(True)
plt.legend()

#display plot
plt.show()

#calculate and display best fit resistance
print(f"Best fit resistance: {1/slope:.2f} Ohms")
