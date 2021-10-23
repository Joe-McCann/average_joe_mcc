import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

n = 10
x = np.random.rand(n, 1)
X = np.linspace(0, 1, 10)

slope = 2
intercept = -1

y = slope * x + intercept + np.random.normal(0, 1, size=(n, 1))

model = linear_model.LinearRegression()
model.fit(x, y)
predictions = model.predict(X.reshape(-1, 1))

plt.scatter(x, y)
plt.plot(X, slope*X + intercept, c="r")
plt.plot(X, predictions, c="k")
plt.legend(["True Line", "Predicted Line"])
plt.title("Random Data with Underlying Line")
plt.show()