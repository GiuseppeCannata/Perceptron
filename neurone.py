import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.preprocessing import StandardScaler
from statsmodels.tools.tools import add_constant


class perceptron():

    def __init__(self, inp, target, epochs):

        self.X = inp
        self.y = target
        self.n = inp.shape[0]
        self.p = inp.shape[1]

        self.weights = np.random.normal(loc=0.0, scale=(np.sqrt(2 / self.p)),
                                        size=self.p)  # glorot   # [intercept, w1, w2, ... , wp]
        self.eta = 0.001
        self.epochs = epochs

    def relu(self, x):
        if x >= 0:
            return x
        else:
            return 0

    def derivata_relu(self, x):
        if x < 0:
            return 0
        elif x > 0:
            return 1

    def fit(self):

        for epoch in range(self.epochs):
            outputs = []
            for i, observation in enumerate(self.X):
                pa = np.sum(np.dot(self.weights, observation.T))
                y_pred = self.relu(pa)
                error = self.y[i] - y_pred
                # backprop
                self.weights += self.eta * error * observation #* self.derivata_relu(pa)  # delta rule

    def pred(self, x):
        return self.relu(np.sum(np.dot(self.weights, x.T)))


# ======================= COSTRUZIONE DATASET ============================================
dataset = load_boston()
df = pd.DataFrame(data=dataset.data, columns=dataset.feature_names)
y = dataset.target

chas = df['CHAS'].values
df.drop(labels=['CHAS'], axis=1, inplace=True)

# - standardizzazione
scaler = StandardScaler()
scaler.fit(df.values)
X_train_stan = add_constant(scaler.transform(df.values))
X_train_stan = np.c_[X_train_stan, chas]

p = perceptron(X_train_stan, y, 300)
p.fit()
print(p.weights)

res = []
y_preds = []
for i, el in enumerate(X_train_stan):
    y_pred = p.pred(el)
    res.append(p.y[i] - y_pred)
    y_preds.append(y_pred)

plt.scatter(y_preds, res)
plt.title('Residual plot of train samples')
plt.xlabel('y pred')
plt.ylabel('residuals')
plt.show()