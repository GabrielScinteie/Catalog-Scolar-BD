from tkinter import *
import catalog
from database import cur
import cx_Oracle


class AdaugaClase(Frame):
    def submit(self):
        try:
            # e posibila situatia in care clasa sa fie valida insa sala sa fie ocupata, moment in care s-ar insera
            # o clasa fara sala
            cur.execute('savepoint a')
            cur.execute("INSERT INTO Clasa VALUES('{}')".format(self.varClasa.get()))
            cur.execute("INSERT INTO Sala VALUES('{}',{},{})".format(self.varClasa.get(), self.varEtaj.get(),
                                                                     self.varNrSala.get()))
            cur.execute('commit')
        except cx_Oracle.IntegrityError as e:
            cur.execute('rollback to SAVEPOINT a')
            print(e)

    def __init__(self, master):
        Frame.__init__(self, master)

        self.backButton = Button(self, command=lambda: master.switch_frame(catalog.Catalog), text='Back')
        self.backButton.grid(row=0, column=0)

        l1 = Label(self, fg='red', text='Clasa', bd=10,
                   font=('Times New Roman', 14, 'bold'))
        l1.grid(row=1, column=1)

        l2 = Label(self, fg='red', text='Etaj', bd=10,
                   font=('Times New Roman', 14, 'bold'))
        l2.grid(row=1, column=2)

        l3 = Label(self, fg='red', text='Numar sala', bd=10,
                   font=('Times New Roman', 14, 'bold'))
        l3.grid(row=1, column=3)

        self.varClasa = StringVar()

        eClasa = Entry(self, textvariable=self.varClasa)
        eClasa.grid(row=2, column=1)

        self.varEtaj = StringVar()
        self.varNrSala = StringVar()

        self.varEtaj.set('0')
        self.varNrSala.set('1')

        collection = [0, 1, 2]

        dropEtaj = OptionMenu(self, self.varEtaj, *collection)
        dropEtaj.grid(row=2, column=2)

        collection = [x for x in range(1, 11)]

        dropNrSala = OptionMenu(self, self.varNrSala, *collection)
        dropNrSala.grid(row=2, column=3)

        submit_btn = Button(self, text='Adauga clasa', command=self.submit, fg='blue',
                            font=('Times New Roman', 12, 'bold'))
        submit_btn.grid(row=2, column=4)
