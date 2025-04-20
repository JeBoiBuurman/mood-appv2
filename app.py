import streamlit as st
import pandas as pd
from datetime import date
import os




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

dataframe = {
        "username": username,
        "Date" : datum,
        "mood" : mood,
        "energy" : energy,
        "stress" : stress,
        "sleep" : sleep
}
new_df = pd.DataFrame([dataframe])


if st.button("Save"):
    if not username:
        st.warning("Please enter your username before saving.")
    else:
        user_file = f"{username}_mood_data.csv"
        master_file = "data/all_user_mood_data.csv"

        #save to user file
        if os.path.exists(user_file):
            df = pd.read_csv(user_file)
            df = pd.concat([df, new_df], ignore_index=True)
        else:
            df = new_df

        df.drop_duplicates(subset=["Date"], keep="last", inplace=True)
        df.to_csv(user_file, index=False)

        # save to master file
        if os.path.exists(master_file):
            master_df = pd.read_csv(master_file)
            master_df = pd.concat([master_df, new_df], ignore_index=True)
        else:
            master_df = new_df

        
        
        master_df.drop_duplicates(subset=["Date"], keep='last', inplace=True)
        master_df.to_csv(master_file, index=False)
        st.success("Your entry has been saved!")