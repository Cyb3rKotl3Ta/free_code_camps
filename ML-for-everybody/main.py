import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report


def scaled_dataset(dataframe, oversample=False):
    X = dataframe[dataframe.columns[:-1]].values
    y = dataframe[dataframe.columns[-1]].values

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    if oversample:
        ros = RandomOverSampler()
        X, y = ros.fit_resample(X, y)
    
    data = np.hstack((X, np.reshape(y, (-1, 1))))

    return data, X, y


cols = ['fLength', 'fWidth', 'fSize', 'fConc', 'fConc1', 
        'fAsym', 'fM3Long','fM3Trans', 'fAlpha', 'fDist', 'class']
df = pd.read_csv('ML-for-everybody/magic04.data', names=cols)
df['class'] = (df['class'] == 'g').astype(int)

# print(df.head())
print(df['class'].unique())


# for label in cols[:-1]:
#     plt.hist(df[df['class']==1][label], color='blue', label='gamma', alpha=0.7, density=True)
#     plt.hist(df[df['class']==0][label], color='red', label='hadron', alpha=0.7, density=True)
#     plt.title(label)
#     plt.ylabel('Probabilyty')
#     plt.xlabel(label)
#     plt.legend()
#     plt.show()

# Train, validation and test set
train, valid, test = np.split(df.sample(frac=1), [int(0.6*len(df)), int(0.8*len(df))])

# print(len(train[train['class']==1]))
# print(len(train[train['class']==0]))

train , X_train, y_train = scaled_dataset(train, oversample=True)
valid , X_valid, y_valid = scaled_dataset(valid, oversample=False)
test , X_test, y_test = scaled_dataset(test, oversample=False)


# print(sum(y_train==1))
# print(sum(y_train==0))


#kNN SECTION

knn_model = KNeighborsClassifier(n_neighbors=1)
knn_model.fit(X_train, y_train)

y_pred = knn_model.predict(X_test)
print(classification_report(y_test, y_pred))

