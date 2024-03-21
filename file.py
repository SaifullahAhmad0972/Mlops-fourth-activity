from flask import Flask, jsonify
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Initialize Flask application
app = Flask(__name__)

# Load and prepare the dataset and model as before
data = pd.read_csv('healthcare-dataset-stroke-data.csv')
X = data[['age']].values
y = data['stroke'].values.reshape(-1, 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

@app.route('/metrics', methods=['GET'])
def metrics():
    # Return the calculated metrics as a JSON response
    return jsonify({
        'Mean Squared Error': mse,
        'R-squared': r2
    })

if __name__ == '__main__':
    app.run(debug=True)
