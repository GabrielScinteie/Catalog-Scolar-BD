from tkinter import *
import startPage


class Window(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title = 'Catalog scolar'
        self.frame = None
        self.switch_frame(startPage.StartPage)
        self.additionalInfoFrames = {}

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self.frame is not None:
            self.frame.destroy()
        self.frame = new_frame
        self.frame.pack()
