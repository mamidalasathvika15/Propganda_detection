# Propaganda Detection System

An explainable NLP-based platform that detects propaganda techniques in text, assigns a severity risk score (0–100), highlights evidence sentences, and suggests neutral rewrites for better decision support.

This system moves beyond simple classification by combining detection, risk estimation, explanation, and response generation into a single pipeline.

---

## Features

- Detects propaganda techniques using transformer-based NLP models (BERT / RoBERTa)
- Assigns severity-based risk scores (0–100 scale)
- Highlights propaganda-triggering sentences
- Generates human-readable explanations
- Suggests neutral rewrite alternatives
- Interactive interface for testing input text (Streamlit app)

---

## Project Pipeline

Input Text  
→ Preprocessing  
→ Propaganda Technique Detection  
→ Risk Scoring (0–100)  
→ Explanation Generation  
→ Sentence Highlighting  
→ Neutral Rewrite Suggestions

---

## Tech Stack

- Python
- HuggingFace Transformers
- PyTorch / Scikit-learn
- Pandas
- NumPy
- Streamlit

---

## Folder Structure

propaganda-detection-system/
│
├── app.py
├── src/
├── data/
├── demo/
├── requirements.txt
└── README.md

---

## How to Run the Project

Clone the repository:

git clone [https://github.com/yourusername/propaganda-detection-system.git](https://github.com/mamidalasathvika15/Propganda_detection)

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

---

## Dataset

The model is trained using a propaganda detection dataset (for example, the SemEval Propaganda Dataset).

Due to size limitations, the full dataset is not included in this repository.

A small sample dataset is available inside the data/ folder for testing.

---

## Example Use Case

Input:

"Our country is under threat because of these people."

Output:

- Technique detected: Fear Appeal
- Risk score: 78/100
- Explanation: Uses emotional pressure to influence audience perception
- Suggested rewrite: Provide evidence-based reasoning without emotional exaggeration

---

## Demo

![Demo Screenshot](demo/demo.png)
please refer the demo folder for results.

---

## Future Improvements

- Add multi-language propaganda detection
- Deploy model using FastAPI
- Integrate real-time news and social media analysis
- Improve explanation interpretability
- Add dashboard visualization for analytics

---

## Applications

- Journalism verification workflows
- Social media moderation
- Election misinformation monitoring
- Educational tools for media literacy
- Policy and governance research support
