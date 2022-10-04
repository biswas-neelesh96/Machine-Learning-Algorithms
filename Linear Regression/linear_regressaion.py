import numpy as np

def root_mean_squared_error(y, y_pred):
    return np.sqrt(np.mean((y - y_pred)**2))

class LinearRegression:
    def __init__(self, learning_rate=0.01, n_iterations=300):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        m, n = X.shape

        # init parameters
        self.weights = np.zeros(n)
        self.bias = 0

        # gradient descent
        for _ in range(self.n_iterations):
            y_predicted = np.dot(X, self.weights) + self.bias       # y = wx + b || [m, ] =  [m, n] . [n, ] + [1, ]

            # compute gradients
            dw = (1 / m) * np.dot(X.T, (y_predicted - y))           # dw = (1 / m) * (X.T . (y_predicted - y)) || [n, ] = [n, m] . ([m, ] - [m, ])
            db = (1 / m) * np.sum(y_predicted - y)                  # db = (1 / m) * np.sum(y_predicted - y) || [1, ] = Σ([m, ] - [m, ])

            # update parameters
            self.weights -= self.learning_rate * dw                 # w = w - ɑ * dw
            self.bias -= self.learning_rate * db                    # b = b - ɑ * db

        return self

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias

    def score(self, X, y):
        y_pred = self.predict(X)
        return 1 - root_mean_squared_error(y, y_pred) / np.mean(y)

if __name__ == "__main__":
    X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
    y = np.array([1, 2, 3, 4, 5])
    y = y * (np.random.randn(5) * 0.01 + 1)

    regressor = LinearRegression()
    regressor.fit(X, y)
    print(regressor.predict(X))
    print(f'RMSE: {regressor.score(X, y)}')