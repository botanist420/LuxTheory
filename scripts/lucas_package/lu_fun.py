from inspect import signature



def get_params(fun: callable): 
    
    sig = signature(fun)
    print(sig)


def get_one_arg(fun: callable, arg_name:str):
    
    sig = signature(fun)
    print(sig.parameters[arg_name])
    
    
if __name__ == "__main__":
    print("This script stored all useful functions that I developed...")
    print("Load example test...")
    
    import pandas as pd
    get_params(pd.read_csv)
    print("*"*22*2*2)
    get_one_arg(pd.read_csv, "verbose")