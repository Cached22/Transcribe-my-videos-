from whisper import Whisper
import logging
from utils.speaker_diarization import diarize_audio
from config.settings import WHISPER_MODEL

# Initialize Whisper model
model = Whisper.load_model(WHISPER_MODEL)

def transcribe_audio(audio_path, speaker_data):
    """
    Transcribes the audio using Whisper and integrates speaker diarization data.
    
    :param audio_path: Path to the audio file to be transcribed.
    :param speaker_data: Speaker diarization information.
    :return: A list of tuples containing speaker ID and the corresponding transcription.
    """
    transcriptions = []
    try:
        # Load the audio file
        audio = model.load_audio(audio_path)
        # Split the audio into chunks based on speaker_data
        for speaker_id, (start_time, end_time) in speaker_data.items():
            # Extract the audio chunk for the current speaker
            audio_chunk = audio[int(start_time * model.sample_rate):int(end_time * model.sample_rate)]
            # Transcribe the audio chunk
            result = model.transcribe(audio_chunk)
            # Append the speaker ID and transcription to the list
            transcriptions.append((speaker_id, result['text']))
    except Exception as e:
        logging.error(f"Error transcribing audio: {e}")
        raise e

    return transcriptions

def integrate_diarization_transcription(speaker_data, transcriptions):
    """
    Integrates the speaker diarization data with the transcriptions.
    
    :param speaker_data: Speaker diarization information.
    :param transcriptions: List of transcriptions with speaker IDs.
    :return: Combined transcription with speaker labels.
    """
    combined_transcription = ""
    for speaker_id, transcription in transcriptions:
        combined_transcription += f"Speaker {speaker_id}: {transcription}\n"
    return combined_transcription

# Example usage:
# speaker_data = diarize_audio('path/to/extracted_audio.wav')
# transcriptions = transcribe_audio('path/to/extracted_audio.wav', speaker_data)
# combined_transcription = integrate_diarization_transcription(speaker_data, transcriptions)