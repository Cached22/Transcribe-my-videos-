```python
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import threading
from config import settings
from main import process_video_file

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Video File Processor')
        self.geometry('400x200')

        self.folder_path = tk.StringVar(value=settings.folder_to_watch)

        self.create_widgets()

    def create_widgets(self):
        self.folder_label = tk.Label(self, text="Watched Folder:")
        self.folder_label.pack()

        self.folder_entry = tk.Entry(self, textvariable=self.folder_path, width=50)
        self.folder_entry.pack()

        self.browse_button = tk.Button(self, text="Browse", command=self.browse_folder)
        self.browse_button.pack()

        self.start_button = tk.Button(self, text="Start Monitoring", command=self.start_monitoring)
        self.start_button.pack()

        self.stop_button = tk.Button(self, text="Stop Monitoring", command=self.stop_monitoring, state=tk.DISABLED)
        self.stop_button.pack()

        self.status_label = tk.Label(self, text="")
        self.status_label.pack()

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.folder_path.set(folder_selected)
            settings.folder_to_watch = folder_selected

    def start_monitoring(self):
        self.status_label.config(text="Monitoring started...")
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.monitor_thread = threading.Thread(target=self.monitor_folder)
        self.monitor_thread.daemon = True
        self.monitor_thread.start()

    def stop_monitoring(self):
        self.status_label.config(text="Monitoring stopped.")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        if self.monitor_thread.is_alive():
            # Implement logic to stop the monitoring thread
            pass

    def monitor_folder(self):
        # Implement logic to monitor the folder and process new video files
        # This is a placeholder for the actual monitoring logic
        pass

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.stop_monitoring()
            self.destroy()

if __name__ == "__main__":
    app = Application()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
```