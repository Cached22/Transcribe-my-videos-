# config/settings.py

# Path to the folder being monitored for new video files
FOLDER_TO_WATCH = 'watched_folder/'

# Path where the final transcription files will be saved
TRANSCRIPTS_FOLDER = 'transcripts/'

# Path to the log file
LOG_FILE_PATH = 'logs/processing.log'

# API keys and other sensitive information can be stored here
# For example, if using Whisper API for transcription
# WHISPER_API_KEY = 'your_api_key_here'

# You can also include other settings such as:
# - File formats to watch for
# - Diarization settings like minimum speech duration
# - Transcription language or model settings
# - Any other global settings that might be used across multiple modules

# File formats to watch for
VIDEO_FILE_FORMATS = ['.mp4', '.avi', '.mov']

# Diarization settings
DIARIZATION_MIN_SPEECH_DURATION = 2.0  # seconds

# Transcription settings
TRANSCRIPTION_LANGUAGE = 'en'
TRANSCRIPTION_MODEL = 'base'  # or 'small', 'medium', 'large' depending on the use case

# Ensure that these settings are consistent with the shared dependencies and the application's purpose.