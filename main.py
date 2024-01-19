```python
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os
import logging
from utils.audio_extraction import extract_audio
from utils.speaker_diarization import diarize_audio
from utils.transcription import transcribe_audio
from utils.file_naming import generate_file_name
from config.settings import folder_to_watch
from utils.save_transcription import save_transcription

class VideoFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return None

        if not event.src_path.endswith('.mp4'):
            return None

        logging.info(f"New video file detected: {event.src_path}")
        process_video_file(event.src_path)

def process_video_file(file_path):
    try:
        audio = extract_audio(file_path)
        speakers = diarize_audio(audio)
        transcriptions = transcribe_audio(audio, speakers)
        filename = generate_file_name(file_path)
        save_transcription(transcriptions, filename)
        logging.info(f"Processed file saved as: {filename}")
    except Exception as e:
        logging.error(f"Failed to process {file_path}: {e}")

def main():
    logging.basicConfig(filename='logs/processing.log', level=logging.INFO)
    path = folder_to_watch
    event_handler = VideoFileHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    logging.info(f"Watching for videos in {path}")

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
```