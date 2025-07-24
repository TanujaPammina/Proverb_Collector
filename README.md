# Proverb_Collector
# 📜 Indian Local Proverb Collector

A simple Streamlit app to collect, preserve, and display traditional Indian proverbs from different regions, languages, and dialects — ensuring that local wisdom continues to thrive in the digital age.

---

## 🚀 Demo

👉 [Live on Hugging Face Spaces](https://huggingface.co/spaces/TanujaPammina/Proverb_Collector)
*(Replace the link with your actual space URL)*

---

## 📌 Features

- 📝 Users can submit their local proverbs with optional English translations.
- 🌐 Multi-language support for all Indian dialects.
- 🧾 Stores all submissions in a connected **Google Sheet**.
- 📊 View collected proverbs in a live, searchable table.
- 🔐 Secure credentials via **base64** in Hugging Face secrets.

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) – Interactive UI
- [gspread](https://github.com/burnash/gspread) – Google Sheets API
- [Hugging Face Spaces](https://huggingface.co/spaces) – Hosting platform
- `oauth2client`, `pandas`, `base64`, `datetime`

---

## 📂 Folder Structure
├── app.py # Main Streamlit app
├── requirements.txt # Python dependencies
├── README.md # Project overview
├── REPORT.md # Project explanation & solution
├── CONTRIBUTING.md # Contribution guidelines
├── CHANGELOG.md # Version history
├── LICENSE # Open-source license (MIT)

---

## 🔐 Environment Variable

To protect your Google Sheets credentials, encode your `Proverb-service.json` key as base64 and save it as a secret in Hugging Face:

bash
import base64

with open("Proverb-service.json", "rb") as f:
    print(base64.b64encode(f.read()).decode())
Then in Hugging Face Secrets, add:
GSPREAD_JSON = <your base64 string here>
🧪 Installation (for local testing)
git clone https://github.com/your-username/proverb-collector.git
cd proverb-collector
pip install -r requirements.txt
streamlit run app.py
✍️ Example Proverb
Telugu: ఓడిపోయిన నౌకను దూషించకూడదు
English: Never curse a sunken boat.
🙋‍♀️ Author
Tanuja Pammina
📧 tanujapammina@gmail.com
📃 License
This project is licensed under the MIT License.




