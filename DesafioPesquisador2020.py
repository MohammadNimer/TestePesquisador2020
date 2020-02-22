import pandas as pd

df = pd.read_csv('sms_senior.csv', encoding='unicode_escape', index_col='Full_Text', parse_dates=['Date'])
print(df)

