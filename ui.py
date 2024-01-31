import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import main

def upload_file(entry):
    filename = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, filename)

def save_folder(entry):
    foldername = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, foldername)

def start_process(first_file, second_file, output_path, chunksize):
    if not first_file.get() or not second_file.get() or not output_path.get():
        messagebox.showerror("Error", "All file paths must be set before starting the process.")
        return

    main.first_file_path = first_file.get()
    main.second_file_path = second_file.get()
    main.output_path = output_path.get()

    if not chunksize.get():
        main.chunksize = 2000
    else:
        main.chunksize = int(chunksize.get())

    main.run()

    # Update finished_var here
    finished_var.set("Process finished.")

root = tk.Tk()

root.geometry("800x600")

 # First file upload
button1 = tk.Button(root, text="Upload first file", command=lambda: upload_file(entry1), width=20, height=2)
button1.place(relx=0.1, rely=0.2, anchor='w')
label1 = tk.Label(root, text="This should be your current game's players.txt file exported from RDBM using squad file. (Ex: FIFA 19)", wraplength=300)
label1.place(relx=0.4, rely=0.15, anchor='w')
entry1 = tk.Entry(root, width=50)
entry1.place(relx=0.4, rely=0.2, anchor='w')

# Second file upload
button2 = tk.Button(root, text="Upload second file", command=lambda: upload_file(entry2), width=20, height=2)
button2.place(relx=0.1, rely=0.4, anchor='w')
label2 = tk.Label(root, text="This should be target game's players.txt file exported from RDBM using squad file. (Ex: FIFA 23)", wraplength=300)
label2.place(relx=0.4, rely=0.35, anchor='w')
entry2 = tk.Entry(root, width=50)
entry2.place(relx=0.4, rely=0.4, anchor='w')

# Output folder path
button3 = tk.Button(root, text="Choose output folder", command=lambda: save_folder(entry3), width=20, height=2)
button3.place(relx=0.1, rely=0.6, anchor='w')
label3 = tk.Label(root, text="Output folder path")
label3.place(relx=0.4, rely=0.55, anchor='w')
entry3 = tk.Entry(root, width=50)
entry3.place(relx=0.4, rely=0.6, anchor='w')

# Chunk size
label4 = tk.Label(root, text="This defines how many rows will be processed at a time. Higher values will consume more memory. (Default: 2000)", wraplength=300)
label4.place(relx=0.4, rely=0.75, anchor='w')
entry4 = tk.Entry(root, width=50)
entry4.place(relx=0.4, rely=0.8, anchor='w')

# Process finished label
finished_var = tk.StringVar()
finished_label = tk.Label(root, textvariable=finished_var)
finished_label.place(relx=0.5, rely=0.9, anchor='w')

# Start process button
button_start = tk.Button(root, text="Start process", command=lambda: start_process(entry1, entry2, entry3, entry4), width=20, height=2)
button_start.place(relx=0.1, rely=0.9, anchor='w')

root.mainloop()