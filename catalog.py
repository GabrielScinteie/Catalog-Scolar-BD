from tkinter import *
import startPage
from elevi import Elevi
from database import cur
import adaugaClase


class Catalog(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.backButton = Button(self, command=lambda: master.switch_frame(startPage.StartPage), text='Back')
        self.backButton.grid(row=0, column=0)

        self.adaugaClasa = Button(self, command=lambda: master.switch_frame(adaugaClase.AdaugaClase),
                                  text='Adauga clasa', fg='blue', font=('Times New Roman', 12, 'bold'))
        self.adaugaClasa.grid(row=0, column=2)

        cur.execute('select * from sala order by clasa_clasa')
        self.varClasa = StringVar()

        l = Label(self, text='Clasa', fg='red', font=('Times New Roman', 14, 'bold'))
        l.grid(row=1, column=1)

        l = Label(self, text='Etaj', fg='red', font=('Times New Roman', 14, 'bold'))
        l.grid(row=1, column=2)

        l = Label(self, text='Numar', fg='red', font=('Times New Roman', 14, 'bold'))
        l.grid(row=1, column=3)

        collection = []
        for elem in cur:
            collection.append((elem[0], elem[1], elem[2]))

        for (i, clasa) in enumerate(collection):
            button = Button(self, text=clasa[0], command=lambda clasa=clasa: self.switch_frame_Elevi(clasa), fg='blue',
                            font=('Times New Roman', 12, 'bold'))
            button.grid(row=i + 2, column=1)

            label = Label(self, text=clasa[1], fg='blue', font=('Times New Roman', 12, 'bold')).grid(row=i + 2,
                                                                                                     column=2)
            label = Label(self, text=clasa[2], fg='blue', font=('Times New Roman', 12, 'bold')).grid(row=i + 2,
                                                                                                     column=3)
        cur.execute('select * from clasa order by clasa')

    def switch_frame_Elevi(self, clasa):
        caractereInutile = "(,)'"
        clasa = clasa[0]
        for caracter in caractereInutile:
            clasa = clasa.replace(caracter, "")

        self.master.additionalInfoFrames['Clasa'] = clasa
        self.master.switch_frame(Elevi)
