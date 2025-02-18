import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Shashank@2',
    database = "brr"
)

mycursor = mydb.cursor()



limit = "SELECT * FROM employee limit 3 offset 1"
mycursor.execute(limit)
for x in mycursor:
    print(x)

# mycursor.execute('SHOW DATABASES')

# mycursor.execute("USE brr")
# mycursor.execute("SHOW TABLES")
# mycursor.execute("SELECT * FROM employee")


#create an primary key for an exixting table

# mycursor.execute("ALTER TABLE employee ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# sql = "INSERT INTO employee (name, age) VALUES (%s, %s)"
# val = ('test2', 22)

# mycursor.execute(sql, val)

# mydb.commit()
# mycursor.execute("SELECT * FROM employee")
# mycursor.execute("DESC employee")
# mycursor.execute("SELECT * FROM employee WHERE name='shashank'")
# for x in mycursor:
#     print(x)
# result = mycursor.fetchone()
# for x in result:
#     print(x)



# sql = "SELECT * FROM employee WHERE name LIKE '%es%'"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)


# sql = "SELECT * FROM employee WHERE name=%s"
# adr = ("shashank",)
# mycursor.execute(sql, adr)
# result = mycursor.fetchall()

# for x in result:
#     print(x)


# sql = "SELECT * FROM employee ORDER BY name DESC"
# mycursor.execute(sql)
# result = mycursor.fetchall()

# for x in result:
#     print(x)


# sql = "DELETE FROM employee WHERE name='test2'"
# mycursor.execute(sql)
# mydb.commit()
# sql2 = "SELECT * FROM employee"
# mycursor.execute(sql2)
# result = mycursor.fetchall()
# for x in result:
#     print(x)



# sql = "INSERT INTO employee(name, age) VALUES(%s, %s)"
# value = ('HAck', 22)
# mycursor.execute(sql, value)
# mydb.commit()
# sql2 = "Select * from employee"
# mycursor.execute(sql2)
# for x in mycursor:
#     print(x)

# sql = "DELETE FROM  employee WHERE name=%s"
# val = ("Hack",)
# mycursor.execute(sql, val)
# mydb.commit()
# sql2 = "SELECT * FROM employee"
# mycursor.execute(sql2)
# re = mycursor.fetchall()
# for x in re:
#     print(x)


# create = "CREATE TABLE test (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(30))"
# mycursor.execute(create)
# mydb.commit()

# mycursor.execute("Desc test")
# for x in mycursor:
#     print(x)

# delete = "DROP TABLE test "
# mycursor.execute(delete)
# mydb.commit()
# show = "SHOW TABLES"
# mycursor.execute(show)
# for x in mycursor:
    # print(x)

# delete = "DROP TABLE IF EXISTS test"
# mycursor.execute(delete)

# update = "UPDATE employee set name = 'SHASHANK' where name='Shashank'"
# mycursor.execute(update)
# mydb.commit()
# show = "SELECT * FROM employee"
# mycursor.execute(show)
# for x in mycursor:
#     print(x)

# update = "UPDATE employee set name = %s where name=%s"
# input2 = ('shashank','SHASHANK')
# mycursor.execute(update, input2)
# mydb.commit()
# show = "SELECT * FROM employee"
# mycursor.execute(show)
# for x in mycursor:
#     print(x)


# limit = "SELECT * FROM employee limit 1"
# mycursor.execute(limit)
# for x in mycursor:
#     print(x)

