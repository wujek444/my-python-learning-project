import pandas as pd
from pandas import Series, DataFrame
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor

# save filepath to variable for easier access
melbourne_file_path = 'datasets/melb_data.csv'

# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path)

print(melbourne_data.columns)

# dropna drops data rows with missing values (think of na as "not available")
melbourne_data = melbourne_data.dropna(axis=0)

#save dataframe to html for better viewing
#print(melbourne_data.to_html(), file=open("generated/data_visualization_na_stripped.html", "w"))

#price is the prediction target (we are trying to predict it dependent on "features")
y: Series = melbourne_data.Price #y=prediction_target; it contains data from single column "Price"

#selecting features to predict price by
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X: DataFrame = melbourne_data[melbourne_features] #X is conventional name for features
#print("Data description:", X.describe(), sep='\n')
#print("Data head (first few rows of data):", X.head(), sep='\n')

# Define model. Specify a number for random_state to ensure same results each run (value doesn't matter)
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model (build decision tree model)
melbourne_model.fit(X, y)

#predictions:
print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))
print("Real values are:", y.head(), sep='\n')

#model validation
predicted_home_prices = melbourne_model.predict(X)
error = mean_absolute_error(y, predicted_home_prices) #mean absolute error (MAE - metric used to summarize model quality)
print("Mean absolute error in dollars:", error) #this validation is bad, because it is using same data as used to train the model
