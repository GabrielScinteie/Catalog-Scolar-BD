from tkinter import *
from database import cur
import elevi
import vizualizareNote
import tkinter.ttk as ttk


class VizualizareMedii(Frame):
    def veziNote(self, materie):
        self.master.additionalInfoFrames['Materie'] = materie
        self.master.switch_frame(vizualizareNote.VizualizareNote)

    def __init__(self, master):
        Frame.__init__(self, master)

        self.backButton = Button(self, command=lambda: master.switch_frame(elevi.Elevi), text='Back')
        self.backButton.grid(row=0, column=0)

        l1 = Label(self, fg='red', text='Materie', bd=10,
                   font=('Times New Roman', 14, 'bold')).grid(row=1, column=1)
        l2 = Label(self, fg='red', text='Medie', bd=10,
                   font=('Times New Roman', 14, 'bold')).grid(row=1, column=2)

        rows = cur.execute(
            "SELECT m.denumire, round(avg(nota)) from INREGISTRARENOTA i, elev e, pc, materie m where i.elev_codmatricol(+) = e.codmatricol AND pc.materie_id_materie(+) = m.id_materie AND pc.materie_id_materie = i.pc_materie_id_materie(+) AND pc.profesor_id_profesor = i.PC_ID_Profesor(+) AND pc.clasa_clasa = i.pc_clasa_clasa(+) AND e.codmatricol = {} AND pc.clasa_clasa = '{}' GROUP BY m.denumire".format(
                master.additionalInfoFrames['CodMatricolElev'], master.additionalInfoFrames['Clasa']
            ))

        for (i, row) in enumerate(rows):
            for (j, camp) in enumerate(row):
                Label(self, fg='blue', text=camp, bd=4,
                      font=('Times New Roman', 12, 'bold')).grid(row=i + 2, column=j + 1)
            Button(self, command=lambda materie=row[0]: self.veziNote(materie),
                   width=10,
                   text='Note', fg='blue',
                   font=('Times New Roman', 12, 'bold')).grid(row=i + 2, column=len(row) + 1)
