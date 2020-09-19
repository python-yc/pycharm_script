# -*- coding: utf-8 -*-
import pandas as pd
import pyodbc
import sqlalchemy

# 数据库信息为实际真实
connection = pyodbc.connect('DRIVER=(SQL Server);SERVER=(local);'
                            'DATABASE=AdventureWorks;USER=sa;PASSWORD=123456')

engine = sqlalchemy.create_engine('mssql+pyodbc://sa:123456@(local)/AdventureWorks'
                                  '?driver=SQL+Server')
qurey = "select cout(FirstName) as Count from Person.person where FirstName='Tony'"

# 两个库连接数据库
df1 = pd.read_sql_query(qurey, connection)
df2 = pd.read_sql_query((qurey, engine))

print(df2.head())
