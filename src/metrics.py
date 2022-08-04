import sklearn.metrics as metrics
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd

def mean_absolute_error(y_true, y_pred):
    return metrics.mean_absolute_error(y_true, y_pred)

def magnitude_relative_error(y_true, y_pred):
    return np.abs(y_true - y_pred) / y_true

def r2_score(y_true, y_pred):
    return metrics.r2_score(y_true, y_pred)

def mean_magnitude_of_relative_error(y_true, y_pred):
    return np.mean(magnitude_relative_error(y_true, y_pred))

def pred(y_true, y_pred, rate: float = 0.25):
    errors = magnitude_relative_error(y_true, y_pred)
    s = 0
    for error in errors:
        if error <= 0.25:
            s = s + 1
    return s / len(y_true)


def scores_DataFrame(y_train, y_test, train_predictions, test_predictions):
  scores = pd.DataFrame(index = ['r2_score', 'MAE', 'MMRE', 'PRED (0.25)'], columns = ['Train score', 'Test score'])
  scores.loc['r2_score']['Train score'], scores.loc['r2_score']['Test score'] = r2_score(y_train, train_predictions), r2_score(y_test, test_predictions)
  scores.loc['MAE']['Train score'], scores.loc['MAE']['Test score'] = mean_absolute_error(y_train, train_predictions), mean_absolute_error(y_test, test_predictions)
  scores.loc['MMRE']['Train score'], scores.loc['MMRE']['Test score'] = mean_magnitude_of_relative_error(y_train, train_predictions), mean_magnitude_of_relative_error(y_test, test_predictions)
  scores.loc['PRED (0.25)']['Train score'], scores.loc['PRED (0.25)']['Test score'] = pred(y_train, train_predictions), pred(y_test, test_predictions)
  return scores



def plot_predictions(y_true, y_pred, figsize: tuple, title = ''):
    fig = plt.figure(figsize = figsize)
    plt.subplot(1, 2, 1)
    plt.plot(y_true, y_true, c = 'seagreen', label = 'True')
    plt.scatter(y_true, y_pred, c = 'darkslategrey')
    plt.subplot(1, 2, 2)
    sns.distplot(y_true - y_pred, color = 'g')
    fig.suptitle(title, fontsize = 16)
    plt.legend()
    plt.show()