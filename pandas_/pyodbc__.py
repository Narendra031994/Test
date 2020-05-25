import pyodbc 
import pandas as pd

sql_conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=VAMPIRE; DATABASE=covid;   Trusted_Connection=yes')
cur = sql_conn.cursor()
query = "SELECT * from covid_countries;"
df1 = pd.read_sql(query, sql_conn)

 
print(df1.head(2))


data = pd.DataFrame(data = [[10,2],[30,11]],columns = ['col1','col2'],)

for i,row in data.iterrows():
    cur.execute("INSERT INTO copy_data(col1,col2) values(?,?)",(int(row['col1']), int(row['col2'])))
cur.commit()
sql_conn.close()
    
