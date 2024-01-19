# Installation and Usage Guide for "Transcribe my videos"

## Step 1: Clone the Repository
- Open **GitHub Desktop**.
- Navigate to `File > Clone Repository`.
- In the URL tab, paste `https://github.com/WesElliottEFD/Transcribe-my-videos-.git` and choose your desired local path.
- Click on `Clone`.

## Step 2: Open the Project in VS Code
- Right-click on the repository in GitHub Desktop.
- Select `Open in Visual Studio Code`.

## Step 3: Set Up Your Environment
- Ensure Python is installed on your machine.
- Open a terminal in VS Code (`Terminal > New Terminal`).

## Step 4: Install Dependencies
- The project has dependencies listed in `requirements.txt`.
- Run `pip install -r requirements.txt` in the terminal.

## Step 5: Configure Settings
- Edit `config/settings.py` to set paths and other settings such as `FOLDER_TO_WATCH`, `TRANSCRIPTS_FOLDER`.
- Adjust these according to your preferences.

## Step 6: Running the Application
- The main application is in `main.py`.
- Start the application with `python main.py` in the terminal.

## Step 7: Using the GUI (Optional)
- For a GUI, check `ui/interface.py`.
- This script uses Tkinter for a basic graphical interface.

## Step 8: Understand the Functionality
- The app monitors a folder for video files, extracts audio, performs speaker diarization, and transcribes the audio.
- Details are in the `utils` folder (`audio_extraction.py`, `speaker_diarization.py`, `transcription.py`).

## Step 9: Check Logs and Output
- Application logs are in `logs/processing.log`.
- Transcriptions are saved as specified in `config/settings.py`.

## Note
- Ensure correct directory and Python environment when running commands.
- The README in the repository is for a different project; refer to the source code for guidance.


