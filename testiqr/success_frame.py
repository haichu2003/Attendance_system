import tkinter as tk
from tkinter import ttk
import time

class SuccessFrame(tk.Frame):
    def __init__(self, parent, controller, is_visible=False):
        tk.Frame.__init__(self, parent)
        self.is_visible = is_visible

        label = ttk.Label(self)
        label['text'] = "Attendance recorded successfully"

        return_button = ttk.Button(self)
        return_button['text'] = "Return"
        return_button['command'] = lambda: [self.set_is_visible(False), controller.show_frame(0)]
        
        # label.grid(row=3, column=3)
        # return_button.grid(row=4, column=3)
        label.place(relx=0.5, rely=0.47, anchor=tk.CENTER)
        return_button.place(relx=0.5, rely=0.53, anchor=tk.CENTER)
    

    def set_is_visible(self, is_visible):
        self.is_visible = is_visible
    