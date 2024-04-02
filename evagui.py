from tkinter import Tk, Button, messagebox
import threading
import main  

def start_voice_assistant():
    threading.Thread(target=main.start_voice_assistant, daemon=True).start()

def show_help():
    messagebox.showinfo("Help", "Information about how to use the voice assistant.")

def setup_gui():
    root = Tk()
    root.title("Evaspeech")
    root.geometry("400x300")

    # Start button for EVASpeech
    start_btn = Button(root, text="Start Evaspeech", command=start_voice_assistant)
    start_btn.pack(pady=20)

    # Pause button
    pause_btn = Button(root, text="Pause/Resume Evaspeech", command=main.pause_voice_assistant)
    pause_btn.pack(pady=10)

    # Help button
    help_btn = Button(root, text="Help", command=show_help)
    help_btn.pack(pady=10)

    # Change voice button
    change_voice_btn = Button(root, text="Change Voice", command=main.change_voice)
    change_voice_btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    setup_gui()
