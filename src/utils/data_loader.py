import os;
import pandas as pd

def read_data_csv(path, filename):
    
    """
    Reads a csv file from the given path and returns a Dataframe
    """
    try:
       return pd.read_csv(os.path.join(path, filename))
    
    except FileNotFoundError as e :
        print("File Not Found. Check the path and filename")
        
    except Exception as e :
        print(f'error reading file {e}')
        

def read_data_xl(path, filename):
    
    """
    Reads an excel file from a given path and returns dataframe
    """
    try:
        return pd.read_excel(os.path.join(path, filename))
        
    except FileNotFoundError as e:
        print("File Not Found. Check the path and filename")
        
    except Exception as e:
        print(f'error reading file {e}')

