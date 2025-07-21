# 🛡️ Shield AI - Real-Time Cyberbullying Detection

A Flask-based web application that uses an LSTM deep learning model to detect cyberbullying in real-time based on user-submitted text.

## 🚀 Features

- 🔍 Detects whether a message contains cyberbullying or not.
- ✅ Shows confidence score for each prediction.
- 📣 Allows anonymous reporting of flagged messages.
- ✨ Clean, simple HTML frontend.
- 🧠 Trained using LSTM with preprocessed and tokenized text data.

## 📂 Project Structure
cyber/
├── app.py # Flask backend
├── lstm_bully_detector.keras # Trained LSTM model
├── tokenizer.pickle # Tokenizer used during training
├── templates/
│ └── index.html # Frontend HTML page
├── reports.txt # Stores reported messages
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## 🧪 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/cyberbullying-detection.git
   cd cyberbullying-detection
2. Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install requirements:
pip install -r requirements.txt
4. Run the app:
python app.py
5. Open in browser:
http://127.0.0.1:5000/
##Future Ideas
Add login for moderators
Create a dashboard to review reports
Add charts for cyberbullying trends
