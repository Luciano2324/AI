# In the context of neural networks, a batch is a subset of the total training data that is used in one iteration of the training process. During each iteration, the neural network processes the batch of data, updates its weights, and then moves on to the next batch.

# Batching is used in deep learning because it can reduce the memory requirements of the training process, as well as make the training process more computationally efficient. Additionally, batching can also lead to more stable weight updates, as the weights are updated based on the average of the gradients across a batch of examples, rather than on a single example.

# The size of the batch, also known as the batch size, is a hyperparameter that can be tuned to optimize the performance of a neural network. A smaller batch size can lead to more frequent weight updates and allow the network to more quickly adapt to the training data, but it can also lead to more noise in the weight updates. A larger batch size can lead to more stable weight updates, but it can also make the network more slow to adapt to the training data. The ideal batch size will depend on the size of the training data, the computational resources available, and the specific requirements of the problem being solved.

import numpy as np

inputs = [1, 2, 3, 2.5]
weights = [[0.2, 0.8, -0.5, 1.0], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]
biases = [ 2, 3, 0.5 ]

output = np.dot(weights, inputs) + biases
"""
 the output variable works under the hood: 
 np.dot([1,2,3], [4,5,6]) = 1*4 + 2*5 + 3*6 = 32
 np.dot(weights, inputs) = [np.dot(weights[0], inputs), np.dot(weights[1], inputs), np.dot(weights[2], inputs)] = [2.8, -1.79, 1.85]
 np.dot(weights, inputs) + biases = [2.8, -1.79, 1.85] + [ 2, 3, 0.5 ] = [4.8, 1.21, 2.385]
"""
print(output)