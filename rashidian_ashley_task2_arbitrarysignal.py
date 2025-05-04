"""
This program generates two mathematically defined non-linear signals for an XY oscilloscope display and combines multiple sine waves to create the visualizations in XY mode.
"""
import numpy as np  #import NumPy for creating signals
import matplotlib.pyplot as plt     #import Matplotlib for plotting

t = np.linspace(0, 2 * np.pi, 10000)    #create time vector from 0 to 2pi, 10,000 samples

x = np.sin(3 * t) + 0.5 * np.sin(7 * t)     #create X signal using sine waves
y = np.sin(4 * t + np.pi / 2) + 0.3 * np.sin(10 * t)    #create Y signal using sine waves

#plot X vs Y to simulate oscilloscope XY mode
plt.figure()
plt.plot(x, y)

#label and style plot
plt.title("XY Mode Signal Display")
plt.axis('equal')   #aspect ratio is 1:1
plt.grid(True)
#display final plot
plt.show()
