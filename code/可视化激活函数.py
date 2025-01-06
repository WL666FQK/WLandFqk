import numpy as np
import matplotlib.pyplot as plt
def sigmoid(x):
    return 1 / (1+np.exp(-x))

def plot_activation_function(func, x, title):
    y = func(x)
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.show()

def tanh(x):
    return np.tanh(x)

def relu(x):
    return np.maximum(0, x)

def leaky_relu(x, alpha=0.01):
    return np.where(x>0, x, x*alpha)

def parametric_relu(x, parm=0.5):
    return np.where(x>0, x, x*parm)

def elu(x, alpha=1):
    return np.where(x>0, x, alpha*(np.exp(x) - 1))

x_value = np.arange(-10, 10, 0.1)

# plot_activation_function(sigmoid, x_value, 'Simoid')
# plot_activation_function(tanh, x_value, 'tanh')
# plot_activation_function(relu, x_value, 'relu')
# plot_activation_function(leaky_relu, x_value, 'leaky_relu')
# plot_activation_function(parametric_relu, x_value, 'parametric_relu')
plot_activation_function(elu, x_value, 'elu')