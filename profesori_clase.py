from tkinter import *
import startPage
from database import cur


class Profesori_Clase(Frame):
    def submit(self):

        rows = cur.execute("select id_materie from materie where denumire = '{}'".format(self.varMaterie.get()))
        id_materie = ''
        for row in rows:
            id_materie = row[0]
        print(id_materie)

        rows = cur.execute(
            "select id_profesor from profesor where nume || ' ' || prenume = '{}'".format(self.varProfesor.get()))
        id_profesor = ''
        for row in rows:
            id_profesor = row[0]
        print(id_profesor)

        cur.execute("INSERT INTO PC VALUES({}, {}, '{}')".format(id_materie, id_profesor, self.varClasa.get()))
        cur.execute('commit')

    def __init__(self, master):
        Frame.__init__(self, master)

        self.backButton = Button(self, command=lambda: master.switch_frame(startPage.StartPage), text='Back')
        self.backButton.grid(row=0, column=0)

        Label(self, fg='red', text='Clasa', bd=10,
              font=('Times New Roman', 14, 'bold')).grid(row=1, column=1)

        Label(self, fg='red', text='Materie', bd=10,
              font=('Times New Roman', 14, 'bold')).grid(row=1, column=2)

        Label(self, fg='red', text='Profesor', bd=10,
              font=('Times New Roman', 14, 'bold')).grid(row=1, column=3)

        self.varClasa = StringVar()
        self.varMaterie = StringVar()
        self.varProfesor = StringVar()

        rows = cur.execute("SELECT clasa from clasa order by clasa")
        clase = []
        for row in rows:
            for elem in row:
                clase.append(elem)
        dropProf = OptionMenu(self, self.varClasa, *clase)
        dropProf.grid(row=2, column=1)

        rows = cur.execute("SELECT denumire from materie")
        materii = []
        for row in rows:
            for elem in row:
                materii.append(elem)

        dropProf = OptionMenu(self, self.varMaterie, *materii)
        dropProf.grid(row=2, column=2)

        rows = cur.execute("select nume || ' ' || prenume from profesor")
        nume_prenume = []
        for row in rows:
            for elem in row:
                nume_prenume.append(elem)

        dropProf = OptionMenu(self, self.varProfesor, *nume_prenume)
        dropProf.grid(row=2, column=3)

        submit_btn = Button(self, text='Adauga', command=self.submit, fg='blue', font=('Times New Roman', 12, 'bold'))
        submit_btn.grid(row=2, column=4)
