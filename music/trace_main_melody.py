import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# 1. Load the audio file
file_path = "song.wav"   # Change this to your WAV filename
y, sr = librosa.load(file_path)

# 2. Use librosa's piptrack (pitch estimation)
pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

# 3. Extract the dominant pitch at each time frame
pitch_track = []
for i in range(pitches.shape[1]):
    index = magnitudes[:, i].argmax()
    pitch = pitches[index, i]
    pitch_track.append(pitch)

pitch_track = np.array(pitch_track)

# 4. Remove zero values (silence/unvoiced parts)
nonzero_pitches = pitch_track[pitch_track > 0]
times = np.linspace(0, len(y) / sr, num=len(pitch_track))

# 5. Plot the pitch contour
plt.figure(figsize=(12, 5))
plt.plot(times, pitch_track, linewidth=1)
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.title("Pitch Contour (Melody Over Time)")
plt.show()

# Optional: print first few pitch values
print("Sample extracted pitches (Hz):")
print(nonzero_pitches[:20])
