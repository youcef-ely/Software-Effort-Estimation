import sys
import os

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path+"\\src")

import data_visualization

import numpy as np


def define_missing_values(data):
    return data.replace('?', np.nan)


def drop_missing_values_cols(data, rate):
    rates = data_visualization.nan_columns_rates(data)
    rates = rates[rates > rate]
    return data.drop(rates.index, axis = 1)

def drop_missing_values_rows(data, rate):
    rates = data_visualization.nan_rows_rates(data)
    rates = rates[rates > rate]
    return data.drop(rates.index)