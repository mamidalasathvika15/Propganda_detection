import pandas as pd
import re

# Load sentences
df = pd.read_csv("sentences_with_offsets.csv")
df["label"] = 0

# Simple propaganda cue words
propaganda_keywords = [
    "must", "never", "always", "danger", "threat",
    "enemy", "evil", "corrupt", "shocking",
    "disaster", "crisis", "urgent", "destroy",
    "attack", "fear", "propaganda"
]

def is_propaganda(sentence):
    sentence = sentence.lower()
    return any(word in sentence for word in propaganda_keywords)

# Assign labels
for idx, row in df.iterrows():
    if is_propaganda(row["sentence_text"]):
        df.at[idx, "label"] = 1

# Save
df.to_csv("task1_sentences_labeled.csv", index=False)

print(" Final dataset created")
print("\nLabel distribution:")
print(df["label"].value_counts())
