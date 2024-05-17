import tkinter as tk
from tkinter import ttk
import time

class SuccessFrame(tk.Frame):
    def __init__(self, parent, controller, frame_id, is_visible=False):
        tk.Frame.__init__(self, parent)
        self.is_visible = is_visible
        self.controller = controller

        label = ttk.Label(self)
        label['text'] = "Attendance recorded successfully"

        return_button = ttk.Button(self)
        return_button['text'] = "Return"
        return_button['command'] = lambda: [self.set_is_visible(False), self.controller.show_frame(1)]
        
        # label.grid(row=3, column=3)
        # return_button.grid(row=4, column=3)
        label.place(relx=0.5, rely=0.47, anchor=tk.CENTER)
        return_button.place(relx=0.5, rely=0.53, anchor=tk.CENTER)

        # self.control_thread = threading.Thread(target=self.success)
        # self.control_thread.start()

        # self.bind("<Escape>", lambda: self.control_thread.join())

        # self.auto_go_back()
    

    def set_is_visible(self, is_visible):
        self.is_visible = is_visible

    def set_props(self, props):
        self.props = props

    def auto_go_back(self):
        if self.is_visible:
            self.set_is_visible(False)
            self.after(500, self.controller.show_frame(1))
        self.auto_go_back()

    # def success(self):
    #     if self.is_visible:
    #         time.sleep(5)
    #         self.set_is_visible(False)
    #         self.controller.show_frame(0)
    #     time.sleep(5)
    #     self.success()
    