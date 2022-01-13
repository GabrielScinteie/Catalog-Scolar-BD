from tkinter import *
import vizualizareMedii
from database import cur
import adaugaNote
import stergeNota


class VizualizareNote(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.backButton = Button(self, command=lambda: master.switch_frame(vizualizareMedii.VizualizareMedii),
                                 text='Back')
        self.backButton.grid(row=0, column=0)

        self.addButton = Button(self, command=self.adaugaNote, text='Adauga nota', width=10,
                                fg='blue', font=('Times New Roman', 12, 'bold'))
        self.addButton.grid(row=0, column=2)

        codMatricol = master.additionalInfoFrames['CodMatricolElev']
        materie = master.additionalInfoFrames['Materie']
        rows = cur.execute(
            "SELECT i.ID_INREGISTRARENOTA,i.nota, i.data from INREGISTRARENOTA i, elev e, pc, materie m where i.elev_codmatricol = e.codmatricol AND pc.materie_id_materie = m.id_materie AND pc.materie_id_materie = i.pc_materie_id_materie AND pc.profesor_id_profesor = i.PC_ID_Profesor AND pc.clasa_clasa = i.pc_clasa_clasa AND e.codmatricol = '{}' AND m.denumire = '{}'"
                .format(codMatricol, materie))

        l1 = Label(self, fg='red', text='Nota', bd=10,
                   font=('Times New Roman', 14, 'bold')).grid(row=1, column=1)
        l2 = Label(self, fg='red', text='Data', bd=10,
                   font=('Times New Roman', 14, 'bold')).grid(row=1, column=2)

        for (i, row) in enumerate(rows):
            for (j, camp) in enumerate(row):
                if j != 0:
                    camp = str(camp)[:10]
                    Label(self, fg='blue', text=camp, bd=4,
                          font=('Times New Roman', 12, 'bold')).grid(row=i + 2, column=j)
            Button(self, command=lambda nota=row: self.stergeNota(nota), width=10, text='Sterge',
                   fg='blue', font=('Times New Roman', 12, 'bold')).grid(row=i + 2, column=len(row))

    def adaugaNote(self):
        self.master.switch_frame(adaugaNote.AdaugaNote)

    def stergeNota(self, nota):
        self.master.additionalInfoFrames['id_nota'] = nota[0]
        self.master.switch_frame(stergeNota.StergeNota)
