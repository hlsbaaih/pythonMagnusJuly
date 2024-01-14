from mysql import connector
myDbConnection = connection.connector('host='localhost',user='root',password='Snow',
                                                                database='Pythonmagnus')
c1 = connection.cursor()
c1.execute("select * from emp where deptno=10")
for i in result
    print(i)


myDbconnection.close()




