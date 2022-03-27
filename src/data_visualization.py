import sys
import os

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path+"\\src")
    sys.path.append(module_path+"\\References")


import seaborn as sns
import pandas as pd 
pd.set_option('display.max_row', 70)
pd.set_option('display.max_column', 70)

"from data_dictionary import dictionary"


def pie_plot(column, data_dictionary):
    column.value_counts().sort_index().plot(kind = 'pie',
     labels = data_dictionary.values(), 
     autopct = '%.2f')

def barplot(column):
    sns.barplot(column.value_counts().sort_index())

"""def plot_by_category(data, category):
    categories = {
    'Size': [''],
    'General Information': ['Year of project', 'Organization type', 'Role in organization'],
    'Effort': [''],
    'Environment': [''],
    'Users': [''],
    'Developers': [''],
    'Project': [''], 
    'Product': [''], 
    }
    if (category == 'General Information'):
        if 
"""

def nan_columns_rates(data):
    return (data.isna().sum() / data.shape[0]).sort_values(ascending = False)

def nan_rows_rates(data):
    return data.isna().sum(axis = 1).sort_values(ascending = False) / data.shape[1]

def missing_values_map(data):
    sns.heatmap(data.isna())
