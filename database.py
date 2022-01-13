import cx_Oracle

pwd = input('Introdu parola:')

con = cx_Oracle.connect(user="bd046",
                        password=pwd,
                        dsn="bd-dc.cs.tuiasi.ro:1539/orcl")
cur = con.cursor()
con2 = cx_Oracle.connect(user="bd046",
                         password="bd046",
                         dsn="bd-dc.cs.tuiasi.ro:1539/orcl")
cur2 = con2.cursor()
