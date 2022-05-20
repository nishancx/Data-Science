"""AND Gate perceptron"""
data_set = {
    "00": 0,
    "01": 0,
    "10": 0,
    "11": 1,
}
bias = 0.5
weight_1 = 0.5
weight_2 = 0.5
learning_rate = 0.1
inputs = [[0,0], [0,1], [1, 0], [1, 1]]
condition = False
iteration_count = 0

def get_stored_values(first_input, second_input):
    """gets and gate output

    Args:
        first_input (number): _description_
        second_input (number): _description_

    Returns:
        number: value of and gate output
    """
    return data_set[str(first_input) + str(second_input)]


def recalculate_metrics(target, predicted, x_1, x_2, w_1, w_2, previous_bias):
    """Recalculate weights and bias"""
    global weight_1
    weight_1 = w_1 + learning_rate * (target - predicted) * x_1
    global weight_2
    weight_2 = w_2 + learning_rate * (target - predicted) * x_2
    global bias
    bias = previous_bias + learning_rate * (target - predicted)

def train():
    """train and gate model"""
    print('Iteration: ', iteration_count)
    validity_count = 0
    for inp in inputs:
        stored_value = get_stored_values(inp[0], inp[1])
        out_value = (inp[0] * weight_1) + (inp[1] * weight_2) + bias
        print(
            'inp:', inp,
            'out_value:', round(out_value),
            'stored value: ', stored_value,
            'weight_1:', weight_1,
            'weight_2: ', weight_2, 'bias: ', bias)
        if round(out_value) != stored_value:
            recalculate_metrics(stored_value,
            out_value,
            inp[0],
            inp[1],
            weight_1,
            weight_2,
            bias)
            break
        validity_count+=1
    if validity_count == 4:
        return True
    return False

while condition is not True:
    print('\n\n')
    iteration_count+=1
    condition = train()

print('\n\n\n')
print('Iteration:', iteration_count, 'weight_1:', weight_1, 'weight_2: ', weight_2, 'bias:', bias)

input_1 = input('Enter first input: ')
input_2 = input('Enter second input: ')
predicted_output = (weight_1 * float(input_1)) + (weight_2 * float(input_2) + bias)
print('Predicted output is ', round(predicted_output))