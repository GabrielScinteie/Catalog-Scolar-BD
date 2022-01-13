from tkinter import *
import elevi
from database import cur
import cx_Oracle


class StergeElevi(Frame):
    def exmatriculeazaElev(self):
        codMatricol = self.master.additionalInfoFrames['CodMatricolElev']
        try:
            cur.execute('savepoint a')
            cur.execute("delete from inregistrarenota where elev_codmatricol = {}".format(codMatricol))
            cur.execute("delete from elev where codmatricol = {}".format(codMatricol))
            cur.execute("commit")
            self.master.switch_frame(elevi.Elevi)
        except cx_Oracle.Error as e:
            cur.execute('rollback to SAVEPOINT a')
            print(e)

    def __init__(self, master):
        Frame.__init__(self, master)

        Label(self, fg='red', text='Sigur?', bd=10,
              font=('Times New Roman', 14, 'bold')).grid(row=1, column=1)

        yesButton = Button(self, command=self.exmatriculeazaElev, width=10, text="Da",
                           fg='blue', font=('Times New Roman', 12, 'bold'))
        yesButton.grid(row=2, column=0)

        noButton = Button(self, command=lambda: master.switch_frame(elevi.Elevi), width=10, text="Nu",
                          fg='blue', font=('Times New Roman', 12, 'bold'))
        noButton.grid(row=2, column=2)
