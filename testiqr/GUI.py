import tkinter as tk
from tkinter import ttk
from QR_reader_frame import QRReaderFrame
from start_frame import StartFrame
from input_frame import InputFrame
from success_frame import SuccessFrame

class AttendanceApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Attendance Tracker")
        self.bind('<Escape>', lambda e: container.quit())
        
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # center the window with respect to user's screen
        self.width = 800
        self.height = 600
        screen_width = container.winfo_screenwidth()
        screen_height = container.winfo_screenheight()
        center_x = int((screen_width - self.width) / 2)
        center_y = int((screen_height - self.height) / 2)
        self.geometry(f'{self.width}x{self.height}+{center_x}+{center_y}')

        self.frames = {}
        frames = [
            StartFrame, 
            QRReaderFrame, 
            InputFrame, 
            SuccessFrame
            ]
        for i in range(len(frames)):
            F = frames[i]
            frame = F(container, self)
            self.frames[i] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
        
        self.show_frame(0)
    
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.set_is_visible(True)
        frame.tkraise()

if __name__ == "__main__":
    app = AttendanceApp()
    app.mainloop()