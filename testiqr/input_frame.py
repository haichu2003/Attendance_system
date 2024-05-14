import tkinter as tk
from tkinter import ttk

class InputFrame(tk.Frame):
    def __init__(self, parent, controller, is_visible=False):
        tk.Frame.__init__(self, parent)
        self.is_visible = is_visible

        self.id_label = ttk.Label(self)
        id = -1 # example id, should get from previous reader
        self.id_label['text'] = f'ID: {id}'

        self.name_input_lb = ttk.Label(self)
        self.name_input_lb['text'] = "Your name: "
        name = None
        # get name from database using given ID
        # if not found, ask user to type in their name
        self.name_input_text = tk.Entry(self)
        if not name:
            self.name_input_text.focus_set()
        else:
            self.name_input_text.insert(-1, name)

        self.email_input_lb = ttk.Label(self)
        self.email_input_lb['text'] = "Your email: "
        email = None
        # get email from database using given ID
        # if not found, ask user to type in their email
        self.email_input_text = tk.Entry(self)
        if not email:
            self.email_input_text.focus_set()
        else:
            self.email_input_text.insert(-1, email)

        # button to change pages
        open_previous_frame = ttk.Button(self)
        open_previous_frame['text'] = "Previous Frame"
        open_previous_frame['command'] = lambda : [self.set_is_visible(False), controller.show_frame(1)]

        submit_button = ttk.Button(self)
        submit_button['text'] = "Submit"
        submit_button['command'] = lambda : [self.set_is_visible(False), controller.show_frame(3)]

        self.id_label.grid(row=1, column=1, padx=10, pady=10)
        self.name_input_lb.grid(row=2, column=1, padx=10, pady=10)
        self.name_input_text.grid(row=2, column=2, padx=10, pady=10)
        self.email_input_lb.grid(row=3, column=1, padx=10, pady=10)
        self.email_input_text.grid(row=3, column=2, padx=10, pady=10)
        open_previous_frame.grid(row=4, column=1, padx=10, pady=10)
        submit_button.grid(row=4, column=2, padx=10, pady=10)


    def set_is_visible(self, is_visible):
        self.is_visible = is_visible
    