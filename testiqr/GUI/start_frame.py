import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class StartFrame(tk.Frame):
    def __init__(self, parent, controller, frame_id, is_visible=False):
        tk.Frame.__init__(self, parent)
        self.is_visible = is_visible
        self.controller = controller

        label = ttk.Label(self)
        label['text'] = "Start Frame"
        
        self.filename = None
        choose_file = ttk.Button(self)
        choose_file['text'] = "Choose a file"
        choose_file['command'] =  lambda : [self.open_file()]

        self.foldername = None
        choose_folder = ttk.Button(self)
        choose_folder['text'] = "Open folder"
        choose_folder['command'] = lambda : [self.open_folder()]

        self.course_id = None
        self.course_id_sv = tk.StringVar()
        self.course_id_sv.trace_add("write", self.set_course_id)
        new_course_id = ttk.Label(self, text="Enter course ID:")
        self.course_id_input = ttk.Entry(self, textvariable=self.course_id_sv)

        open_QR_reader_frame = ttk.Button(self)
        open_QR_reader_frame['text'] = "Submit"
        open_QR_reader_frame['command'] = lambda : [self.submit_course()]
        
        # label.grid(row=0, column=4, padx=10, pady=10)
        # open_QR_reader_frame.grid(row=4, column=4, padx=10, pady=10)
        label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        choose_file.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
        choose_folder.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        new_course_id.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
        self.course_id_input.place(relx=0.65, rely=0.65, anchor=tk.CENTER)
        open_QR_reader_frame.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    
    def set_is_visible(self, is_visible):
        self.is_visible = is_visible

    def set_props(self, props):
        self.props = props

    def open_file(self):
        self.foldername = None
        self.course_id = None
        self.filename = filedialog.askopenfilename()
        self.course_id_input.delete(0, tk.END)
        print(self.filename)

    def open_folder(self):
        self.filename = None
        self.foldername = filedialog.askdirectory()
        print(self.foldername)

    def set_course_id(self, var, index, mode):
        self.course_id = self.course_id_sv.get()
        print(f'\"{self.foldername}/{self.course_id}_attendance.csv\"')

    def submit_course(self):
        name = None
        if self.filename: name = self.filename
        else:
            name = f'\"{self.foldername}/{self.course_id}_attendance.csv\"'
        self.set_is_visible(False)
        self.controller.show_frame(1, props={"file":name})
