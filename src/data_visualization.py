import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
import scipy.stats as ss
import pandas as pd
from sqlalchemy import column
pd.set_option('display.max_row', 70)
pd.set_option('display.max_column', 70)
from scipy.stats import f_oneway
import researchpy as rp
from scipy.stats import kendalltau
def pie_plot(data_column, values_meaning):
    if values_meaning != None:
        data_column = data_column.replace(values_meaning)
    fig = plt.figure(figsize = (10, 10))
    fig.patch.set_facecolor('white')
    labels = None
    data_column.value_counts().plot(kind = 'pie', autopct = '%.2f')

## Histograms of numerical columns
def numerical_cols_histogram(Numerical_data_list, data):
    i = 1
    n = len(Numerical_data_list) / 3
    if len(Numerical_data_list) % 3 != 0:
        n = n + 1
    n = int(n)
    plt.figure(figsize = (20, 60))
    for col in Numerical_data_list:
        plt.subplot(n, 3, i)
        sns.distplot(data[col]) 
        i = i + 1
    plt.show()

## Boxplots  
def boxplots(columns, data):
    i = 1
    n = len(columns) / 2
    if len(columns) % 2 != 0:
        n = n + 1
    n = int(n)
    plt.figure(figsize = (20, 90))
    for col in columns:
        plt.subplot(n, 2, i)
        sns.boxplot(data[col])
        i = i + 1
    
def crosstab(df_categorical):
    i = 1
    n = df_categorical.shape[1] / 2
    if df_categorical.shape[1] % 2 != 0:
        n = n + 1
    n = int(n)
    cols = list(df_categorical.columns)
    for j in range(len(cols) - 1):
        plt.figure()
        sns.heatmap(pd.crosstab(df_categorical[cols[j]], df_categorical[cols[j+1]]), annot = True)
        i = i + 1


## Scatter plots of actual effort vs numerical data
def numerical_cols_vs_effort(Numerical_data_list, data):
    i = 1
    n = len(Numerical_data_list) / 3
    if len(Numerical_data_list) % 3 != 0:
        n = n + 1
    n = int(n)
    plt.figure(figsize = (20, 50))
    for col in Numerical_data_list:
        plt.subplot(n, 3, i)
        sns.scatterplot(x=data[col], y=data['Actual effort'])
        plt.xlabel(col)
        plt.ylabel('Actual Effort')
        i = i + 1


def discrete_cols_and_effort(data, discrete_cols):    
    for col in discrete_cols:
        plt.figure(figsize = (10, 11))
        groups_mean = data.groupby(col)['Actual effort'].mean()
        sns.barplot(x = groups_mean.index, y = groups_mean.values)
        plt.xlabel(col)
        plt.ylabel('Actual effort')
        plt.show()

def categorical_cols_vs_effort(df_categorical, actual_effort):
    i = 1
    n = df_categorical.shape[1] / 2
    if df_categorical.shape[1] % 2 != 0:
        n = n + 1
    n = int(n)
    plt.figure(figsize = (20, 200))
    cols = list(df_categorical.columns)
    for col in cols:
        plt.subplot(n, 2, i)
        sns.boxplot(x = df_categorical[col], y = actual_effort)
        plt.xlabel(col)
        plt.ylabel('Actual Effort')
        plt.xticks(rotation = 90)
        i = i + 1

def bar_plot_count(data_column, title, values_meaning = None):
    if values_meaning != None:
        data_column = data_column.replace(values_meaning)
    plt.figure(figsize = (9, 9))
    counts = data_column.value_counts(normalize = True, sort = False)
    ax     = sns.barplot(x = counts.index, y = counts.values)
    ax.bar_label(ax.containers[0], fmt = '%.2f')
    plt.title(title)
    plt.xticks(rotation = 90)


def nan_cols_and_actual_effort(data, nan_cols):
    i = 1
    n = len(nan_cols) / 3
    if len(nan_cols) % 3 != 0:
        n = n + 1
    n = int(n)
    plt.figure(figsize = (20, 50))
    for col in nan_cols:
        df = data.copy()
        df[col] = np.where(df[col].isnull(), 'Null', 'Not Null')
        plt.subplot(n, 3, i)
        sns.barplot(x = df.groupby(col)['Actual effort'].mean().index, y = df.groupby(col)['Actual effort'].mean().values)
        plt.title(col)
        i = i + 1 



def nan_columns_rates(data):
    return (data.isna().sum() / data.shape[0]).sort_values(ascending = False)



def nan_rows_rates(data):
    return data.isna().sum(axis = 1).sort_values(ascending = False) / data.shape[1]



