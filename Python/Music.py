from basic_pitch.inference import predict
import pretty_midi

def pitch_to_note(pitch_number):
    return pretty_midi.note_number_to_name(pitch_number)


# Path to your WAV file
audio_path = "C:\Windows\Media\Ring05.wav" # Make sure it's a WAV file

# Run prediction
model_output, midi_data, note_events = predict(audio_path)

# Sort note events by start time (index 0)
note_events_sorted = sorted(note_events, key=lambda note: note[0])

# Print in order
for start, end, pitch, confidence, _ in note_events_sorted:
    note_name = pitch_to_note(pitch)
    print(f"Note: {note_name}, Start: {start:.2f}s, End: {end:.2f}s, Confidence: {confidence:.2f}")
