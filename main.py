import sqlite3

# create database with timestamp and message
def createDB (cursor) :
    cursor.execute("CREATE TABLE messages (timestamp TEXT, message TEXT)")
    connection.commit()

# read in file and load into database
def loadMessages (cursor, file) :
    for line in file :
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
    for row in data :
        file.write(row[0] + " " + row[1] + "\n")

# connect to temp database connection
connection = sqlite3.connect("")
# create cursor
cursor = connection.cursor()
# create database
createDB(cursor)
# open file
file = open('a.txt', 'r')
# load file into database
loadMessages(cursor, file)
# close file
file.close()
# open file
file = open('b.txt', 'r')
# load file into database
loadMessages(cursor, file)
# close file
file.close()
# # print out all messages
# printMessages(cursor)

#write to file
file = open('c.txt', 'w')
writeMessages(cursor, file)
file.close()

# close connection
connection.close()