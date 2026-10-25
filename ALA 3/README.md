# Library Management Chatbot

A rule-based chatbot built in Python using `if-elif-else` conditions, made for the GMIU college assignment. It answers common library questions automatically, in the terminal and in a browser (Streamlit).

> Timings, fines, borrowing limits, contact details and the book list are **sample (illustrative) data**. Edit the top of `library_chatbot.py` to match your real college library.

## Group Members
| Name | Enrollment No. |
|------|----------------|
| ____________ | ____________ |
| ____________ | ____________ |

## Features
Greetings, help menu, library timings, book availability, issue, return, renewal, membership, maximum books, borrowing duration, late fines, rules, search by title/author, location, contact, and exit (`exit` / `quit` / `bye`).

## Project Structure
```
library-chatbot/
├── library_chatbot.py   # Core rule-based chatbot (terminal version)
├── app.py               # Streamlit web version
├── requirements.txt
├── README.md
└── report/Library_Chatbot_Report.pdf
```

## Run Locally (Windows + VS Code)
1. Install Python 3.10+ from https://www.python.org/downloads/ — tick **"Add Python to PATH"**.
2. Install VS Code and the **Python** extension.
3. Open the `library-chatbot` folder in VS Code (File → Open Folder).
4. Open the terminal (Terminal → New Terminal).
5. Terminal chatbot:
   ```
   python library_chatbot.py
   ```
6. Web chatbot:
   ```
   pip install -r requirements.txt
   streamlit run app.py
   ```
   The browser opens at http://localhost:8501.

## Upload to GitHub
**Option A – GitHub website (easiest)**
1. Sign in at https://github.com → click **+** → **New repository**.
2. Name it `library-chatbot`, choose **Public**, click **Create repository**.
3. Click **uploading an existing file**, drag in all project files and the `report` folder, then **Commit changes**.

**Option B – VS Code**
1. Install Git from https://git-scm.com.
2. In VS Code, open the Source Control panel → **Publish to GitHub** → sign in → choose Public.

Your repository URL appears in the browser address bar, e.g. `https://github.com/<your-username>/library-chatbot`.

## Deploy Free on Streamlit Community Cloud
1. Go to https://share.streamlit.io and sign in with GitHub.
2. Click **Create app** → select your repository, branch `main`, main file `app.py`.
3. Click **Deploy**. After a minute you get a live URL like `https://<something>.streamlit.app`.

## Submission Checklist (GMIU Web Portal)
- [ ] Names and enrollment numbers filled in README and report
- [ ] Code runs with `python library_chatbot.py`
- [ ] Web app runs with `streamlit run app.py`
- [ ] Project uploaded to GitHub (public)
- [ ] App deployed on Streamlit Cloud and link tested
- [ ] GitHub and live links written into the report
- [ ] Report PDF saved in `report/` and uploaded on the portal
