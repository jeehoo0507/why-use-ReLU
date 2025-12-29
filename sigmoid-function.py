import numpy as np
import matplotlib.pyplot as plt

# 시그모이드 함수 
def sigmoid(x):
    return 1/(1+np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)

plt.plot(x, y)
plt.plot([0,0],[1.0,0.0], ':') 
plt.title('Sigmoid Function')
plt.show()


#양 끝 부분의 gradient 소실 문제(vanishing gradient problem)