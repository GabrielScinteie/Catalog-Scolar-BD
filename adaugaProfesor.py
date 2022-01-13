from tkinter import *
import profesori
from database import cur


class AdaugaProfesor(Frame):
    def submit(self):

        if self.varNume.get().isalpha() and self.varPrenume.get().isalpha():
            cur.execute("INSERT INTO profesor(nume,prenume) VALUES('{}', '{}')".format(self.varNume.get(),
                                                                                       self.varPrenume.get()))
            cur.execute('commit')
        else:
            print('Numele si prenumele pot contine doar litere')

    def __init__(self, master):
        Frame.__init__(self, master)

        self.backButton = Button(self, command=lambda: master.switch_frame(profesori.Profesori), text='Back')
        self.backButton.grid(row=0, column=0)

        l1 = Label(self, fg='red', text='Nume', bd=10,
                   font=('Times New Roman', 14, 'bold'))
        l1.grid(row=1, column=1)

        l2 = Label(self, fg='red', text='Prenume', bd=10,
                   font=('Times New Roman', 14, 'bold'))
        l2.grid(row=1, column=2)

        self.varNume = StringVar()
        self.varPrenume = StringVar()

        eNume = Entry(self, textvariable=self.varNume)
        eNume.grid(row=2, column=1)

        ePrenume = Entry(self, textvariable=self.varPrenume)
        ePrenume.grid(row=2, column=2)

        submit_btn = Button(self, command=self.submit, text='Adauga profesor',
                            fg='blue', font=('Times New Roman', 12, 'bold'))
        submit_btn.grid(row=2, column=3)
