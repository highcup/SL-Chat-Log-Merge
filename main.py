import sqlite3

def createDB (cursor) :
    cursor.execute("CREATE TABLE messages (timestamp TEXT, message TEXT)")
    connection.commit()

def loadMessages (cursor, file) :
    for line in file :
        cursor.execute("INSERT INTO messages VALUES (?, ?)", (line[0:line.find(']  ')+1], line[line.find(']  ')+3:-1]))
    connection.commit()

def printMessages (cursor) :
    data = cursor.execute("SELECT timestamp, message FROM messages").fetchall()
    for row in data :
        print(row[0] + " " + row[1])

connection = sqlite3.connect("")
cursor = connection.cursor()
createDB(cursor)
file = open('a.txt', 'r')
loadMessages(cursor, file)
file.close()
file = open('b.txt', 'r')
loadMessages(cursor, file)
file.close()
printMessages(cursor)
connection.close()