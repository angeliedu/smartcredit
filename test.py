import pickle


# Load and train your model, and ensure it's in a variable named 'classifier'
# Import the function from model.py that returns the trained model
from model import trained_model

classifier = trained_model()

# Save the trained model
with open('model.pkl', 'wb') as file:
    pickle.dump(classifier, file)

# Load the model for testing or deployment
with open('model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

print(type(loaded_model))

# Prepare your sample input (ensure it's in the correct format as expected by your model)
sample_input = [['MORTGAGE', 22498.05, 23634.03, 41.17, '2 years']]
# Note: The input should be a list of lists, as most models expect 2D array-like structures

# Make a prediction
prediction = loaded_model.predict(sample_input)

# Print the prediction result
print("\nPrediction Result:")
if prediction[0] == 1:
    print("Loan APPROVED")
else:
    print("Loan REJECTED")
