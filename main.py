# Import CalibratorModel

from calibratormodels.NeuralNetworksModel import NeuralNetworksModel

nn_model = NeuralNetworksModel()

data_input = {
    'time': [1200, 1500, 1800],
    'global out': [0, 0.029625, 0.032943],
    'temp out': [22.8, 22.7, 22.8],
    'rh out': [51.65, 51.05, 48.05],
    'co2 out': [613, 619, 623],
    'ventilation': [0, 0, 0],
    'toplights': [1, 1, 1],
    'heater': [1, 1, 1]
}

# target_variable = 'global in'
# predictions = nn_model.predict_measurements(target_variable, data_input)
# print(predictions)

# List of target variables
target_variables = ['global in', 'temp in', 'rh in', 'co2 in']

# Iterate through each target variable and call the function
for target in target_variables:
    predictions = nn_model.predict_measurements(target, data_input)
    print(predictions)
