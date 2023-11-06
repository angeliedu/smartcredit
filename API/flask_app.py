
from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
import traceback

app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load('logistic_regression_model.pkl')
scaler = joblib.load('standard_scaler.pkl')

# Define the columns that the model expects
# This should correspond to the feature engineering process in the original notebook
model_columns = [
    # Add the expected model columns here, for example:
    'home_ownership',
    'annual_inc',
    'loan_amnt',
    'dti',
    # Include all other columns that were used in the model
]

@app.route('/predict', methods=['POST'])
def predict():
    try:
        json_ = request.json
        print(json_)
        query_df = pd.DataFrame(json_)
        query = pd.get_dummies(query_df)
        query = query.reindex(columns=model_columns, fill_value=0)

        scaled_query = scaler.transform(query)
        prediction = model.predict(scaled_query)

        return jsonify({'prediction': list(prediction)})
    except Exception as e:
        return jsonify({'error': str(e), 'trace': traceback.format_exc()})

if __name__ == '__main__':
    app.run(debug=True)
