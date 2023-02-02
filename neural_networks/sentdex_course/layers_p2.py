#In this case the input variable is one of the last neurons(output neuron), thats why it takes 4 weights cause before the output neurons there are 4 hidden layers with 3 unique weights each one.
inputs = [1, 2, 3, 2.5]
weights = [[0.2, 0.8, -0.5, 1.0], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]
biases = [ 2, 3, 0.5 ]

layer_ouputs = []

for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input*weight
    neuron_output += neuron_bias
    layer_ouputs.append(neuron_output)

print(layer_ouputs)