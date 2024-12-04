import oracledb
import pandas as pd
from sqlalchemy import create_engine

# connect to oracle database
connection=oracledb.connect(
     user="user",
     password="password",
     dsn="host:port/schema")
# create engine
engine = create_engine('oracle+oracledb://', creator=lambda: connection)
# Get the data into a DataFrame
query = "SELECT * FROM X"
df = pd.read_sql(query, engine)
print(df.describe())