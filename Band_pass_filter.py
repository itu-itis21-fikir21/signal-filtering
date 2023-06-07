# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 18:17:42 2023

@author: Dell
"""

import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# Read the audio file
sample_rate, audio_data = wavfile.read('Africa.wav')

b = [2.13554442e-14, 0, -4.27108884e-14, 0, 2.13554442e-14]
a = [  1, -3.86444732,  5.59769624, -3.60203023,  0.86878133]

z1 = 0.0
z2 = 0.0
z3=0.0
z4=0.0
y1 = 0.0
y2 = 0.0
y3 = 0.0
y4 = 0.0

def butterworth_bpf(x):
    global z1, z2, y1, y2, y3, y4
    y = b[0] * x + b[1] * z1 + b[2] * z2 + b[3]*z3 + b[4]*z4 - a[1] * y1 - a[2] * y2 - a[3] * y3 - a[4] * y4
    z2 = z1
    z1 = x
    y4 = y3
    y3 = y2
    y2 = y1
    y1 = y
    return y

# Apply the band-pass filter to the audio data
filtered_audio = np.zeros_like(audio_data, dtype=np.float64)
for i in range(len(audio_data)):
    filtered_audio[i] = butterworth_bpf(float(audio_data[i]))

# Scale the filtered audio to match the original amplitude
max_amplitude = np.max(np.abs(audio_data))
filtered_audio = np.int16(filtered_audio / np.max(np.abs(filtered_audio)) * max_amplitude)

# Save the filtered audio as a new WAV file
wavfile.write('AfricaBPF.wav', sample_rate, filtered_audio)

# Plot the original and filtered signals
t = np.arange(0, len(audio_data) / sample_rate, 1 / sample_rate)
plt.plot(t, audio_data, label='Original')
plt.plot(t, filtered_audio, label='Filtered')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Original vs. Filtered Audio')
plt.legend()
plt.show()