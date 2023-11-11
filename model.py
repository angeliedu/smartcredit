# 1. Feature Engineering

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

# 2. Model Training and Evaluation

# Train logistic regression model
classifier = LogisticRegression(max_iter=1000, random_state=42)
classifier.fit(X_train_scaled, y_train)

# Evaluate model
y_pred = classifier.predict(X_test_scaled)
mse = mean_squared_error(y_test, y_pred)