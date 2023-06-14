import tkinter as tk
from tkinter import filedialog
import json
import yaml
import os
import xmltodict


def select_input_file():
    filename = filedialog.askopenfilename(filetypes=[('All Files', '*.*')])
    entry_input.delete(0, tk.END)
    entry_input.insert(tk.END, filename)

def select_output_file():
    filename = filedialog.asksaveasfilename(filetypes=[('All Files', '*.*')])
    entry_output.delete(0, tk.END)
    entry_output.insert(tk.END, filename)

root = tk.Tk()

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

lbl_input = tk.Label(frame, text="Plik wejściowy:")
lbl_input.grid(row=0, column=0, sticky='e')

entry_input = tk.Entry(frame, width=50)
entry_input.grid(row=0, column=1)

btn_input = tk.Button(frame, text="Wybierz...", command=select_input_file)
btn_input.grid(row=0, column=2)

lbl_output = tk.Label(frame, text="Plik wyjściowy:")
lbl_output.grid(row=1, column=0, sticky='e')

entry_output = tk.Entry(frame, width=50)
entry_output.grid(row=1, column=1)

btn_output = tk.Button(frame, text="Wybierz...", command=select_output_file)
btn_output.grid(row=1, column=2)

output_format = tk.StringVar(frame)
output_format.set('xml')  # ustawienie domyślnej wartości

lbl_format = tk.Label(frame, text="Format wyjściowy:")
lbl_format.grid(row=2, column=0, sticky='e')

opt_format = tk.OptionMenu(frame, output_format, 'xml', 'json', 'yaml')
opt_format.grid(row=2, column=1, sticky='w')

btn_convert = tk.Button(frame, text="Konwertuj", command=convert_files)
btn_convert.grid(row=3, column=1, pady=10)

root.mainloop()