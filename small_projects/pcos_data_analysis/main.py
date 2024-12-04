import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

pcos_data_file_path = '../datasets/PCOS_data.csv'
pcos_data = pd.read_csv(pcos_data_file_path)

print(pcos_data.keys())

y = pcos_data['PCOS (Y/N)']
X = pcos_data[['Skin darkening (Y/N)', 'Hair loss(Y/N)', 'Cycle(R/I)', 'Cycle length(days)', 'Blood Group']]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
pcos_model = DecisionTreeRegressor()
pcos_model.fit(train_X, train_y)

predictions = pcos_model.predict(val_X)

print('Predictions :', [round(prediction) for prediction in predictions[:10]], sep='\n')
print('Actual values :', val_y[:10], sep='\n')
print('MEA =', mean_absolute_error(val_y, predictions))
