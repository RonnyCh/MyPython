import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully");

conn.execute('CREATE TABLE timesheet (date TEXT, day TEXT, company TEXT, rate TEXT)')
print ("Table created successfully");
conn.close()


#os.chdir(r'c:\Users\r.christianto\SQLiteStudio')
#con = sqlite3.connect("mydatabase")