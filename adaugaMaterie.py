from tkinter import *
import materii
from database import cur


class AdaugaMaterie(Frame):
    def submit(self):
        rows = cur.execute("select denumire from materie")
        collection = []
        for row in rows:
            for elem in row:
                collection.append(elem)

        if self.varDenumire.get() not in collection:
            cur.execute("INSERT INTO Materie(denumire) VALUES('{}')".format(self.varDenumire.get()))
            cur.execute('commit')
        else:
            print("Materia deja exista")

    def __init__(self, master):
        Frame.__init__(self, master)

        self.backButton = Button(self, command=lambda: master.switch_frame(materii.Materii), text='Back')
        self.backButton.grid(row=0, column=0)

        l1 = Label(self, fg='red', text='Denumire', bd=10,
                   font=('Times New Roman', 14, 'bold'))
        l1.grid(row=1, column=1)

        self.varDenumire = StringVar()

        eDenumire = Entry(self, textvariable=self.varDenumire)
        eDenumire.grid(row=2, column=1)

        submit_btn = Button(self, text='Adauga materie', command=self.submit, fg='blue',
                            font=('Times New Roman', 12, 'bold'))
        submit_btn.grid(row=2, column=4)
