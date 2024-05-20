import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

from Add_attendance import AddAttendance

class StartFrame(tk.Frame):
    def __init__(self, parent, controller, frame_id, is_visible=False):
        tk.Frame.__init__(self, parent)
        self.is_visible = is_visible
        self.controller = controller
        self.frame_id = frame_id
        wrapper_frame = tk.Frame(self)

        label = ttk.Label(self)
        label['text'] = "Start Frame"

        self.filename = None
        choose_file = ttk.Button(wrapper_frame)
        choose_file['text'] = "Choose a file"
        choose_file['command'] =  lambda : [self.open_file()]

        self.filename_label = ttk.Label(wrapper_frame)

        self.foldername = None
        choose_folder = ttk.Button(wrapper_frame)
        choose_folder['text'] = "Open folder"
        choose_folder['command'] = lambda : [self.open_folder()]

        self.foldername_label = ttk.Label(wrapper_frame)

        self.course_id = None
        self.course_id_sv = tk.StringVar()
        self.course_id_sv.trace_add("write", self.set_course_id)
        new_course_id = ttk.Label(wrapper_frame, text="Enter course ID:")
        self.course_id_input = ttk.Entry(wrapper_frame, textvariable=self.course_id_sv)

        open_QR_reader_frame = ttk.Button(self)
        open_QR_reader_frame['text'] = "Submit"
        open_QR_reader_frame['command'] = lambda : [self.submit_course()]
        
        label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        choose_file.grid(row=1, column=0, padx=10, pady=10)
        self.filename_label.grid(row=1, column=1, padx=10, pady=10)
        choose_folder.grid(row=2, column=0, padx=10, pady=10)
        self.foldername_label.grid(row=2, column=1, padx=10, pady=10)
        new_course_id.grid(row=3, column=0, padx=10, pady=10)
        self.course_id_input.grid(row=3, column=1, padx=10, pady=10)
        wrapper_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
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
        self.filename_label['text'] = self.filename
        self.foldername_label['text'] = ''

    def open_folder(self):
        self.filename = None
        self.foldername = filedialog.askdirectory()
        print(self.foldername)
        self.foldername_label['text'] = self.foldername
        self.filename_label['text'] = ''

    def set_course_id(self, var, index, mode):
        self.course_id = self.course_id_sv.get()
        print(f'\"{self.foldername}/{self.course_id}_attendance.xlsx\"')

    def submit_course(self):
        name = None
        if self.filename is not None: name = self.filename
        elif self.foldername is None: 
            print('a folder must be chosen')
            return
        elif self.course_id is None: 
            print('you must enter a course id!')
            return
        elif self.foldername is not None and self.course_id is not None:
            name = f'\"{self.foldername}/{self.course_id}_attendance.xlsx\"'
        # check file here
        #
        #
        self.set_is_visible(False)
        self.controller.show_frame(1, props={"file":self.foldername_label})
