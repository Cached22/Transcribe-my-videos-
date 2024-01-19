```python
from pyannote.audio import Pipeline

def diarize_audio(audio_file_path):
    # Initialize the diarization pipeline
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization")

    # Apply the diarization pipeline on the audio file
    diarization = pipeline(audio_file_path)

    # Extract speaker information
    speaker_data = []
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        speaker_info = {
            'speaker_id': speaker,
            'start_time': turn.start,
            'end_time': turn.end
        }
        speaker_data.append(speaker_info)

    return speaker_data
```