'''
This file will contain read only commands to confirm that the example.db is stored on disk and not in memory
'''
import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()
c.execute('SELECT * FROM person')
print(c.fetchall())
c.execute('SELECT * FROM address')
print(c.fetchall())


conn.close()