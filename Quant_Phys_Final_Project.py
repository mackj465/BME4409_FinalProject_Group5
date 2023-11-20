# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 14:01:52 2023

@author: mackj
"""

import cmath
import numpy as np
import matplotlib.pyplot as plt

def calculate_impedance(frequency, resistance, inductance, capacitance):
    omega = 2 * np.pi * frequency
    impedance = resistance + 1j * (omega * inductance - 1 / (omega * capacitance))
    return impedance

# Example values
frequency = 1000  # in Hertz
resistance = 100  # in ohms
inductance = 0.1  # in Henry
capacitance = 0.001  # in Farad

impedance = calculate_impedance(frequency, resistance, inductance, capacitance)

print(f"Impedance: {impedance:.2f} ohms")

# Plot impedance magnitude and phase against frequency
frequency_range = np.array([5, 10, 15, 20, 25, 30, 35])  # Frequency range from 5 to 35 Hz
impedance_values = [calculate_impedance(f, resistance, inductance, capacitance) for f in frequency_range]

plt.figure(figsize=(10, 5))

# Magnitude plot
plt.subplot(1, 2, 1)
plt.plot(frequency_range, np.abs(impedance_values))
plt.title('Impedance Magnitude vs Frequency')
plt.xlabel('Frequency (Hz)')
plt.ylabel('|Z| (ohms)')

# Phase plot
plt.subplot(1, 2, 2)
plt.plot(frequency_range, np.angle(impedance_values, deg=True))
plt.title('Impedance Phase vs Frequency')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (degrees)')

plt.tight_layout()
plt.show()