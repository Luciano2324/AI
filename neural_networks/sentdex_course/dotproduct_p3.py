import numpy as np

inputs = [1, 2, 3, 2.5]

weights = [
            [0.2, 0.8, -0.5, 1.0], 
            [0.5, -0.91, 0.26, -0.5], 
            [-0.26, -0.27, 0.17, 0.87]
        ]

biases = [ 2, 3, 0.5 ]

output = np.dot(weights, inputs) + biases
"""
 the output variable works under the hood: 
 np.dot([1,2,3], [4,5,6]) = 1*4 + 2*5 + 3*6 = 32
 np.dot(weights, inputs) = [np.dot(weights[0], inputs), np.dot(weights[1], inputs), np.dot(weights[2], inputs)] = [2.8, -1.79, 1.85]
 np.dot(weights, inputs) + biases = [2.8, -1.79, 1.85] + [ 2, 3, 0.5 ] = [4.8, 1.21, 2.385]
"""
print(output)