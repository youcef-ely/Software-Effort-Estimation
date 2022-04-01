import numpy as np


def define_missing_values(data):
    return data.replace('?', np.nan)


def drop_missing_values_cols(data, columns_rates, rate):
    #Columns rates is the rate of nan values in each column, we get it from data_visualization module, nan_columns_rates function
    rates = columns_rates
    rates = rates[rates >= rate]
    return data.drop(rates.index, axis = 1)

def drop_missing_values_rows(data, rows_rates, rate):
    #Columns rates is the rate of nan values in each row, we get it from data_visualization module, nan_rows_rates function
    rates = rows_rates
    rates = rates[rates >= rate]
    return data.drop(rates.index)

def missing_values_columns(data):
    sum = data.isna().sum()
    return sum[sum != 0].index

