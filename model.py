# Importing necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error

# Functio to return the trained model
def trained_model():
    return classifier

# 1. Data Loading and Preprocessing
# Load datasets
rejected_data = pd.read_csv('/Users/eduardoangeli/Desktop/Capstone/Dataset/rejected_2007_to_2018q4.csv/rejected_2007_to_2018Q4.csv')
accepted_data = pd.read_csv('/Users/eduardoangeli/Desktop/Capstone/Dataset/accepted_2007_to_2018q4.csv/accepted_2007_to_2018Q4.csv')


# Label datasets: 1 for accepted and 0 for rejected
accepted_data['label'] = 1
rejected_data['label'] = 0

# Rename columns in rejected dataset to match accepted dataset
rejected_data.rename(columns={'Amount Requested': 'loan_amnt', 'Debt-To-Income Ratio': 'dti'}, inplace=True)

# Select and align columns for merging
selected_columns = ['home_ownership', 'annual_inc', 'loan_amnt', 'dti', 'emp_length', 'label']
for column in selected_columns:
    if column not in rejected_data.columns:
        rejected_data[column] = None

# Merge datasets
merged_data = pd.concat([accepted_data[selected_columns], rejected_data[selected_columns]], axis=0).reset_index(drop=True)

# Handle missing values
for column in ['home_ownership', 'emp_length']:
    merged_data[column].fillna(merged_data[column].mode()[0], inplace=True)
for column in ['annual_inc']:
    merged_data[column].fillna(merged_data[column].median(), inplace=True)

# Convert dti values to numerical format and handle missing values
merged_data['dti'] = merged_data['dti'].str.rstrip('%').astype('float') / 100.0
merged_data['dti'].fillna(merged_data['dti'].median(), inplace=True)


# 2. Feature Engineering

# One-hot encoding categorical columns ( encoding to categorical variables)
encoded_data = pd.get_dummies(merged_data, columns=['home_ownership', 'emp_length'])

# Splitting data and scaling features (split our data into training and test sets and scale, to normalizing data)
X = encoded_data.drop(columns=['label']) 
y = merged_data['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# Handle NaN values
if np.isnan(X_train_scaled).any():
    nan_columns = np.where(np.isnan(X_train_scaled).any(axis=0))[0]
    for col in nan_columns:
        col_mean = np.nanmean(X_train_scaled[:, col])
        X_train_scaled[np.isnan(X_train_scaled[:, col]), col] = col_mean
        X_test_scaled[np.isnan(X_test_scaled[:, col]), col] = col_mean


# 3. Model Training and Evaluation

# Train logistic regression model
classifier = LogisticRegression(max_iter=1000, random_state=42)
classifier.fit(X_train_scaled, y_train)

# Evaluate model
y_pred = classifier.predict(X_test_scaled)
mse = mean_squared_error(y_test, y_pred)