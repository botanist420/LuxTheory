import pandas as pd
from sqlalchemy import create_engine


def purl(user_name: str="lucaslee", pwd: str="1234", db_name: str="lucas_db"):
    
    psql_url_string = f"postgresql://{user_name}:{pwd}@localhost:5432/{db_name}"
    
    engine = create_engine(psql_url_string)
    
    return engine


def pselect(tbl_name: str, engine, limit_rows: int=10):
    
    query_text = f"""
    SELECT *
    FROM "{tbl_name}"
    LIMIT {limit_rows}
    ;
    """
    # print(query_text)
    
    df = pd.read_sql_query(query_text, engine)
    return df


def df_to_sql(data: pd.DataFrame, name: str, con, index=False, if_exists: str="append"):
    df = data
    print(f"About to use python df export to psql table,\nNew table name will be: {name}\n")
    print("Create and Insert values into PSQL table...")
    
    df.to_sql(name=name, con=con, index=index, if_exists=if_exists)
    
    print("All done!")

if __name__ == "__main__":
    engine = purl()
    tbl_name = "curry_stats"
    print(f"Using table: {tbl_name}\n")
    result = pselect(tbl_name, engine, 5)
    print(result)