import random
import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def initialize_weights(input_size, hidden_size, output_size):
    # Initialize weights randomly for the input layer to the hidden layer and the hidden layer to the output layer
    weights_input_hidden = [[random.uniform(-1, 1) for _ in range(hidden_size)] for _ in range(input_size)]
    weights_hidden_output = [[random.uniform(-1, 1) for _ in range(output_size)] for _ in range(hidden_size)]
    return weights_input_hidden, weights_hidden_output

def feedforward(input_data, weights_input_hidden, weights_hidden_output):
    # Forward propagation through the network
    hidden_layer_input = [sum(input_data[i] * weights_input_hidden[i][j] for i in range(len(input_data))) for j in range(len(weights_input_hidden[0]))]
    hidden_layer_output = [sigmoid(x) for x in hidden_layer_input]
    
    output_layer_input = [sum(hidden_layer_output[j] * weights_hidden_output[j][k] for j in range(len(hidden_layer_output))) for k in range(len(weights_hidden_output[0]))]
    output = [sigmoid(x) for x in output_layer_input]
    
    return output

# Example input data
input_data = [[0, 0], [0, 1], [1, 0], [1, 1]]

# Define the architecture of the neural network
input_size = 2
hidden_size = 3
output_size = 1

# Initialize random weights for the network
weights_input_hidden, weights_hidden_output = initialize_weights(input_size, hidden_size, output_size)

# Perform forward propagation for each input
for data_point in input_data:
    output = feedforward(data_point, weights_input_hidden, weights_hidden_output)
    print(f"Input: {data_point}, Output: {output}")
