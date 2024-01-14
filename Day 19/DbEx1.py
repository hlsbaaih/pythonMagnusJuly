from mysql import connector
myDbConnection = connector.connect(host='localhost',user='root',password='Snow',
                                   database='pythonmagnus')
c1 = myDbConnection.cursor()
c1.execute("drop table if exists emp")
c1.execute("create table emp (empno int,ename varchar(20),sal int, deptno int)")
c1.execute("insert into emp values(101,'abc',1000,60)")
c1.execute("insert into emp values(102,'bcd',1200,20)")
or
sql="insert into emp values(%s,%s,%s,%s)"
data = (103,'cde',2000,30)
c1.execute(sql,data)
myDbconnection.commit()
myDbconnection.close()
