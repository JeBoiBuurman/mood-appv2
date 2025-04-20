
# 📊 Mood & Energy Tracker App

This is a simple, user-friendly web app to log and track your daily mood, energy, stress levels, sleep duration, and optional notes. Data is securely stored in Google Sheets and the app is hosted using Streamlit Cloud.

---

## 🚀 Live App

Access the live app here:  
👉 [mood-appv2 Streamlit App](https://mood-appv2-qp7rarbtmtbneou9dqcgpy.streamlit.app/)

---

## 💡 Features

- Record mood, energy, stress, and sleep daily
- Optional notes for context
- Data is stored directly in Google Sheets
- Automatically timestamps each entry
- Hosted in the cloud with real-time access
- Built with beginner-friendly tools

---

## 🛠️ Built With

- [Streamlit](https://streamlit.io/) – Web UI framework
- [Google Sheets API](https://developers.google.com/sheets/api) – Data storage
- [gspread](https://github.com/burnash/gspread) – Python API for Google Sheets
- [Google-auth](https://googleapis.dev/python/google-auth/latest/) – Secure authentication
- [Pandas](https://pandas.pydata.org/) – Data manipulation

---

## 🔐 Secrets & Credentials

This app uses Streamlit's built-in `st.secrets` to securely store `credentials.json`.

Example `st.secrets` config (do NOT commit this to GitHub):

```toml
credentials = """
{
  "type": "service_account",
  "project_id": "...",
  "private_key_id": "...",
  "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
  ...
}
"""
```

---

## 📦 Installation

1. Clone this repo:
```bash
git clone https://github.com/JeBoiBuurman/mood-appv2.git
cd mood-appv2
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Add your `credentials.json` or Streamlit secrets

4. Run the app locally:
```bash
streamlit run app.py
```

---

## 🧭 Folder Structure

```
mood-appv2/
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📌 Future Improvements

- 📈 Mood & energy trend charts
- 📅 Weekly/monthly filters
- ⬇ Download your mood history as CSV
- 🔐 User-based data separation (tokens or usernames)
- 📊 Dashboard view for insights

---

## 🧑‍💻 Author

Made with ❤️ by [JeBoiBuurman](https://github.com/JeBoiBuurman)  
Feel free to contribute or fork the project!

