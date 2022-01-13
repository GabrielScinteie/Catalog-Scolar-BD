import mainWindow
import database

# create main window
applic = mainWindow.Window()
applic.mainloop()
database.con.close()
database.con2.close()
