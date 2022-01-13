from tkinter import *
import catalog
import profesori
import materii
import profesori_clase


class StartPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text="").grid(row=0, column=1)
        self.b1 = Button(self, text='Catalog', fg='blue', font=('Times New Roman', 14, 'bold'),
                         command=lambda: master.switch_frame(catalog.Catalog)).grid(row=1, column=1)
        Label(self, text="").grid(row=2, column=1)
        self.b2 = Button(self, text='Profesori', fg='blue', font=('Times New Roman', 14, 'bold'),
                         command=lambda: master.switch_frame(profesori.Profesori)).grid(row=3, column=1)
        Label(self, text="").grid(row=4, column=1)
        self.b3 = Button(self, text='Materii', fg='blue', font=('Times New Roman', 14, 'bold'),
                         command=lambda: master.switch_frame(materii.Materii)).grid(row=5, column=1)
        Label(self, text="").grid(row=6, column=1)
        self.b4 = Button(self, text='Profesori-Clase', fg='blue', font=('Times New Roman', 14, 'bold'),
                         command=lambda: master.switch_frame(profesori_clase.Profesori_Clase)).grid(row=7, column=1)
        Label(self, text="                              ", font=('Times New Roman', 14, 'bold')).grid(row=8, column=1)
