import pandas as pd

df = pd.read_csv("sentences_with_risk_scores.csv")

high_risk = df[df["risk_score"] >= 60]

print("🔥 High Risk Propaganda Sentences:\n")

for _, row in high_risk.head(5).iterrows():
    print("Sentence:", row["sentence_text"])
    print("Technique:", row["technique"])
    print("Risk Score:", row["risk_score"])
    print("-" * 50)


