import pandas as pd
import numpy as np

print("EEWS AI Prototype Started")

# Simulated seismic signal
signal = np.random.normal(0, 1, 1000)

mean_value = np.mean(signal)
std_value = np.std(signal)
max_value = np.max(signal)

print(f"Mean: {mean_value}")
print(f"Standard Deviation: {std_value}")
print(f"Maximum Value: {max_value}")

print("Signal processing completed.")
