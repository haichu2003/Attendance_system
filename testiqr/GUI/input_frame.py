import tkinter as tk
from tkinter import ttk

class InputFrame(tk.Frame):
    def __init__(self, parent, controller, frame_id, is_visible=False):
        tk.Frame.__init__(self, parent)
        self.is_visible = is_visible
        self.props = None

        wrapper_frame = tk.Frame(self)

        self.id_label = ttk.Label(wrapper_frame)
        self.id = -1 # example id, should get from previous reader

        self.id_label['text'] = "ID"

        self.id_value = ttk.Label(wrapper_frame)
        self.id_value['text'] = self.id

        # get user name and store in self.name
        self.name = None
        self.name_input_lb = ttk.Label(wrapper_frame)
        self.name_input_lb['text'] = "Your name: "
        self.name_sv = tk.StringVar()
        self.name_sv.trace_add('write', self.set_name)
        self.name_input_text = tk.Entry(wrapper_frame, textvariable=self.name_sv)
        
        # get user email and store in self.email
        self.email = None
        self.email_input_lb = ttk.Label(wrapper_frame)
        self.email_input_lb['text'] = "Your email: "
        self.email_sv = tk.StringVar()
        self.email_sv.trace_add('write', self.set_email)
        self.email_input_text = tk.Entry(wrapper_frame, textvariable=self.email_sv)

        # button to change pages
        open_previous_frame = ttk.Button(wrapper_frame)
        open_previous_frame['text'] = "Previous Frame"
        open_previous_frame['command'] = lambda : [
            self.set_is_visible(False), 
            controller.show_frame(frame_id - 1)
            ]

        submit_button = ttk.Button(wrapper_frame)
        submit_button['text'] = "Submit"
        submit_button['command'] = lambda : [
            self.set_is_visible(False),
            self.clear_input(),
            controller.show_frame(frame_id + 1)
            ]

        # grid for multiple items
        self.id_label.grid(row=2, column=2, padx=10, pady=10)
        self.id_value.grid(row=2, column=3, padx=10, pady=10)
        self.name_input_lb.grid(row=3, column=2, padx=10, pady=10)
        self.name_input_text.grid(row=3, column=3, padx=10, pady=10)
        self.email_input_lb.grid(row=4, column=2, padx=10, pady=10)
        self.email_input_text.grid(row=4, column=3, padx=10, pady=10)
        open_previous_frame.grid(row=5, column=2, padx=10, pady=10)
        submit_button.grid(row=5, column=3, padx=10, pady=10)

        # center the wrapper of above items
        wrapper_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def set_name(self, var, index, mode):
        self.name = self.name_sv.get()
        print(self.name)

    def set_email(self, var, index, mode):
        self.email = self.email_sv.get()
        print(self.email)

    def set_is_visible(self, is_visible):
        self.is_visible = is_visible
        # if not is_visible:

    def set_props(self, props):
        self.props = props
        if self.props['id']: 
            print(self.props['id'])
            self.id = self.props['id']
            # get name and email by id here
            self.id_value['text'] = self.id

    def clear_input(self):
        self.name_input_text.delete(0, tk.END)
        self.email_input_text.delete(0, tk.END)

