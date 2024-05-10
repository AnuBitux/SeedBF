import tkinter as tk
from tkinter import filedialog
import subprocess
import os

def select_file():
    file_path = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def start_tool():
    file_path = file_entry.get()
    text = text_entry.get("1.0", "end-1c")
    if file_path:
        command = f'/opt/Tools/Recovery/SeedBF/sbve/bin/python3 /opt/Tools/Recovery/SeedBF/seedbf.py -p {file_path} -s "{text}"'
        os.system(command)
        root.destroy()

# Create main window
root = tk.Tk()
root.title("Passphrase bruteforce")

# Create widgets
file_label = tk.Label(root, text="Passphrase list:")
file_label.grid(row=0, column=0, padx=10, pady=5)

file_entry = tk.Entry(root, width=50)
file_entry.grid(row=0, column=1, padx=10, pady=5)

select_button = tk.Button(root, text="Select File", command=select_file, bg="black", fg="blue")
select_button.grid(row=0, column=2, padx=10, pady=5)

text_label = tk.Label(root, text="BIP39 mnemonic:")
text_label.grid(row=1, column=0, padx=10, pady=5)

text_entry = tk.Text(root, height=5, width=50)
text_entry.grid(row=1, column=1, padx=10, pady=5, columnspan=2)

start_button = tk.Button(root, text="GO!", command=start_tool, bg="black", fg="blue")
start_button.grid(row=2, column=1, padx=10, pady=5)

# Run the main event loop
root.mainloop()
