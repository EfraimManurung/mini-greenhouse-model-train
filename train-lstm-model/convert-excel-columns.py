import pandas as pd

# Load the Excel file into a pandas DataFrame
file_path = 'lstm-datasets.xlsx'  # Replace with the path to your Excel file
df = pd.read_excel(file_path)

# Rearranging the columns as per the new order
new_column_order = [
    'timesteps',  # Renamed to 'Timesteps [5 minutes / -]' later
    'Action Ventilation',
    'Action Toplights',
    'Action Heater',
    'Rewards',
    'CO2 In (Predicted NN)',
    'CO2 In (Predicted GL)',
    'CO2 In (Predicted Combined)',
    'Temperature In (Predicted NN)',
    'Temperature In (Predicted GL)',
    'Temperature In (Predicted Combined)',
    'RH In (Predicted NN)',
    'RH In (Predicted GL)',
    'RH In (Predicted Combined)',
    'PAR In (Predicted NN)',
    'PAR In (Predicted GL)',
    'PAR In (Predicted Combined)',
    'CO2 In (Actual)',
    'Temperature In (Actual)',
    'RH In (Actual)',
    'PAR In (Actual)'
]

# Reorder the DataFrame's columns
df_reordered = df[new_column_order]

# Rename the 'timesteps' column to 'Timesteps [5 minutes]'
df_reordered.rename(columns={'timesteps': 'Timesteps [5 minutes]'}, inplace=True)

# Save the modified DataFrame back to an Excel file
output_file_path = 'rearranged_file.xlsx'  # Modify the output path if needed
df_reordered.to_excel(output_file_path, index=False)

print(f"Rearranged file has been saved as '{output_file_path}'")
