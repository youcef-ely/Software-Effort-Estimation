import pandas as pd
def read_data(file_name, sheet_name = 0, header = 0):
    return pd.read_excel('C:/Users/User/Desktop/INSEA/MFE/Software Cost Estimation Project/Data/'+file_name+'.xlsx', sheet_name= sheet_name, header = header)

def save_data(df, file_name):
    df.to_excel('C:/Users/User/Desktop/INSEA/MFE/Software Cost Estimation Project/Data/'+file_name+'.xlsx')


