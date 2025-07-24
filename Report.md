# Indian Local Proverb Collector - AI Powered Open Source App

## 🚀 Project Overview

The Indian Local Proverb Collector is an AI-powered Streamlit application designed to preserve the rich linguistic and cultural heritage of India. The app allows users to submit local proverbs in any language or dialect, along with optional English translations. The submitted proverbs are stored in a connected Google Sheet for real-time viewing and future use in AI datasets and cultural research.

---

## 👤 Team Details

- **Name:** Tanuja Pammina  
- **Email:** tanujapammina@gmail.com  
- **Team Members:** Solo project

---

## 🎯 Problem Statement

Local proverbs are a vital part of Indian wisdom, often passed down orally through generations. Many are at risk of being lost due to lack of digital preservation. There is a need for a simple, user-friendly platform to collect, translate, and store these proverbs for future generations, cultural studies, and AI training.

---

## 💡 Solution

This app provides:
- A user-friendly Streamlit UI to submit proverbs.
- Fields for name, location, language/dialect, proverb, and optional English translation.
- Integration with Google Sheets via Hugging Face Secrets using `gspread` and `oauth2client`.
- Real-time display of submitted proverbs in a data table.

---

## 🔧 Tech Stack

- **Frontend & App Logic:** Streamlit  
- **Backend Integration:** Google Sheets API via `gspread`  
- **Cloud Hosting:** Hugging Face Spaces  
- **Secrets Handling:** Hugging Face Environment Variables  
- **Language:** Python  
- **Others:** Markdown, Git, GitHub

---

## 🔒 Secrets Used

- Google Service Account JSON was base64-encoded and stored securely in Hugging Face secrets as `GSPREAD_JSON`.

---

## ✅ Features

- 📤 Submit proverb with details
- 📄 View all previously submitted proverbs
- 🎈 Clean, responsive interface
- 💾 Data saved live to Google Sheets
- 🌐 Supports multiple Indian languages and dialects

---

## 📦 Files in This Repo

- `app.py` - Main Streamlit application
- `requirements.txt` - Required Python packages
- `REPORT.md` - This project report
  

---

## 🌍 Future Scope

- Add audio support for spoken proverbs
- Translate using multilingual AI models
- Tag proverbs by category or theme
- Use for building NLP datasets for regional languages

---

## 🙏 Acknowledgements

- VISWAM Summer of AI - for the platform and challenge  
- Streamlit, Hugging Face, and Google Sheets API  
- OpenAI for ChatGPT assistance during development

---

## 🔗 Live Demo

[🔗 Click here to try the app on Hugging Face](https://huggingface.co/spaces/TanujaPammina/Proverb_Collector)  
(Replace with your actual Hugging Face space link)

---

