# import libraries
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# assign a scope
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

# create credentials
credaccess = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

# authorize a gspread client
client = gspread.authorize(credaccess)

# access Google Sheets by calling client.open
sheet = client.open('My Spreadsheet').sheet1

# set data to all records in sheet 1
data = sheet.get_all_records()

# print to terminal
print(data)
