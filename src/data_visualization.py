from cv2 import normalize
import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd
pd.set_option('display.max_row', 70)
pd.set_option('display.max_column', 70)


def pie_plot(data_column, values_meaning):
    if values_meaning != None:
        data_column = data_column.replace(values_meaning)
    fig = plt.figure(figsize = (10, 10))
    fig.patch.set_facecolor('white')
    labels = None
    data_column.value_counts().plot(kind = 'pie', autopct = '%.2f')


def histplot(column):
    sns.distplot(column.value_counts().sort_index())


def bar_plot_count(data_column, title, values_meaning = None):
    if values_meaning != None:
        data_column = data_column.replace(values_meaning)
    plt.figure(figsize = (12, 9))
    counts = data_column.value_counts(normalize = True, sort = False)
    ax     = sns.barplot(x = counts.index, y = counts.values)
    ax.bar_label(ax.containers[0], fmt = '%.2f')
    plt.title(title)
    plt.xticks(rotation = 75)



def nan_columns_rates(data):
    return (data.isna().sum() / data.shape[0]).sort_values(ascending = False)



def nan_rows_rates(data):
    return data.isna().sum(axis = 1).sort_values(ascending = False) / data.shape[1]



def missing_values_map(data):
    sns.heatmap(data.isna())


def visualize_feature_target(feature_column, target_column, values_meaning = None):
    plt.figure(figsize = (12,12))
    # If the feature column dtype is float
    if feature_column.dtype == 'float64':
        plt.plot(feature_column, target_column)
    elif values_meaning != None:
        plt.scatter(x = feature_column.replace(values_meaning), y = target_column, c = feature_column)
    plt.xlabel(feature_column.name)
    plt.ylabel(target_column.name)
    plt.legend()
    plt.show()


def corr_matrix(data):
    plt.figure(figsize = (30,30))
    sns.heatmap(data.corr(), annot = True)
    return data.corr()
