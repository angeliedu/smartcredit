import json
import os
import secrets

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.mail import EmailMessage, send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from .forms import LoginForm, UserRegistrationForm
from .models import \
    CreditEvaluationModel  # Create a model to store evaluation results
from .models import UserRegistration


def generate_verification_code(length=5):
    return secrets.randbelow(10**length)

def checkout_view(request):
    # You can include any additional context data here if needed
    return render(request, 'SmartCredit/CheckoutPage.html')


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                # Redirect to a success page or do something else
                return redirect('CreditForm')
            else:
                # Invalid email or password
                # You can customize this part based on your requirements
                return render(request, 'SmartCredit/login.html', {'form': form, 'error': 'Invalid email or password'})
    else:
        form = LoginForm()

    return render(request, 'SmartCredit/login.html', {'form': form})


def signup_page(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Perform additional server-side validation if needed
            user = form.save()
            # You might want to handle user authentication or email verification here
            
            return redirect('login_page')  # Redirect to a success page
    else:
        form = UserRegistrationForm()

    return render(request, 'SmartCredit/SignUp.html', {'form': form})

Saved_code = generate_verification_code()

def verification(request):
    if request.method == 'POST':
        entered_code = request.POST.get('entered_code', '')
        server_code = request.POST.get('server_code', '')

        if entered_code == server_code:
            # Update the user's email_verified status
            user = UserRegistration.objects.get(email=request.user.email)  # Assuming you have a user object in the session
            user.email_verified = True
            user.save()

            return JsonResponse({'valid': True})
        else:
            return JsonResponse({'valid': False})
    return render(request, 'SmartCredit/Verification.html')
    
def ForgotPassword(request):
    # Your login page view logic here
    return render(request, 'SmartCredit/ForgotPassword.html')






#import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# Django View
@csrf_exempt
def CreditForm(request):
    result_message = '',
    if request.method == 'POST':
        # Retrieve form data from the request
        home_ownership = request.POST.get('home_ownership')
        annual_inc = request.POST.get('annual_inc')
        loan_amnt = request.POST.get('loan_amnt')
        emp_length = request.POST.get('emp_length')
        dti = loan_amnt/annual_inc

        # Convert data to the format expected by the model
        user_data = pd.DataFrame({
            'home_ownership': [home_ownership],
            'annual_inc': [float(annual_inc)],
            'loan_amnt': [float(loan_amnt)],
            'dti': dti,  # You need to handle dti separately based on your model
            'emp_length': [emp_length]
            })
                # Load datasets
        rejected_data = pd.read_csv('SmartCredit/archive/rejected_2007_to_2018q4.csv/rejected_2007_to_2018Q4.csv')
        accepted_data = pd.read_csv('SmartCredit/archive/accepted_2007_to_2018q4.csv/accepted_2007_to_2018Q4.csv')

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

        # Feature Engineering
        # One-hot encoding categorical columns
        encoded_data = pd.get_dummies(merged_data, columns=['home_ownership', 'emp_length'])

        # Splitting data and scaling features
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

        # Model Training and Evaluation
        classifier = LogisticRegression(max_iter=1000, random_state=42)
        classifier.fit(X_train_scaled, y_train)
        y_pred = classifier.predict(X_test_scaled)
        mse = mean_squared_error(y_test, y_pred)

        # One-hot encode categorical features
        user_encoded = pd.get_dummies(user_data, columns=['home_ownership', 'emp_length'])

        # Align the columns with the training data
        user_encoded = user_encoded.reindex(columns=X_train.columns, fill_value=0)

        # Scale the features
        user_scaled = scaler.transform(user_encoded)

        # Make prediction
        prediction = classifier.predict(user_scaled)

        # Display the result (you can customize this part)
        if prediction[0] == 1:
            result_message = "Loan ACCEPTED"
        else:
            result_message = "Loan REJECTED"

        return HttpResponse(f"Prediction Result: {result_message}")

    # Render the form template for GET requests
    return render(request, 'SmartCredit/MainForm.html', {'result_message': result_message})
