from tkinter import *
from vizualizareMedii import VizualizareMedii
from actualizareElevi import ActualizeazaElev
from database import cur, cur2
import catalog
import adaugaElevi
import stergeElevi


class Elevi(Frame):
    def actualizeazaElev(self, elev):
        self.master.additionalInfoFrames['CodMatricolElev'] = elev[0]
        self.master.switch_frame(ActualizeazaElev)

    def veziNote(self, elev):
        self.master.additionalInfoFrames['CodMatricolElev'] = elev[0]
        self.master.switch_frame(VizualizareMedii)

    def stergeElev(self, elev):
        self.master.additionalInfoFrames['CodMatricolElev'] = elev[0]
        self.master.switch_frame(stergeElevi.StergeElevi)

    def __init__(self, master):
        Frame.__init__(self, master)

        # print("select * from elev where Clasa_Clasa = '{}'".format(self.master.additionalInfoFrames['Clasa']))
        rows = cur.execute(
            "select * from elev where Clasa_Clasa = '{}'".format(self.master.additionalInfoFrames['Clasa']))

        # code for creating table

        self.backButton = Button(self, command=lambda: master.switch_frame(catalog.Catalog), text='Back')
        self.backButton.grid(row=0, column=0)

        self.add = Button(self, command=lambda: master.switch_frame(adaugaElevi.AdaugaElev), text='Adauga elev',
                          width=10,
                          fg='blue',
                          font=('Times New Roman', 14, 'bold'))
        self.add.grid(row=0, column=4)

        # head-ul tabelului
        self.e = Label(self, fg='red', text='CodMatricol', bd=10,
                       font=('Times New Roman', 14, 'bold'))
        self.e.grid(row=1, column=1)

        self.e = Label(self, fg='red', text='Nume', bd=10,
                       font=('Times New Roman', 14, 'bold'))
        self.e.grid(row=1, column=2)

        self.e = Label(self, fg='red', text='Prenume', bd=10,
                       font=('Times New Roman', 14, 'bold'))
        self.e.grid(row=1, column=3)

        self.e = Label(self, fg='red', text='CNP', bd=10,
                       font=('Times New Roman', 14, 'bold'))
        self.e.grid(row=1, column=4)

        self.e = Label(self, fg='red', text='Email', bd=10,
                       font=('Times New Roman', 14, 'bold'))
        self.e.grid(row=1, column=5)

        self.e = Label(self, fg='red', text='Clasa', bd=10,
                       font=('Times New Roman', 14, 'bold'))
        self.e.grid(row=1, column=6)

        self.e = Label(self, fg='red', text='MedieGenerala', bd=10,
                       font=('Times New Roman', 14, 'bold'))
        self.e.grid(row=1, column=7)

        for (i, result) in enumerate(rows):
            for (j, item) in enumerate(result):
                self.e = Label(self, fg='blue', text=item, bd=4,
                               font=('Times New Roman', 12, 'bold'))
                self.e.grid(row=i + 2, column=j + 1)

            self.button = Button(self, command=lambda elev=result: self.actualizeazaElev(elev), width=10,
                                 text='Actualizeaza', fg='blue',
                                 font=('Times New Roman', 12, 'bold'))
            self.button.grid(row=i + 2, column=len(result) + 2)

            self.button2 = Button(self, command=lambda elev=result: self.veziNote(elev), width=10, text="Medii",
                                  fg='blue', font=('Times New Roman', 12, 'bold'))
            self.button2.grid(row=i + 2, column=len(result) + 3)

            rows2 = cur2.execute(
                "SELECT ROUND(avg(mediiMaterii),2) as Medie "
                "FROM (SELECT e.nume as Nume, e.prenume as Prenume, avg(nota) as mediiMaterii     "
                "from INREGISTRARENOTA i, elev e, pc, materie m "
                "where i.elev_codmatricol = e.codmatricol AND pc.materie_id_materie = m.id_materie AND "
                "pc.materie_id_materie = i.pc_materie_id_materie AND pc.profesor_id_profesor = i.PC_ID_Profesor AND "
                "pc.clasa_clasa = i.pc_clasa_clasa AND e.codmatricol = '{}' "
                "GROUP BY e.nume, e.prenume,m.denumire) "
                "GROUP BY nume, prenume"
                    .format(result[0]))

            medieGen = 0
            for row in rows2:
                medieGen = row[0]

            self.l = Label(self, text=medieGen, fg='blue', font=('Times New Roman', 14, 'bold'))
            self.l.grid(row=i + 2, column=len(result) + 1)

            Button(self, command=lambda elev=result: self.stergeElev(elev), width=10, text='Exmatriculeaza',
                   fg='blue', font=('Times New Roman', 12, 'bold')).grid(row=i + 2, column=len(result) + 4)
