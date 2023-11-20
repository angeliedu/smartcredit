# check_table.py
from django.db import connection
from SmartCredit.models import UserRegistration  # Import your model

table_name = UserRegistration._meta.db_table
cursor = connection.cursor()
cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
if cursor.fetchone():
    print(f"The table '{table_name}' exists in the database.")
else:
    print(f"The table '{table_name}' does not exist in the database.")
