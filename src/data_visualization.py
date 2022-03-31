import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd 
pd.set_option('display.max_row', 70)
pd.set_option('display.max_column', 70)


def pie_plot(column, values_meaning):
    
    labels = None
    if dict != {}:
        labels = dict.values()
    column.value_counts().sort_index().plot(kind = 'pie',
    labels = values_meaning, 
    autopct = '%.2f')

def histplot(column):
    sns.distplot(column.value_counts().sort_index())

"""def plot_by_category(data, category): 
    category_columns = data_dictionary.categories(category)    
    for col in category_columns:
        if data_dictionary.values_meaning(col) != {}:
            if data[col].dtype == 'int64':
                plt.figure(figsize = (10,10))
                pie_plot(data[col])
            elif data[col].dtype == 'float64':
                plt.figure(figsize = (10,10))
                histplot(data[col])
            else: 
                continue
        else: 
            continue"""


def nan_columns_rates(data):
    return (data.isna().sum() / data.shape[0]).sort_values(ascending = False)

def nan_rows_rates(data):
    return data.isna().sum(axis = 1).sort_values(ascending = False) / data.shape[1]

def missing_values_map(data):
    sns.heatmap(data.isna())


def visualize_feature_target(feature_column, target_column, feature_codes = {}):
    plt.figure(figsize = (12,12))
    # If the column is  ot categorial and its type is flaot
    if feature_codes == {} and feature_column.dtype == 'float':
        plt.plot(feature_column, target_column)
    elif dict != {}:
        plt.scatter(feature_column, target_column, c = feature_column, label = feature_column)
    plt.xlabel(feature_column.column)
    plt.ylabel(target_column.column)
    plt.legend()
    plt.show()

