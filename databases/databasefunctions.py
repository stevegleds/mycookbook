'''
This file will contain read only commands to confirm that the example.db is stored on disk and not in memory
'''
import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()
personname = 'joe'
personid = 3
c.execute('''
          INSERT INTO person VALUES(6, 'Joann')
          ''')
# c.execute('''
#           INSERT INTO address VALUES(2, 'steve road', '1', '00000', 1)
#           ''')

conn.commit()
conn.close()