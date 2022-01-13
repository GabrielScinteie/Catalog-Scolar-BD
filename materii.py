from tkinter import *
import startPage
from database import cur
import adaugaMaterie


class Materii(Frame):
    def adaugaMaterie(self):
        self.master.switch_frame(adaugaMaterie.AdaugaMaterie)

    def __init__(self, master):
        Frame.__init__(self, master)

        self.backButton = Button(self, command=lambda: master.switch_frame(startPage.StartPage), text='Back')
        self.backButton.grid(row=0, column=0)

        self.addButton = Button(self, command=lambda: master.switch_frame(adaugaMaterie.AdaugaMaterie),
                                text='Adauga materie', font=('Times New Roman', 14, 'bold'), fg='blue')
        self.addButton.grid(row=0, column=2)

        cur.execute('select denumire from materie')
        self.varClasa = StringVar()

        Label(self, fg='red', text='Materii', bd=10,
              font=('Times New Roman', 14, 'bold')).grid(row=1, column=1)

        collection = []
        for elem in cur:
            collection.append(elem)

        for (i, materie) in enumerate(collection):
            l = Label(self, fg='blue', text=materie, bd=4,
                      font=('Times New Roman', 12, 'bold'))
            l.grid(row=i + 2, column=1)
