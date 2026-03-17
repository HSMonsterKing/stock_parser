import pymssql
"""
使用 pymssql 對資料進行連接
"""
server= "stanleyoreo.database.windows.net"
database = "free-sql-db-9475644" 
user = "dbeng"
password = "Zxcv1234"
'''密碼洩漏問題'''
print("import 成功")

connect = pymssql.connect(server,user,password,database)