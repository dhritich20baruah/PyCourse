import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

file_path = "song.wav"
y, sr = librosa.load(file_path)

D = np.abs(librosa.stft(y))

DB = librosa.amplitude_to_db(D, ref=np.max)

plt.figure(figsize=(12, 6))
librosa.display.specshow(DB, sr=sr, x_axis='time', y_axis='log', cmap='magma')
plt.colorbar(format="%+2.0f dB")
plt.title("Spectrogram of Song")
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.show()