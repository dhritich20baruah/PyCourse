import librosa
import numpy as np
import matplotlib.pyplot as plt

# --------- Load Audio File ---------
file_path = "song.wav"    # change this as needed
y, sr = librosa.load(file_path)

# --------- Extract Pitches ---------
pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
pitch_track = []
for i in range(pitches.shape[1]):
    index = magnitudes[:, i].argmax()
    pitch = pitches[index, i]
    pitch_track.append(pitch)
pitch_track = np.array(pitch_track)

# Keep only non-zero pitches (skip silence)
pitch_track = pitch_track[pitch_track > 0]

# --------- Western Note Conversion ---------
note_names = ['C', 'C#', 'D', 'D#', 'E', 'F',
              'F#', 'G', 'G#', 'A', 'A#', 'B']

def freq_to_western_note(freq):
    if freq <= 0:
        return None
    # Convert freq → MIDI note number
    midi = 69 + 12 * np.log2(freq / 440.0)
    midi_rounded = int(round(midi))
    note = note_names[midi_rounded % 12]
    octave = (midi_rounded // 12) - 1
    return f"{note}{octave}"

# --------- Indian Swara Conversion ---------
# Assuming Sa = C (261.63 Hz). Adjust if needed
SA_FREQ = 261.63

swara_names = ["Sa", "Re", "Ga", "Ma", "Pa", "Dha", "Ni", "Sa (upper)"]
ratios = [1.0, 9/8, 6/5, 4/3, 3/2, 5/3, 15/8, 2.0]  # just intonation ratios

def freq_to_swara(freq):
    if freq <= 0:
        return None
    closest_swara = None
    min_diff = float("inf")
    for ratio, name in zip(ratios, swara_names):
        expected = SA_FREQ * ratio
        diff = abs(freq - expected)
        if diff < min_diff:
            min_diff = diff
            closest_swara = name
    return closest_swara

# --------- Convert first few for preview ---------
print("\nSample Pitch Analysis (first 20 detected pitches):")
for f in pitch_track[:20]:
    western = freq_to_western_note(f)
    swara = freq_to_swara(f)
    print(f"{f:.2f} Hz  -->  {western}  |  {swara}")
