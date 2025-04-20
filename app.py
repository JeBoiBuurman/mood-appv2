import streamlit as st
import pandas as pd
from datetime import date
import os
import gspread
from google.oauth2.service_account import Credentials
import json
# Define scope for Google Sheets + Drive access
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Load credentials from file and authorize client


creds_json = st.secrets["credentials"]
creds_dict = json.loads(creds_json)
creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPE)

client = gspread.authorize(creds)

# Open your sheet by name
sheet = client.open("mood_tracker").sheet1








st.title("mood and energy tracker")
username = st.text_input("Enter your name or ID")

datum = st.date_input("Date")
mood = st.slider("How's your Mood today?", 0, 5)
energy = st.slider("How's your Energy today?", 0, 5)
stress = st.slider("How Stressed are you today?", 0, 5)
sleep = st.number_input("How many hours did you sleep today:",0,24)
st.write("Mood:", mood)
st.write("Energy:", energy)
st.write("Stress:", stress)
st.write("Sleep:", sleep)
note = st.text_input("any notes?")


dataframe = {
        "username": username,
        "Date" : datum,
        "mood" : mood,
        "energy" : energy,
        "stress" : stress,
        "sleep" : sleep,
        "notes" : note
}
new_df = pd.DataFrame([dataframe])


if st.button("Save"):
    if not username:
        st.warning("Please enter your username before saving.")
    else:
        try:
            google_data = [username, str(datum), mood, energy, stress, sleep, note]
            sheet.append_row(google_data)
        
            st.success("Your entry has been saved!")
        except Exception as e:
            st.error(f'Error saving data: {e}')
     #   user_file = f"{username}_mood_data.csv"
    #    master_file = "data/all_user_mood_data.csv"

        #save to user file
    #    if os.path.exists(user_file):
    #        df = pd.read_csv(user_file)
    #        df = pd.concat([df, new_df], ignore_index=True)
    #    else:
    #        df = new_df
#
 #       df.drop_duplicates(subset=["Date"], keep="last", inplace=True)
 #       df.to_csv(user_file, index=False)
#
#        # save to master file
#        if os.path.exists(master_file):
#            master_df = pd.read_csv(master_file)
#            master_df = pd.concat([master_df, new_df], ignore_index=True)
#        else:
#            master_df = new_df

        
        
 #       master_df.drop_duplicates(subset=["Date"], keep='last', inplace=True)
  #      master_df.to_csv(master_file, index=False)
        