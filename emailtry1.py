import sqlite3 

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()
cur.execute('''
DROP TABLE IF EXISTS Counts''')
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')
fname = "mbox.txt"
fh = open (fname)
for line in fh: 
 if line.startswith('From: '):
    pieces = line.split()
    email = pieces[1]
    email1 = email.split('@')
    email2 = email1[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (email2, ))
    row = cur.fetchone()
    if row is None :
     cur.execute('''INSERT INTO Counts (org, count) 
                VALUES ( ?, 1 )''', ( email2, ) )
    else :
     cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', 
            (email2, ))
 conn.commit()   
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10' 
print ("done")
print ("Counts:")
for row in cur.execute(sqlstr) :
    print (str(row[0]), row[1])

cur.close()   