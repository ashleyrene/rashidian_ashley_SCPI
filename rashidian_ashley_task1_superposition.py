"""
This program simulates the superposition of two sine waves, a 10kHz carrier and 1kHz data wave, to visualize the resulting waveform, a superimposed wave. It plots all three: the carrier, the data, and the superimposed signal.
"""
import numpy as np      #import NumPy for math functions
import matplotlib.pyplot as plt     #import Matplotlib for plotting

t = np.linspace(0, 1e-3, 1000)  #create time axis from 0 to 1 ms, 1000 pts

#define 10 kHz sine wave as carrier signal
carrier = np.sin(2 * np.pi * 10000 * t)
#define 1 kHz sine wave as data signal
data = 0.5 * np.sin(2 * np.pi * 1000 * t)
#add two signals together to form superimposed wave
superimposed = carrier + data

#plot the carrier, data, and superimposed waves
plt.figure()
plt.plot(t * 1000, carrier, label="Carrier Wave")
plt.plot(t * 1000, data, label="Data Wave")
plt.plot(t * 1000, superimposed, label="Superimposed")
#add plot labels and legend
plt.xlabel("Time (ms)")
plt.ylabel("Amplitude")
plt.legend()
plt.title("Superposition of Waves")
plt.grid(True)
#display the plot
plt.show()
