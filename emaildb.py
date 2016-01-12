import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = mbox.txt 

fh = open(fname)

for line in fh :
    if line.startswith('From: ') : 
      pieces = line.split()
      email = pieces[1]
      e1= email.split('.')
	  print e1
	  orgnamelist = email.findall('@\s+',x)
  
	  orgname = orgnamelist[0]
      print (orgname)
      cur.execute('SELECT count FROM Counts WHERE org = ? ', (orgname, ))
      row = cur.fetchone()
      if row is None:
        cur.execute('''INSERT INTO Counts (orgname, count) 
                VALUES ( ?, 1 )''', ( orgname, ) )
      else : 
         cur.execute('UPDATE Counts SET count=count+1 WHERE orgname = ?', 
            (orgname, ))
    # This statement commits outstanding changes to disk each 
    # time through the loop - the program can be made faster 
    # by moving the commit so it runs only after the loop completes
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

print
print ("Counts:")
for row in cur.execute(sqlstr) :
    print (str(row[0]), row[1])

cur.close()

