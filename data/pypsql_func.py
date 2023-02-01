import pandas as pd
from sqlalchemy import create_engine


def gen_engine_url(user_name: str="lucaslee", pwd: str="1234", db_name: str="lucas_db"):
    
    psql_url_string = f"postgresql://{user_name}:{pwd}@localhost:5432/{db_name}"
    
    engine = create_engine(psql_url_string)
    
    return engine


def psql_select(tbl_name: str, engine, limit_rows: int=10):
    
    query_text = f"""
    SELECT *
    FROM "{tbl_name}"
    LIMIT {limit_rows}
    ;
    """
    
    # print(query_text)
    
    df = pd.read_sql_query(query_text, engine)
    return df

if __name__ == "__main__":
    engine = gen_engine_url()
    tbl_name = "curry_stats"
    print(f"Using table: {tbl_name}\n")
    result = psql_select(tbl_name, engine, 5)
    print(result)