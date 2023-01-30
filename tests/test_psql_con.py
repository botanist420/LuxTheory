from sqlalchemy import create_engine
import pandas as pd

#require: sqlalchemy and psycopg2-binary for driver

def con_psql(user_name="adminlucaslee", db_name="lucas_db", tbl_name="persons"):
    
    psql_url = f"postgresql://{user_name}@localhost:5432/{db_name}"
    
    print("This is the URL:\n")
    print(psql_url)
    
    engine = create_engine(psql_url)
    query = f"select * from {tbl_name} limit 20;"
    result = pd.read_sql_query(query, engine)
    print(result)





if __name__ == "__main__":
    input_user = input("your user name: ")
    input_db = input("type the db to connect to postgresql: ")
    input_tbl = input("type the table your want to query: ")
    con_psql(input_user, input_db, input_tbl)