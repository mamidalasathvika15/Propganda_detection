import pandas as pd
import re
import os

#  PATH HANDLING (ROBUST) 
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "task1_sentences_labeled.csv")

#  LOAD TASK-1 OUTPUT 
df = pd.read_csv(DATA_PATH)

# Only propaganda sentences
prop_df = df[df["label"] == 1].copy()

#  TECHNIQUE KEYWORDS 
TECHNIQUES = {
    "Loaded Language": [
        "shocking", "disaster", "crisis", "evil", "corrupt",
        "danger", "destroy", "threat", "horrible", "terrible"
    ],
    "Fear Appeal": [
        "danger", "threat", "attack", "destroy", "fear",
        "risk", "catastrophe", "crisis"
    ],
    "Name Calling": [
        "enemy", "traitor", "corrupt", "evil", "criminal", "liar"
    ],
    "Exaggeration": [
        "always", "never", "everyone", "no one", "completely", "totally"
    ],
    "Appeal to Authority": [
        "experts say", "scientists say", "according to",
        "research shows", "officials say"
    ],
    "Black-and-White Thinking": [
        "either", "or else", "only choice", "no alternative"
    ]
}

# TEXT NORMALIZATION 
def normalize(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

# TECHNIQUE DETECTION 
def detect_techniques(sentence):
    sentence = normalize(sentence)
    detected = []

    for technique, keywords in TECHNIQUES.items():
        for kw in keywords:
            if kw in sentence:
                detected.append(technique)
                break

    if not detected:
        detected.append("General Persuasion")

    return ", ".join(detected)

# Apply Task-2
prop_df["technique"] = prop_df["sentence_text"].apply(detect_techniques)

#  SAVE OUTPUT 
OUTPUT_FILE = os.path.join(BASE_DIR, "task2_sentences_with_techniques.csv")
prop_df.to_csv(OUTPUT_FILE, index=False)

print("Task-2 Technique Classification Completed")
print(" Saved as:", OUTPUT_FILE)
print("\nSample output:")
print(prop_df[["sentence_text", "technique"]].head(5))
