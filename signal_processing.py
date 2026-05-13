import numpy as np

def calculate_rms(signal):
    return np.sqrt(np.mean(signal**2))

def zero_crossing_rate(signal):
    return ((signal[:-1] * signal[1:]) < 0).sum()

# Example signal
signal = np.random.normal(0, 1, 1000)

rms = calculate_rms(signal)
zcr = zero_crossing_rate(signal)

print("RMS:", rms)
print("Zero Crossing Rate:", zcr)
