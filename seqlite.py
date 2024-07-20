import sqlite3
connection=sqlite3.connect("tudent.db")
cursor  = connection.cursor()

tableinfo='''
create table student(name varchar(255),class varchar(55),section varchar(55))
'''

cursor.execute(tableinfo)

cursor.execute('''insert into student values ('sonu','6','v')''')
cursor.execute('''insert into student values ('sofy','7','b')''')
cursor.execute('''insert into student values ('sona','5','c')''')
cursor.execute('''insert into student values ('soum','6','c')''')
cursor.execute('''insert into student values ('soham','3','d')''')

print("the code is exceuted")
data = cursor.execute('''select * from student''')
for row in data:
    print (row)