from tkinter import *
import vizualizareNote
from database import cur, cur2
import tkinterpp


class AdaugaNote(Frame):
    def submit(self):
        materie = self.master.additionalInfoFrames['Materie']
        codMatricol = self.master.additionalInfoFrames['CodMatricolElev']

        clasa = self.master.additionalInfoFrames['Clasa']
        rows = cur.execute("select id_materie from materie where denumire = '{}'".format(materie))

        id_materie = ''
        for row in rows:
            for elem in row:
                id_materie = elem

        caractereInutile = "(,)'"
        for caracter in caractereInutile:
            self.varProf.set(self.varProf.get().replace(caracter, ""))

        id_profesor = ''
        rows = cur2.execute("SELECT id_profesor FROM PROFESOR WHERE nume || ' ' || prenume = '{}'"
                            .format(self.varProf.get()))
        for row in rows:
            for elem in row:
                id_profesor = elem

        cur2.execute("INSERT INTO INREGISTRARENOTA(nota,data,PC_Materie_ID_Materie, Elev_CodMatricol,PC_ID_Profesor,"
                     "PC_Clasa_Clasa)  VALUES({}, TO_DATE('{}','fmDD-MM-YYYY'), {}, {}, {}, '{}')"
                     .format(self.varNota.get(), self.varData.get(), id_materie, codMatricol, id_profesor, clasa))
        cur2.execute("commit")

    def __init__(self, master):
        Frame.__init__(self, master)

        materie = self.master.additionalInfoFrames['Materie']
        codMatricol = self.master.additionalInfoFrames['CodMatricolElev']
        clasa = self.master.additionalInfoFrames['Clasa']

        self.backButton = Button(self, command=lambda: master.switch_frame(vizualizareNote.VizualizareNote),
                                 text='Back')
        self.backButton.grid(row=0, column=0)

        l1 = Label(self, fg='red', text='Nota', bd=10,
                   font=('Times New Roman', 14, 'bold'))
        l1.grid(row=1, column=1)

        l2 = Label(self, fg='red', text='Data', bd=10,
                   font=('Times New Roman', 14, 'bold'))
        l2.grid(row=1, column=2)

        l3 = Label(self, fg='red', text='Profesor', bd=10,
                   font=('Times New Roman', 14, 'bold'))
        l3.grid(row=1, column=3)

        self.varNota = StringVar()
        self.varData = StringVar()
        self.varProf = StringVar()

        collection = [x for x in range(1, 11)]

        dropNota = OptionMenu(self, self.varNota, *collection)
        dropNota.grid(row=2, column=1)

        eData = tkinterpp.EntryWithPlaceholder(self, textvariable=self.varData, placeholder='DD-MM-YYYY')
        eData.grid(row=2, column=2)

        cur.execute(
            "SELECT p.nume || ' ' || p.prenume FROM profesor p, pc, materie m ,clasa c WHERE p.ID_profesor = pc.Profesor_ID_profesor AND m.ID_materie = pc.Materie_ID_materie AND c.Clasa = pc.Clasa_Clasa AND pc.Clasa_Clasa = '{}' AND m.denumire = '{}'"
                .format(clasa, materie))
        # print('Astia sunt profii: ')
        collection = []
        for row in cur:
            for elem in row:
                collection.append(elem)

        # for elem in collection:
        #     print(elem)

        dropProf = OptionMenu(self, self.varProf, *collection)
        dropProf.grid(row=2, column=3)

        submit_btn = Button(self, text='Adauga nota', command=self.submit, fg='blue',
                            font=('Times New Roman', 12, 'bold'))
        submit_btn.grid(row=2, column=4)
