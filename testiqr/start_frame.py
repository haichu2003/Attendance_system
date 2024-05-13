import tkinter as tk
from tkinter import ttk

class StartFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self)
        label['text'] = "Start Frame"
        label.grid(row=0, column=4, padx=10, pady=10)

        open_QR_reader_frame = ttk.Button(self)
        open_QR_reader_frame['text'] = "Next Frame"
        open_QR_reader_frame['command'] = lambda : controller.show_frame(1)
        open_QR_reader_frame.grid(row=1, column=1, padx=10, pady=10)
