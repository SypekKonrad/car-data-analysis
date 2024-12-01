import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import numpy as np

SERVICE_ACCOUNT_FILE = 'toyota-avensis-441923-f7a47164daac.json'
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
gc = gspread.authorize(credentials)
spreadsheets = gc.list_spreadsheet_files()
# print(spreadsheets)

spreadsheet_name = "toyota avensis t22"
spreadsheet = gc.open(spreadsheet_name)
sheet = spreadsheet.sheet1

raw_data = sheet.get_all_values()

df = pd.DataFrame(raw_data[4:], columns=raw_data[0])

# selected_columns = df.iloc[:, [11, 12, 13, 14]]  
selected_columns = df.iloc[:, [11, 12, 13, 14]].copy()

selected_columns.columns = ['Date', 'Price', 'Kilometers Traveled', 'Liters']

selected_columns.replace('', np.nan, inplace=True)  
selected_columns.dropna(inplace=True)

selected_columns.to_csv('cleaned_car_data.csv', index=False)

# data_array = selected_columns.to_numpy()

# result display
# headers = selected_columns.columns.tolist()
# print(" | ".join(headers))  
# print("-" * 50)  
# print(data_array)  
