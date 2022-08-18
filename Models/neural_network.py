import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd
import tensorflow as tf
import tensorflow_addons as tfa
import random
from sklearn.model_selection import KFold, cross_val_score
import matplotlib.pyplot as plt
import os




class NeuralNetwork:

  def __init__(self, parameters: dict, X_train, y_train, metrics, epochs = 500, seed = 10):
    self.parameters = parameters
    self.X_train = X_train
    self.y_train = y_train
    self.epochs = epochs
    self.y_scaler = StandardScaler().fit(np.array(y_train).reshape((-1, 1)))
    self.y_train_sc = pd.DataFrame(self.y_scaler.transform(np.array(self.y_train).reshape((-1, 1))), index = self.y_train.index)
    self.history = None
    self.model = None
    self.seed = seed
    self.metrics = metrics

 

  def create_network(self): 
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.InputLayer(input_shape = self.X_train.shape[1])) 
    model.add(tf.keras.layers.Dropout(self.parameters['Dropout']))
        
    model.add(tf.keras.layers.Dense(1, activation  = 'linear'))

    model.compile(loss = tf.keras.losses.MeanAbsoluteError(),
                optimizer = tf.keras.optimizers.SGD(self.parameters['learning_rate'], momentum = self.parameters['momentum']), 
                metrics = [tfa.metrics.RSquare()])
    return model


  def cv_scores(self):
    kfold = KFold(n_splits = 5, shuffle = True, random_state = 37)
    mae_, mmre_, r2_, pred_ = [], [], [], []
    for train, test in kfold.split(self.X_train, self.y_train_sc):
      self.tf_seed()
      model = self.create_network()
      # Fit the model
      model.fit(self.X_train.values[train], self.y_train_sc.values[train],
                epochs = self.epochs, batch_size = self.parameters['batch_size'], verbose = 0)
      # evaluate the model
      predictions = model.predict(self.X_train.values[test], verbose=0)
      predictions = self.y_scaler.inverse_transform(predictions)
      mae_.append(self.metrics.mean_absolute_error(self.y_train.values[test], predictions))
      mmre_.append(self.metrics.mean_magnitude_of_relative_error(self.y_train.values[test], predictions))
      r2_.append(self.metrics.r2_score(self.y_train.values[test], predictions))
      pred_.append(self.metrics.pred(self.y_train.values[test], predictions.reshape((predictions.shape[0], ))))
    return dict(mae = np.array(mae_), mmre = np.array(mmre_), r2 = np.array(r2_), pred = np.array(pred_)) 

  def fit(self):
    self.tf_seed()
    model = self.create_network()
    self.model = model
    self.history = self.model.fit(self.X_train, self.y_train_sc, validation_split = 0.2, epochs = self.epochs, batch_size = self.parameters['batch_size'], verbose = 0)

  def evaluate(self, X_test, y_test):
    return self.model.evaluate(X_test, self.y_scaler.transform(np.array(y_test).reshape((-1, 1))))
  
  def predict(self, X_test):
    return self.y_scaler.inverse_transform(self.model.predict(X_test).reshape((-1, 1)))
  
  def tf_seed(self):
    os.environ['PYTHONHASHSEED'] = str(self.seed)
    # if your machine has GPUs use following to off it
    os.environ['CUDA_VISBLE_DEVICE'] = ''
    np.random.seed(self.seed)
    random.seed(self.seed)
    tf.random.set_seed(self.seed)



  def plot_history(self):
    fig = plt.figure(figsize = (15, 5))
    plt.subplot(1, 2, 1)
    plt.plot(self.history.history['r_square'], c = 'seagreen')
    plt.plot(self.history.history['val_r_square'], c = 'green')
    plt.title("Model's Score")
    plt.ylabel('R2')
    plt.xlabel('Epochs')
    plt.legend(['Train', 'Val'], loc='upper left')
    plt.subplot(1, 2, 2)
    plt.plot(self.history.history['loss'], c = 'seagreen')
    plt.plot(self.history.history['val_loss'], c = 'green')
    plt.title("Model's loss")
    plt.ylabel('Loss')
    plt.xlabel('Epochs')
    plt.legend(['Train', 'Val'], loc='upper left')
    plt.show()
    fig.savefig('/content/nn.pdf')
