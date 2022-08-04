from sklearn import preprocessing
from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import data_visualization as dv



def categories_processing(data, categories):
    for cat in categories:
        pk = data[cat].value_counts(normalize = True)[1]
        data[cat] = data[cat].apply(lambda x: x /pk**0.5)
        data[cat] = data[cat].apply(lambda x: x - data[cat].mean())
    return data

def pca(data, n_components = 120):
    pca = PCA(n_components = n_components)
    pca.fit(data)
    return pca

    
def famd_features(pca, data):
    new_features = pca.fit_transform(data)
    pca_features = pd.DataFrame(data = new_features
             , columns = ['Principal component ' + str(i) for i in range(1, new_features.shape[1] + 1)])
    pca_features.index = [i for i in range (1, len(data) + 1)]
    return np.round(pca_features, 3)

def plot_individuals(pc, pca, component1 = 1, component2 = 2):
    xmin, xmax = pc['Principal component '+str(component1)].min(), pc['Principal component '+str(component1)].max()
    ymin, ymax = pc['Principal component '+str(component2)].min(), pc['Principal component '+str(component2)].max()
    xmin, xmax = int(np.ceil(np.abs(xmin))), int(np.ceil(np.abs(xmax)))
    ymin, ymax = int(np.ceil(np.abs(ymin))), int(np.ceil(np.abs(ymax))) 
    fig, ax = plt.subplots(figsize=(20,20))
    ax.plot()
    ax.axis([-xmin, +xmax, -ymin, +ymax])
    ax.plot([-xmin, +xmax],[0,0],color='silver',linestyle='--')
    ax.plot([0,0],[-ymin, +ymax],color='silver',linestyle='--')
    plt.scatter(x = pc['Principal component '+str(component1)], 
                y = pc['Principal component '+str(component2)])
    for i in range(len(pc)):
        ax.text(pc.values[i,component1 - 1], pc.values[i,component2 - 1], pc.index[i]) 
    ax.set_xlabel("Comp.1 (" + str(np.round(pca.explained_variance_ratio_ * 100, 2)[component1 - 1])+'%)')
    ax.set_ylabel("Comp.2 (" + str(np.round(pca.explained_variance_ratio_ * 100, 2)[component2 - 1])+'%)')
    plt.show()
    
def components(pca, data):
    comp = pca.components_
    comp = pd.DataFrame(comp).T
    comp.index = data.columns
    comp.columns = ['Principal component ' + str(i) for i in range(1, comp.shape[1] + 1)]
    return comp
    
def corr_cercle(numerical_columns, categorical_columns, data, new_features, component1 = 1, component2 = 2): 
    fig, ax = plt.subplots(figsize = (15, 15))
    ax.axis([-1, 1, -1, 1])
    ax.plot([-1, 1], [0, 0], color = 'silver', linestyle = '--')
    ax.plot([0, 0], [-1, 1], color = 'silver', linestyle = '--')
    x = np.linspace(-1, 1, 500)
    y = (1 - x**2)**0.5
    plt.plot(x, y, c = 'b')
    plt.plot(x, -y, c = 'b')
    ########################### Numerical columns
    pc1_correlations = [np.corrcoef(data[col], 
                        new_features['Principal component ' + str(component1)])[0,1] for col in numerical_columns]
    pc2_correlations = [np.corrcoef(data[col], 
                        new_features['Principal component ' + str(component2)])[0,1] for col in numerical_columns]
    correlations = pd.DataFrame([pc1_correlations, pc2_correlations]).T
    correlations.index = numerical_columns
    correlations.columns = ['Principal component ' + str(component1), 'Principal component ' + str(component2)]
    plt.scatter(x = correlations['Principal component '+str(component1)], 
                y = correlations['Principal component '+str(component2)], 
                c = 'r', label = 'Numerical features')
    for i in range(len(correlations)):
        ax.text(correlations['Principal component ' + str(component1)][i], 
                correlations['Principal component ' + str(component2)][i],
                correlations.index[i])
        
    ########################### Categorical columns
    pc1_associations = [dv.rapport_corr(data[col], 
                        new_features['Principal component ' + str(component1)]) for col in categorical_columns]
    pc2_associations = [dv.rapport_corr(data[col], 
                        new_features['Principal component ' + str(component2)]) for col in categorical_columns]
    associations = pd.DataFrame([pc1_associations, pc2_associations]).T
    associations.index = categorical_columns
    associations.columns = ['Principal component ' + str(component1), 'Principal component ' + str(component2)]
    plt.scatter(x = associations['Principal component '+str(component1)], 
                y = associations['Principal component '+str(component2)], 
                c = 'b', label = 'Categorical features')
    for i in range(len(associations)):
        ax.text(associations['Principal component ' + str(component1)][i], 
                associations['Principal component ' + str(component2)][i],
                associations.index[i])
    plt.legend()
    plt.plot()
    
    return correlations, associations

def explained_variance(pca):
    exp_var_pca = pca.explained_variance_ratio_
    cum_sum_eigenvalues = np.cumsum(exp_var_pca)
    plt.figure(figsize = (15, 15))
    plt.bar(range(0,len(exp_var_pca)), exp_var_pca, alpha=0.5, align='center', label='Individual explained variance')
    plt.step(range(0,len(cum_sum_eigenvalues)), cum_sum_eigenvalues, where='mid',label='Cumulative explained variance')
    plt.ylabel('Explained variance ratio')
    plt.xlabel('Principal component index')
    plt.legend(loc='best')
    plt.tight_layout()
    plt.show()

    