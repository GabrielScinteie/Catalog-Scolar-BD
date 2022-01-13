from tkinter import *
from database import cur
import elevi


class ActualizeazaElev(Frame):
    def submit(self):
        caractereInutile = "(,)'"
        for caracter in caractereInutile:
            self.varClasa.set(self.varClasa.get().replace(caracter, ""))

        if self.varNume.get().isalpha() and self.varPrenume.get().isalpha() and len(self.varCNP.get()) == 13:
            print("UPDATE ELEV SET NUME = '{}', PRENUME = '{}', CNP = '{}', EMAIL = '{}', CLASA_CLASA = '{}'".format(
                self.varNume.get(), self.varPrenume.get(), self.varCNP.get(),
                self.varEmail.get(), self.varClasa.get()))

            cur.execute(
                "UPDATE ELEV SET NUME = '{}', PRENUME = '{}', CNP = '{}', EMAIL = '{}', CLASA_CLASA = '{}' WHERE "
                "CODMATRICOL = {}".format(
                    self.varNume.get(), self.varPrenume.get(), self.varCNP.get(),
                    self.varEmail.get(), self.varClasa.get(), self.codMatricol)
            )
            cur.execute("commit")
        else:
            print('Unul dintre campuri nu este valid')

    def __init__(self, master):
        Frame.__init__(self, master)

        self.backButton = Button(self, command=lambda: master.switch_frame(elevi.Elevi), text='Back')
        self.backButton.grid(row=0, column=0)

        l1 = Label(self, fg='red', text='CodMatricol', bd=10,
                   font=('Times New Roman', 14, 'bold'))
        l1.grid(row=1, column=1)

        l2 = Label(self, fg='red', text='Nume', bd=10,
                   font=('Times New Roman', 14, 'bold'))
        l2.grid(row=1, column=2)

        l3 = Label(self, fg='red', text='Prenume', bd=10,
                   font=('Times New Roman', 14, 'bold'))
        l3.grid(row=1, column=3)

        l4 = Label(self, fg='red', text='CNP', bd=10,
                   font=('Times New Roman', 14, 'bold'))
        l4.grid(row=1, column=4)

        l5 = Label(self, fg='red', text='Email', bd=10,
                   font=('Times New Roman', 14, 'bold'))
        l5.grid(row=1, column=5)

        l6 = Label(self, fg='red', text='Clasa', bd=10,
                   font=('Times New Roman', 14, 'bold'))
        l6.grid(row=1, column=6)

        self.varNume = StringVar()
        self.varPrenume = StringVar()
        self.varCNP = StringVar()
        self.varEmail = StringVar()
        self.varClasa = StringVar()

        self.codMatricol = master.additionalInfoFrames['CodMatricolElev']
        cur.execute("select * from elev where CodMatricol = '{}'".format(self.codMatricol))

        collection = []
        for result in cur:
            for elem in result:
                collection.append(elem)

        self.varNume.set(collection[1])
        self.varPrenume.set(collection[2])
        self.varCNP.set(collection[3])
        self.varEmail.set(collection[4])
        self.varClasa.set(collection[5])

        eCod = Label(self, text=self.codMatricol)
        eCod.grid(row=2, column=1)

        eNume = Entry(self, textvariable=self.varNume)
        eNume.grid(row=2, column=2)

        ePrenume = Entry(self, textvariable=self.varPrenume)
        ePrenume.grid(row=2, column=3)

        eCNP = Entry(self, textvariable=self.varCNP)
        eCNP.grid(row=2, column=4)

        eEmail = Entry(self, textvariable=self.varEmail)
        eEmail.grid(row=2, column=5)

        cur.execute('SELECT * from clasa')
        collection = []
        for elem in cur:
            collection.append(elem)

        dropClasa = OptionMenu(self, self.varClasa, *collection)
        dropClasa.grid(row=2, column=6)

        submit_btn = Button(self, text='Actualizeaza', command=self.submit, fg='blue',
                            font=('Times New Roman', 12, 'bold'))
        submit_btn.grid(row=2, column=7)
