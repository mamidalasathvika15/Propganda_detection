import os
import pandas as pd
import nltk

ARTICLES_DIR = "data/articles"
OUTPUT_FILE = "sentences_with_offsets.csv"

records = []

for filename in os.listdir(ARTICLES_DIR):
    if not filename.endswith(".txt"):
        continue

    article_id = filename.replace(".txt", "")
    file_path = os.path.join(ARTICLES_DIR, filename)

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    sentences = nltk.sent_tokenize(text)

    cursor = 0
    sentence_id = 0

    for sent in sentences:
        start = text.find(sent, cursor)
        if start == -1:
            continue

        end = start + len(sent)
        cursor = end

        records.append({
            "article_id": article_id,
            "sentence_id": sentence_id,
            "sentence_text": sent,
            "start_char": start,
            "end_char": end
        })

        sentence_id += 1

df = pd.DataFrame(records)
df.to_csv(OUTPUT_FILE, index=False)

print(f" Extracted {len(df)} sentences")
print(f" Saved to {OUTPUT_FILE}")
