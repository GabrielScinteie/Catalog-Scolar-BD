from tkinter import *
import profesori
from database import cur


class ActualizeazaProfesor(Frame):
    def submit(self):
        id_profesor = self.master.additionalInfoFrames['id_prof']
        cur.execute("UPDATE profesor SET nume = '{}', prenume = '{}' WHERE id_profesor = {}".format(self.varNume.get(),
                                                                                                    self.varPrenume.get(),
                                                                                                    id_profesor))
        cur.execute('commit')

        self.master.switch_frame(profesori.Profesori)

    def __init__(self, master):
        Frame.__init__(self, master)

        id_profesor = self.master.additionalInfoFrames['id_prof']

        self.backButton = Button(self, command=lambda: master.switch_frame(profesori.Profesori), text='Back')
        self.backButton.grid(row=0, column=0)

        l1 = Label(self, fg='red', text='Nume', bd=10,
                   font=('Times New Roman', 14, 'bold'))
        l1.grid(row=1, column=1)

        l2 = Label(self, fg='red', text='Prenume', bd=10,
                   font=('Times New Roman', 14, 'bold'))
        l2.grid(row=1, column=2)

        # l3 = Label(self, fg='red', text='Materie', bd=10,
        #            font=('Times New Roman', 14, 'bold'))
        # l3.grid(row=1, column=3)

        self.varNume = StringVar()
        self.varPrenume = StringVar()

        cur.execute("select * from profesor where id_profesor = '{}'".format(id_profesor))

        collection = []
        for result in cur:
            for elem in result:
                collection.append(elem)

        for elem in collection:
            print(elem)

        self.varNume.set(collection[1])
        self.varPrenume.set(collection[2])

        eNume = Entry(self, textvariable=self.varNume)
        eNume.grid(row=2, column=1)

        ePrenume = Entry(self, textvariable=self.varPrenume)
        ePrenume.grid(row=2, column=2)

        submit_btn = Button(self, command=self.submit, text='Actualizeaza profesor',
                            fg='blue', font=('Times New Roman', 12, 'bold'))
        submit_btn.grid(row=2, column=3)
