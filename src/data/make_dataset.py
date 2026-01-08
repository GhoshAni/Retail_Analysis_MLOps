# load data in dataframe
def load_retail_df_1():
    """
    loads data in a data frame
    
    """
    retail_df_1 = read_data_csv(path, 'data.csv')
    return retail_df_1

def load_retail_df_2():
    """
    loads data in a data frame
    
    """
    retail_df_2 = read_data_xl(path, 'data.xlsx')
    return retail_df_2