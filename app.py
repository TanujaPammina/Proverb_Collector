import streamlit as st
from datasets import load_dataset, Dataset
import pandas as pd

# Save to Hugging Face dataset
def save_to_dataset(data, dataset_repo="TanujaPammina/proverbs"):
    csv_file = "proverbs.csv"

    # Try loading existing dataset
    try:
        dataset = load_dataset(dataset_repo, split="train")
        df_existing = dataset.to_pandas()
    except:
        df_existing = pd.DataFrame()

    # Harmonize old column names
    if 'Translation' in df_existing.columns and 'English_Translation' not in df_existing.columns:
        df_existing['English_Translation'] = df_existing['Translation']

    # Drop unwanted columns (including Timestamp)
    df_existing = df_existing.drop(
        columns=[col for col in ['TimeStamp', 'Translation', 'Timestamp'] if col in df_existing.columns],
        errors='ignore'
    )

    # Create new row
    df_new = pd.DataFrame([data])
    df_combined = pd.concat([df_existing, df_new], ignore_index=True)

    # Save to CSV
    df_combined.to_csv(csv_file, index=False, encoding='utf-8')

    # Push to Hugging Face
    ds_to_push = Dataset.from_pandas(df_combined)
    ds_to_push.push_to_hub(dataset_repo, split="train")

# --------------------- Streamlit UI -----------------------

st.set_page_config(page_title="Telugu Proverb Collector", page_icon="🌿")
st.title("🌿 Telugu Proverb Collector")

with st.form("proverb_form"):
    name = st.text_input("👤 Name")
    location = st.text_input("📍 Location")
    language = st.text_input("🗣 Language", value="Telugu")
    proverb = st.text_area("💬 Enter Proverb in Your Language")
    english_translation = st.text_area("🔤 Translate Proverb to English")

    submitted = st.form_submit_button("✅ Submit Proverb")

    if submitted:
        if name and proverb:
            data = {
                "Name": name,
                "Location": location,
                "Language": language,
                "Proverb": proverb,
                "English_Translation": english_translation
                # No Timestamp included
            }
            save_to_dataset(data)
            st.success("✅ Proverb submitted successfully!")
            st.balloons()
        else:
            st.error("⚠️ Please fill in at least Name and Proverb fields.")

# View submitted data
if st.button("📄 View Submitted Proverbs"):
    try:
        dataset = load_dataset("TanujaPammina/proverbs", split="train")
        df = dataset.to_pandas()

        # Harmonize column names
        if 'Translation' in df.columns and 'English_Translation' not in df.columns:
            df['English_Translation'] = df['Translation']

        # Drop unnecessary columns
        df = df.drop(columns=[col for col in ['Translation', 'Timestamp', 'TimeStamp'] if col in df.columns], errors='ignore')

        st.dataframe(df)
    except Exception as e:
        st.error(f"❌ Could not load data: {e}")
