import pandas as pd

# Load the Excel file into a pandas DataFrame
file_path = 'lstm-datasets-15-days.xlsx'  # Replace with the path to your Excel file
df = pd.read_excel(file_path)

# Rearranging the columns as per the new order
new_column_order = [
    'timesteps',  # Renamed to 'Timesteps [5 minutes]' later
    'Action Ventilation',
    'Action Toplights',
    'Action Heater',
    'Rewards',
    'CO2 In (Predicted DNN)',  # Updated names to match your new format
    'CO2 In (Predicted GL)',
    'CO2 In (Predicted Combined)',
    'CO2 In (Actual)',
    'Temperature In (Predicted DNN)',
    'Temperature In (Predicted GL)',
    'Temperature In (Predicted Combined)',
    'Temperature In (Actual)',
    'RH In (Predicted DNN)',
    'RH In (Predicted GL)',
    'RH In (Predicted Combined)',
    'RH In (Actual)',
    'PAR In (Predicted DNN)',
    'PAR In (Predicted GL)',
    'PAR In (Predicted Combined)',
    'PAR In (Actual)' # ,
    # 'Leaf Temp (Predicted DNN)',
    # 'Leaf Temp (Predicted GL)',
    # 'Leaf Temp (Predicted Combined)',
    # 'Leaf Temp (Actual)'
]

# Reorder the DataFrame's columns
df_reordered = df[new_column_order]

# Rename the 'timesteps' column to 'Timesteps [5 minutes]'
df_reordered.rename(columns={'timesteps': 'Timesteps [5 minutes]'}, inplace=True)

# Save the modified DataFrame back to an Excel file
output_file_path = 'lstm-datasets-15-days-rearranged.xlsx'  # Modify the output path if needed
df_reordered.to_excel(output_file_path, index=False)

print(f"Rearranged file has been saved as '{output_file_path}'")
