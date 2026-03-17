import pymssql
"""
使用 pymssql 對資料進行連接
"""
server= "stanleyoreo.database.windows.net"
database = "free-sql-db-9475644" 
user = "dbeng"
password = "Zxcv1234"
'''密碼洩漏問題'''
"""
資料表建立 DDL:


CREATE TABLE [dbo].[stocks] (
    [Id]    INT             IDENTITY (1, 1) NOT NULL,
    [sid]   CHAR (4)        NOT NULL,
    [sname] VARBINARY (30)  NOT NULL,
    [price] DECIMAL (16, 2) NOT NULL,
    [pdate] DATETIME        CONSTRAINT [DEFAULT_stocks_pdate] DEFAULT GETDATE() NOT NULL,
    CONSTRAINT [PK_stocks] PRIMARY KEY CLUSTERED ([Id] ASC)
);

"""

connect = pymssql.connect(server,user,password,database)