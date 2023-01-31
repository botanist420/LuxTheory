import pandas as pd
from sqlalchemy import create_engine


input_path = "titanic.csv"

psql_url = "postgresql://lucaslee@localhost:5432/lucas_db"

engine = create_engine(psql_url)
print("Connect engine successfully!!!")

df_example = pd.read_csv(input_path)

df_example.to_sql(name="titanic", con=engine, index=False, if_exists="append")

print("Bye Lucas")