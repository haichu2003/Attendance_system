import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class QRReaderFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self)
        label['text'] = "QR Reader Frame"
        label.grid(row=0, column=4, padx=10, pady=10)
        # label.pack()

        self.width = 600
        self.height = 400
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)

        self.image_label = ttk.Label(self)
        self.image_label.grid(row=1, column=4, padx=10, pady=10)

        open_start_frame = ttk.Button(self)
        open_start_frame['text'] = "Previous Frame"
        open_start_frame['command'] = lambda : controller.show_frame(0)
        open_start_frame.grid(row=2, column=1, padx=10, pady=10)

        open_camera = ttk.Button(self)
        open_camera['text'] = "Open Camera"
        open_camera['command'] = lambda : self.open_camera(cap)
        open_camera.grid(row=2, column=2, padx=10, pady=10)
    
    
    def open_camera(self, cap):
        _, frame = cap.read()
        opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) 
    
        # Capture the latest frame and transform to image 
        captured_image = Image.fromarray(opencv_image) 
    
        # Convert captured image to photoimage 
        photo_image = ImageTk.PhotoImage(image=captured_image) 
    
        # Displaying photoimage in the label 
        self.image_label.photo_image = photo_image 
    
        # Configure image in the self.image_label 
        self.image_label.configure(image=photo_image) 
    
        # Repeat the same process after every 10 seconds 
        self.image_label.after(10, lambda : self.open_camera(cap)) 


