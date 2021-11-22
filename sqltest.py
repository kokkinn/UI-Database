import sqlite3
# connection = sqlite3.connect('C:\\Users\\kokki\\Desktop\\Solo\\dbdata.db')
# cur = connection.cursor()
# query = 'SELECT 1 FROM info WHERE Name = "Gerorge"'
# # query = 'SELECT COUNT(1) FROM info WHERE Name = "Geeorge"'
# cur.execute(query)
# connection.commit()
# res = cur.fetchall()
# print(res)

password = "12345"
connection = sqlite3.connect('C:\\Users\\kokki\\Desktop\\Solo\\dbdata.db')
cur = connection.cursor()
query = f'SELECT 1 FROM users WHERE password = "{password}"'
cur.execute(query)
connection.commit()
res = cur.fetchall()
if res[0][0] == 1:
    print("UWU")
else:
    print("no")