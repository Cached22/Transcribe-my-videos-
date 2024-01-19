```python
import os
from datetime import datetime

def generate_file_name(file_path, speaker_data=None):
    """
    Generate a filename for the transcription text file based on the video file name,
    date, or a summary of the content. Optionally include speaker names if provided.

    :param file_path: The path to the video file being processed.
    :param speaker_data: Optional data about speakers to include in the filename.
    :return: A string representing the generated filename.
    """
    base_name = os.path.basename(file_path)
    name_without_ext = os.path.splitext(base_name)[0]
    
    # If speaker data is provided, create a filename that includes the main speaker's name
    if speaker_data and 'main_speaker' in speaker_data:
        main_speaker = speaker_data['main_speaker']
        filename = f"{name_without_ext}_{main_speaker}_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
    else:
        # If no speaker data is provided, just use the current timestamp
        filename = f"{name_without_ext}_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
    
    return filename
```