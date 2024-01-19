from moviepy.editor import VideoFileClip
import os

def extract_audio(file_path):
    """
    Extracts the audio from the given video file and saves it as a .wav file.

    Args:
    file_path (str): The path to the video file from which to extract audio.

    Returns:
    str: The file path to the extracted audio file.
    """
    try:
        # Load the video file
        video_clip = VideoFileClip(file_path)
        
        # Extract audio from the video clip
        audio_clip = video_clip.audio
        
        # Generate the path for the extracted audio file
        base_name = os.path.basename(file_path)
        file_name, _ = os.path.splitext(base_name)
        audio_file_path = os.path.join('transcripts', f'{file_name}.wav')
        
        # Save the audio clip as a .wav file
        audio_clip.write_audiofile(audio_file_path, codec='pcm_s16le')
        
        # Close the clips to release resources
        audio_clip.close()
        video_clip.close()
        
        return audio_file_path
    except Exception as e:
        print(f"Error extracting audio from {file_path}: {e}")
        return None
