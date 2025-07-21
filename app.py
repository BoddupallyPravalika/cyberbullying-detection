from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import re
import string
import os

app = Flask(__name__)

# Load model and tokenizer
model_path = "lstm_bully_detector.keras"
tokenizer_path = "tokenizer.pickle"

if not os.path.exists(model_path) or not os.path.exists(tokenizer_path):
    raise FileNotFoundError("Model or tokenizer file is missing.")

model = load_model(model_path)

with open(tokenizer_path, 'rb') as handle:
    tokenizer = pickle.load(handle)

max_length = 100

# Text cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\n', ' ', text)
    return text.strip()

# Optional: Known safe phrases
safe_phrases = [
    "i support you", "stay strong", "you are amazing", "good luck",
    "congratulations", "well done", "you got this", "keep going"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    cleaned = clean_text(message)

    if cleaned in safe_phrases:
        return render_template('index.html',
                               prediction='Not Cyberbullying ✅',
                               confidence=99.9,
                               message=message)

    seq = tokenizer.texts_to_sequences([cleaned])
    padded = pad_sequences(seq, maxlen=max_length, padding='post')

    pred = float(model.predict(padded).squeeze())
    result = 'Cyberbullying 🚫' if pred >= 0.5 else 'Not Cyberbullying ✅'
    confidence = round(pred * 100, 2)

    return render_template('index.html',
                           prediction=result,
                           confidence=confidence,
                           message=message)

@app.route('/report', methods=['POST'])
def report():
    message = request.form['reported_message']
    reason = request.form.get('reason', 'No reason provided.')

    with open('reports.txt', 'a') as file:
        file.write(f"Reported Message: {message}\n")
        file.write(f"Reason: {reason}\n")
        file.write("-" * 40 + "\n")

    support_msg = "✅ Thank you. Your report has been received anonymously."
    return render_template('index.html', support=support_msg)

if __name__ == '__main__':
    app.run(debug=True)
