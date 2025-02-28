import mysql.connector
#mydb = mysql.connector.connect(
#  host = "localhost",
#  user = "root",
#  password = "root",
#  port = 8889  
#)

#print(mydb)

#mycursor = mydb.cursor()
#query = "create database mydatabase"
#mycursor.execute(query)

#query = "show databases"
#mycursor.execute(query)
#for db in mycursor:
#  print(db)
  
  
mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "root",
  port = 8889  ,
  database = "mydatabase"
)

mycursor = mydb.cursor()

def creaTabella():
  query = "create table clienti (id int auto_increment PRIMARY KEY, nome varchar(100), indirizzo varchar(100)  )"
  mycursor.execute(query)


def inserisciValori():
  #print(mydb)

  #query = "create table clienti (id int auto_increment PRIMARY KEY, nome varchar(100), indirizzo varchar(100)  )"
  query = "insert into clienti (nome, indirizzo) values (%s, %s) "
  #val = ("giovanni", "via milano")
  val = [( "alfredo", "via torino"), ( "antonio" , "via napoli" ), ("giovanni", "via roma")]
  #mycursor.execute(query,val)
  mycursor.executemany(query,val)
  mydb.commit()
  print(mycursor.rowcount, "righe inserite")

def leggiValori():
  query = "select * from clienti"
  mycursor.execute(query)
  myresult = mycursor.fetchall()
  for riga in myresult:
    print(riga)

#leggiValori()

def leggiValore():
  query = "select * from clienti"
  mycursor.execute(query)
  myresult = mycursor.fetchone()
  print(myresult)

#leggiValore()

def eliminaValore(val):
  query = "delete from clienti where id = %s"
  mycursor.execute(query,val)
  mydb.commit()
  print(mycursor.rowcount, "righe eliminate!")
  
#eliminaValore((1,))
#leggiValore()

def aggiornaValore(val):
  query = "update clienti set nome = %s where id = %s"
  mycursor.execute(query,val)
  mydb.commit()
  print(mycursor.rowcount, "righe modificate")

#val tupla con 2 valori

#aggiornaValore(("Tommaso",2))
#leggiValori()

def aggiornaValori(val):
  query = "update clienti set nome = %s where id = %s"
  mycursor.executemany(query,val)
  mydb.commit()
  print(mycursor.rowcount, "righe modificate")

piuValori = [("mimmo",2) , ("marco", 5)]
#aggiornaValori(piuValori)
leggiValori()

