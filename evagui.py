from tkinter import Tk, Button, messagebox
import threading
import main
from main import pause_voice_assistant
from tkinter import Text, END

def start_voice_assistant():
    threading.Thread(target=main.start_voice_assistant, daemon=True).start()

def show_help():
    messagebox.showinfo("EVASpeech help", "For additional guidance please go to evaspeech.com where there are instucted user guides on how to use EVASpeech.")

def quit_eva(root):
    root.destroy() 

def update_transcript(message):
    transcript.config(state='normal')
    transcript.insert(END, message + '\n')
    transcript.config(state='disabled')
    transcript.see(END)

def setup_gui():
    root = Tk()
    root.title("Evaspeech")
    root.geometry("400x450")

    # Configure the color scheme
    root.configure(bg="black")  

    global transcript
    transcript = Text(root, height=10, state='disabled')
    transcript.pack(pady=5)

    # Start button for EVASpeech
    start_btn = Button(root, text="Start Evaspeech", command=start_voice_assistant, bg="#9370DB", fg="white")
    start_btn.pack(pady=20)

    # Pause button
    pause_btn = Button(root, text="Pause/Resume Evaspeech", command=pause_voice_assistant, bg="#9370DB", fg="white")
    pause_btn.pack(pady=10)

    # Help button
    help_btn = Button(root, text="Help", command=show_help, bg="#9370DB", fg="white")
    help_btn.pack(pady=10)

    # Change voice button
    change_voice_btn = Button(root, text="Change Voice", command=main.change_voice, bg="#9370DB", fg="white")
    change_voice_btn.pack(pady=10)

    # Exit button
    quit_eva_btn = Button(root, text="Quit EVASpeech", command=lambda: quit_eva(root), bg="#9370DB", fg="white")
    quit_eva_btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main.set_update_transcript_callback(update_transcript)
    setup_gui()
