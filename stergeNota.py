from tkinter import *
from database import cur
import vizualizareNote


class StergeNota(Frame):

    def exmatriculeazaElev(self):
        id_nota = self.master.additionalInfoFrames['id_nota']
        cur.execute("delete from inregistrarenota where id_inregistrarenota = {}".format(id_nota))
        cur.execute("commit")
        self.master.switch_frame(vizualizareNote.VizualizareNote)

    def __init__(self, master):
        Frame.__init__(self, master)

        Label(self, fg='red', text='Sigur?', bd=10,
              font=('Times New Roman', 14, 'bold')).grid(row=1, column=1)

        yesButton = Button(self, command=self.exmatriculeazaElev, width=10, text="Da",
                           fg='blue', font=('Times New Roman', 12, 'bold'))
        yesButton.grid(row=2, column=0)

        noButton = Button(self, command=lambda: master.switch_frame(vizualizareNote.VizualizareNote), width=10,
                          text="Nu",
                          fg='blue', font=('Times New Roman', 12, 'bold'))
        noButton.grid(row=2, column=2)
