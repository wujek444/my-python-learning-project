import pandas as pd

# save filepath to variable for easier access
melbourne_file_path = 'datasets/melb_data.csv'

# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path)

# print a summary of the data in Melbourne data to a html file
print(melbourne_data.to_html(), file=open("generated/data_visualization.html", "w"))