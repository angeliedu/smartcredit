# utils.py

import pickle


def load_scaler_from_file(scaler_filename='scaler.pkl'):
    try:
        with open(scaler_filename, 'rb') as file:
            scaler = pickle.load(file)
        return scaler
    except FileNotFoundError:
        print(f"Scaler file '{scaler_filename}' not found.")
        return None
    except Exception as e:
        print(f"Error loading scaler: {e}")
        return None
