import numpy as np
from sklearn import preprocessing
import pandas as pd
from sklearn.impute import KNNImputer

nan = np.nan

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

def categorial_cols_imputation(data, columns_name):
    for col in columns_name:
        data[col] = data[col].fillna(data[col].mode()[0])
    return data

def scaling_numerical_data(numerical_columns, data):
    scaler = preprocessing.StandardScaler()
    data[numerical_columns] = scaler.fit_transform(X = data[numerical_columns])
    return scaler, data


def categorical_columns_prepare(categorical_columns, data):
    categorical_columns = [col for col in categorical_columns if col in data.columns]
    for col in categorical_columns:
        data[col] = data[col].apply(lambda x: col + ' ('+str(x)+')')
    return data
    

def polynomial_features(X, degree):
    poly = preprocessing.PolynomialFeatures(degree = degree)
    return poly.fit_transform(X), poly


def  NearestNeighborsImputation(data):
  rates = data.isna().sum().sort_values(ascending = False)
  rates = rates[rates != 0]
  missing_columns_v = list(rates.index)
  new_data_df=data.drop(missing_columns_v,axis='columns')
  for col in missing_columns_v:
      new_data_df[col]=data[col]
      imputer = KNNImputer(n_neighbors=2, weights="uniform")
      new_data_df=pd.DataFrame(imputer.fit_transform(new_data_df),columns=new_data_df.columns)
  return new_data_df

def PolynomialFeatures_labeled(input_df,power):
   
    poly = preprocessing.PolynomialFeatures(power)
    output_nparray = poly.fit_transform(input_df)
    powers_nparray = poly.powers_

    input_feature_names = list(input_df.columns)
    target_feature_names = ["Constant Term"]
    for feature_distillation in powers_nparray[1:]:
        intermediary_label = ""
        final_label = ""
        for i in range(len(input_feature_names)):
            if feature_distillation[i] == 0:
                continue
            else:
                variable = input_feature_names[i]
                power = feature_distillation[i]
                intermediary_label = "%s**%d" % (variable,power)
                if final_label == "":         #If the final label isn't yet specified
                    final_label = intermediary_label
                else:
                    final_label = final_label + " x " + intermediary_label
        target_feature_names.append(final_label)
    output_df = pd.DataFrame(output_nparray, columns = target_feature_names)
    return output_df




