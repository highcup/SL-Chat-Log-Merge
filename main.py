import sqlite3

# create database with timestamp and message
def createDB (cursor) :
    cursor.execute("CREATE TABLE messages (timestamp TEXT, message TEXT)")
    connection.commit()

# read in file and load into database
def loadMessages (cursor, file) :
    with open(file, "r", encoding="utf8") as f :
        for line in f :
            cursor.execute("INSERT INTO messages VALUES (?, ?)", (line[0:line.find(']  ')+1], line[line.find(']  ')+3:-1]))
        connection.commit()

# read in database and print out all rows
def printMessages (cursor) :
    data = cursor.execute("SELECT timestamp, message FROM messages").fetchall()
    for row in data :
        print(row[0] + " " + row[1])

# write messages to file
def writeMessages (cursor, file) :
    data = cursor.execute("SELECT timestamp, message FROM messages").fetchall()
    with open(file, "w", encoding="utf8") as f :
        for row in data :
            f.write(row[0] + " " + row[1] + "\n")

# connect to temp database connection
connection = sqlite3.connect("")
# create cursor
cursor = connection.cursor()
# create database
createDB(cursor)
# load file into database
loadMessages(cursor, "chat.txt")
# load file into database
loadMessages(cursor, "b.txt")
# # print out all messages
# printMessages(cursor)

writeMessages(cursor, "c.txt")
# close connection
connection.close()