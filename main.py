import sqlite3

connection = sqlite3.connect("test.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE messages (timestamp TEXT, message TEXT)")
file1 = open('a.txt', 'r')

while True: 
    # Get next line from file
    line = file1.readline()
    # if line is empty
    # end of file is reached
    if not line:
        break
    cursor.execute("INSERT INTO messages VALUES (?, ?)", (line[0:line.find(']  ')+1], line[line.find(']  ')+3:-1]))

connection.commit()

file1.close()
file1 = open('b.txt', 'r')

rows = cursor.execute('SELECT COUNT(*) FROM messages')
print(rows.rowcount)