import oracledb
import pandas as pd
from sqlalchemy import create_engine
import configparser

#get database properties
config = configparser.RawConfigParser()
config.read('config/sql_datasource.properties')

# connect to oracle database
connection=oracledb.connect(
     user=config.get("oracle", "database_user"),
     password=config.get("oracle", "database_password"),
     dsn=config.get("oracle", "database_dsn"))
# create engine
engine = create_engine('oracle+oracledb://', creator=lambda: connection)
# Get the data into a DataFrame
query = "SELECT * FROM Person"
df = pd.read_sql(query, engine)
print(df.describe())