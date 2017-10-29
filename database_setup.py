import sqlite3

conn = sqlite3.connect('peeps.db')
c = conn.cursor()

c.execute("""CREATE TABLE people(
    id integer primary key,
    fname text,
    lname text,
    relationship text)""")

conn.commit()
c.execute("insert into people(fname, lname, relationship) values('Michelle', 'Wilson', 'Wife')")
conn.commit()
c.execute("insert into people(fname, lname, relationship) values('Janice', 'Goor', 'Mother')")
conn.commit()
c.execute("insert into people(fname, lname, relationship) values('Anthony', 'Wilson', 'Father')")
conn.commit()
c.execute("select * from people")
results = c.fetchall()
for r in results:
    print(r)
conn.close()