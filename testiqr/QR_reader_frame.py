import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class QRReaderFrame(tk.Frame):
    def __init__(self, parent, controller, is_visible=False):
        tk.Frame.__init__(self, parent)
        self.is_visible  = is_visible # check if the frame is visible (i.e. on top of other frames)
        label = ttk.Label(self)
        label['text'] = "QR Reader Frame"
        label.grid(row=0, column=2, padx=10, pady=10)

        open_previous_frame = ttk.Button(self)
        open_previous_frame['text'] = "Previous Frame"
        open_previous_frame['command'] = lambda : [self.set_is_visible(False), controller.show_frame(0)]
        open_previous_frame.grid(row=4, column=3, padx=10, pady=10)

        open_next_frame = ttk.Button(self)
        open_next_frame['text'] = "Next Frame"
        open_next_frame['command'] = lambda : [self.set_is_visible(False), controller.show_frame(2)]
        open_next_frame.grid(row=4, column=4, padx=10, pady=10)

        # initiate Label component to contain camera frame
        self.image_label = ttk.Label(self)
        self.image_label.grid(row=2, rowspan=2, column=2, columnspan=4, padx=10, pady=10)

        # camera frame dimensions
        self.width = 600
        self.height = 400

        # opencv capture with camera
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        self.open_camera()

    
    def set_is_visible(self, is_visible):
        self.is_visible = is_visible
    

    def open_camera(self):
        ret, frame = self.cap.read()
        if not ret: return
        if not self.is_visible:
            # not showing the image read from camera
            # to improve performance
            self.image_label.after(10, lambda : self.open_camera())
            self.image_label.configure(image='')
        else:
            opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) 
            captured_image = Image.fromarray(opencv_image)
            photo_image = ImageTk.PhotoImage(image=captured_image) 
            self.image_label.photo_image = photo_image
            self.image_label.configure(image=photo_image)
            self.image_label.after(10, lambda : self.open_camera())


