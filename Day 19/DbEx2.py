from mysql import connector
myDbConnection = connector.connect(host='localhost',user='root',password='Snow',
                                   database='Pythonmagnus')
c1 = myDbConnection.cursor()
vempno = int(input("Enter the Empno value: "))
vename = input("Enter the Ename value: ")
vsal = int(input("Enter the value of sal value: "))
vdeptno = int(input("Enter the value of dept value: "))

c1.execute("insert into emp (empno,ename,sal,deptno),values(%s,%s,%s,%s)",(vempno,vename,vsal,vdeptno))

myDbConnection.commit()
myDbConnection.close()
