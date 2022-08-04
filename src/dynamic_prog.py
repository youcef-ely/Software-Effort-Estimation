from sklearn.model_selection import cross_val_score, KFold
class DynamicProgOptimizer:

  def __init__(self, parameters_ranges, estimator, X_train, y_train, score_thresold = 1):
    self.parameters_ranges = parameters_ranges
    self.estimator = estimator
    self.X_train = X_train
    self.y_train = y_train
    self.score_thresold = score_thresold
    self.best_parameters = None
  



  def get_estimator(self):
    return self.estimator

  def get_parameters_ranges(self):
      return self.parameters_ranges

  def get_estimator(self):
    return self.best_parameters

  def set_estimator(self, estimator):
    self.estimator = estimator

  def set_parameters_ranges(self, parameters_ranges):
    self.parameters_ranges = parameters_ranges
  
       
  def fitness_function(self, parameters):
    return cross_val_score(self.estimator.set_params(self), self.X_train, self.y_train, cv = KFold(5, shuffle = True)).mean()
  




  def tuning(self):
    best_params = dict()
    while(len(self.parameters_ranges) > len(best_params)):
      remaining_params = list(set(self.parameters_ranges.keys()) - set(best_params.keys()))
      for param in remaining_params:
        sorted_param_values = sorted(self.parameters_ranges[param], key = lambda value: self.fitness_function({param: value}), reverse = True)
        best_params[param] = sorted_param_values[0]
        self.estimator.set_params(**best_params)
        self.estimator.fit(self.X_train, self.y_train)
        score = self.estimator.score(self.X_train, self.y_train)
        if score > self.score_thresold:
          break
    
    return best_params
