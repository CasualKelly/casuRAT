#!python3

import sqlite3

conn = sqlite3.connect('casuRAT.db')
c = conn.cursor()
c.execute('''CREATE TABLE HISTORY([client_ip] text, [utc_time] text, [command_ran] text, [output])''')
conn.commit