import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


from google.colab import auth
from google.colab import data_table
import gspread
from google.auth import default
import pandas as pd

auth.authenticate_user()          # This will ask you to login
creds, _ = default()
gc = gspread.authorize(creds)

worksheet = gc.open("Option Trades").worksheet("Sheet1")
# Get all data as list of lists (more reliable)
# Tell gspread to use Row 2 as the header row
df = pd.DataFrame(worksheet.get_all_records(head=2))

date_cols = ['Trade Date', 'Position Closed Date', 'Option Expiry Date']

for col in date_cols:
    # 1. Clean whitespace
    df[col] = df[col].astype(str).str.strip()
    # 2. Convert to datetime
    df[col] = pd.to_datetime(df[col], dayfirst=True, errors='coerce')

df = df[(df['Strategy']!= 'LEAPS Call') &
        (df['Option Expiry Date'] >= '2026-01-01')]



#data_table.disable_dataframe_formatter()
df.head()
#print(df['Option Expiry Date'].dtype)

