import streamlit as st
import pandas as pd
from datetime import datetime
import gspread
import os
import json
import base64
from oauth2client.service_account import ServiceAccountCredentials

# ------------------ Google Sheets Setup ------------------ #
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Load base64-encoded credentials from Hugging Face secrets
creds_json = base64.b64decode(os.environ["GSPREAD_JSON"]).decode()
creds_dict = json.loads(creds_json)
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)

client = gspread.authorize(creds)
sheet = client.open("Proverbs Collection").sheet1  # Change sheet name if needed

# ------------------ Streamlit UI ------------------ #
st.set_page_config(page_title="Indian Local Proverb Collector", page_icon="📜", layout="centered")

st.markdown("## 📜 Indian Local Proverb Collector")
st.markdown("Preserving the wisdom of our ancestors, one proverb at a time.")
st.markdown("---")

with st.container():
    st.subheader("📝 Share Your Proverb")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("👤 Your Name")
        location = st.text_input("📍 Village / City")

    with col2:
        language = st.text_input("🗣️ Language or Dialect")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    proverb = st.text_area("💬 Enter the Proverb in Your Language")
    translation = st.text_area("🌐 English Translation (Optional)")

    if st.button("📤 Submit Proverb"):
        if name and location and language and proverb:
            row = [name, location, language, proverb, translation, timestamp]
            try:
                sheet.append_row(row)
                st.success("✅ Proverb Submitted Successfully!")
                st.balloons()
            except Exception as e:
                st.error(f"❌ Failed to submit data: {e}")
        else:
            st.warning("⚠️ Please fill in all required fields.")

st.markdown("---")
st.info("📚 Thank you for helping preserve our cultural heritage!")

# ------------------ Display Submitted Proverbs ------------------ #
st.subheader("📖 View Collected Proverbs")

try:
    data = sheet.get_all_records()
    if data:
        df = pd.DataFrame(data)
        st.dataframe(df)
    else:
        st.info("No proverbs submitted yet.")
except Exception as e:
    st.error(f"⚠️ Error fetching data from Google Sheet: {e}")
