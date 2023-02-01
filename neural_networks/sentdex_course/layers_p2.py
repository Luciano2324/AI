#In this case the input variable is one of the last neurons(output neuron), thats why it takes 4 weights cause before the output neurons there are 4 hidden layers with 3 unique weights each one.
inputs = [1, 2, 3, 2.5]
weights = [[0.2, 0.8, -0.5, 1.0], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]
bias = [ 2, 3, 0.5 ]

for x in range(len(bias)):
    output = 0

    output = inputs[0]*weights[x][0] + inputs[1]*weights[x][1] + inputs[2]*weights[x][2] + inputs[3]*weights[x][3] + bias[x]

    print(output)