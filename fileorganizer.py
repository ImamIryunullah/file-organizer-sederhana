import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import font

def file_kamu(directory):
    eksitensi = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.pptx', '.xls', '.xlsx'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
        'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
        'Scripts': ['.py', '.js', '.html', '.css', '.php'],
        'Others': [] 
    }

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        if os.path.isdir(filepath):
            continue

        file_ext = os.path.splitext(filename)[1].lower()
        folder_name = 'Others' 
        for category, ext_list in eksitensi.items():
            if file_ext in ext_list:
                folder_name = category
                break

        folder_path = os.path.join(directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        
        shutil.move(filepath, os.path.join(folder_path, filename))

    messagebox.showinfo("Success", "Files have been organized successfully.")

def browse_directory():
    directory = filedialog.askdirectory()
    if directory:
        file_kamu(directory)


root = tk.Tk()
root.title("imam|github")
root.geometry("400x250")
root.config(bg="#f0f0f0")


header_font = font.Font(family="Helvetica", size=14, weight="bold")
button_font = font.Font(family="Helvetica", size=12)


header_label = tk.Label(root, text="Organize Your Files", font=header_font, bg="#f0f0f0", fg="#333")
header_label.pack(pady=20)

instruction_label = tk.Label(root, text="Select a directory to organize your files into categories.", font=button_font, bg="#f0f0f0", fg="#555")
instruction_label.pack(pady=10)

instruction_label = tk.Label(root, text="Pilih direktori file yang ingin kamu kategorikan", font=button_font, bg="#f0f0f0", fg="#555")
instruction_label.pack(pady=10)

browse_button = tk.Button(root, text="Select Directory", font=button_font, command=browse_directory, bg="#4CAF50", fg="white", relief="flat", width=20, height=2)
browse_button.pack(pady=30)

footer_label = tk.Label(root, text="Powered by ImamIryunullah | GitHub", font=("Helvetica", 8), bg="#f0f0f0", fg="#888")
footer_label.pack(side="bottom", pady=10)

root.mainloop()