def missing_values_map(data):
    plt.figure(figsize = (20,20))
    sns.heatmap(data.isna())


def categories_and_effort_scatter(category, data, values_meaning, effort = 'Actual effort'): 
    plt.scatter(x = data[category].replace(values_meaning), y = data[effort], c = data[category])
    plt.xlabel(category)
    plt.ylabel('Actual effort')
    plt.xticks(rotation = 75)
    plt.legend()
    plt.show()



def corr_matrix(data):
    plt.figure(figsize = (25,25))
    sns.heatmap(data.corr(), annot = True)
    

    
def anova_test(data, data_column_name):
    print('Null hypothesis: The mean of the groups are equal')
    alpha = 0.02
    groups = list(data[data_column_name].unique())
    minimum = data[data_column_name].value_counts().min()
    samples = []
    for category in groups:
        samples.append(data[data[data_column_name] == category]['Actual effort'].sample(minimum))
    stat, p = f_oneway(*samples)
    if p < 0.02:
        print('Null hypothesis rejected')
    else:
        print('Null hypothesis not rejected')
        
def categorical_cols_histograms_vs_effort(df_categorical, actual_effort_data):
    d = df_categorical.assign(Actual_effort = actual_effort_data)
    i = 1
    n = (len(d.columns) - 1) / 2 
    if n % 2 != 0:
        n = n + 1
    n = int(n)
    plt.figure(figsize = (20, 100))
    for col in d.columns:
        grouped_values = []
        if col != 'Actual_effort':
            plt.subplot(n, 2, i)
            for cat in d[col].unique():
                sns.distplot(d[d[col] == cat].Actual_effort, label = cat);
            plt.title(col);
            plt.legend();
        i = i + 1

    plt.show() 

def anova_test(df_categorical, column_name):
    print('Null hypothesis: The mean of the groups are equal')
    alpha = 0.02
    groups = list(df_categorical[column_name].unique())
    minimum = df_categorical[column_name].value_counts().min()
    print(f'Sample size is {minimum}')
    samples = []
    for category in groups:
        if type(category) == str:
            samples.append(df_categorical[df_categorical[column_name] == category]['Actual_effort'].sample(minimum))
    stat, p = f_oneway(*samples)
    print(f_oneway(*samples))
    if p < 0.05:
        print('Null hypothesis rejected')
    else:
        print('Null hypothesis not rejected')


def cramers_association(categorical_data):
    cols = categorical_data.columns
    association_table = pd.DataFrame(columns = cols, index = cols)
    for i in range(len(cols)):
        for j in range(0, len(cols)):
            ctab, chitest, expected = rp.crosstab(categorical_data[cols[i]], categorical_data[cols[j]]
                                                  , margins = False, test = 'chi-square', expected_freqs = True)
            cramerV = chitest[chitest['Chi-square test'] == "Cramer's V = "]['results']
            if cramerV.size != 0:
                association_table.loc[cols[i], cols[j]] = float(cramerV.values[0])
            else: 
                association_table.loc[cols[i], cols[j]] = float(np.nan)
    return association_table

def kendall_tau_association(data, ordinal_columns):
    results = pd.DataFrame(columns = ordinal_columns, index = ordinal_columns)
    for i in range(len(ordinal_columns)):
        for j in range(0, len(ordinal_columns)):
            tau, p_value = kendalltau(data[ordinal_columns[i]], data[ordinal_columns[j]]) 
            results.loc[ordinal_columns[i], ordinal_columns[j]] = tau
    return results

## This function is to use in correlation_actualEffort_categoricalData 
def rapport_corr(x,y):
    somme = 0
    for facteur in x.value_counts().index:
        ind = x[x == facteur].dropna(axis=0).index
        classe = y.loc[ind,]
        somme = somme + len(classe)*np.sum((np.mean(classe)-np.mean(y))**2)
    y_ecart = np.sum((y-np.mean(y))**2)
    rc = somme/y_ecart
    return rc

def correlation_actualEffort_categoricalData(categorical_columns, data):
    results = pd.Series(index = categorical_columns)
    for col in categorical_columns:
        results.loc[col] = rapport_corr(data[col], data['Actual effort'])
    return results
        
from scipy.stats import chi2_contingency

def chi2_test_categorical_features(cat_cols, data):
    associations = pd.DataFrame(columns = cat_cols, index = cat_cols)
    for i in range(len(cat_cols)):
        for j in range(len(cat_cols)):
            associations.loc[cat_cols[i]][cat_cols[j]] = np.round(chi2_contingency(pd.crosstab(data[cat_cols[i]], data[cat_cols[j]]))[1], 2)
    return associations