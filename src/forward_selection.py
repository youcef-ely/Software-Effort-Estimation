import pandas as pd
from statsmodels.tools.tools import add_constant
from statsmodels.regression.linear_model import OLS


class ForwardSelection:
    
    
    def __init__(self, features, target, p_value_threshold = 0.05):
        self.features = features
        self.target = target
        self.p_value_threshold = p_value_threshold
        
    def forward_selection(self):
        initial_features = list(self.features.columns)
        best_features = []
        while (len(initial_features)>0):
            remaining_features = list(set(initial_features)-set(best_features))
            new_pval = pd.Series(index=remaining_features)
            for new_column in remaining_features:
                model = OLS(self.target, add_constant(self.features[best_features+[new_column]])).fit()
                new_pval[new_column] = model.pvalues[new_column]
            min_p_value = new_pval.min()
            if(min_p_value < self.p_value_threshold):
                best_features.append(new_pval.idxmin())
            else:
                break
        return best_features