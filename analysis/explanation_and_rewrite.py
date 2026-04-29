# explanation_and_rewrite.py

import pandas as pd
from risk_scoring import calculate_risk_score


# Explanation generator
def generate_explanation(technique):

    explanations = {
        "Fear Appeal": "This sentence attempts to create fear to influence opinion.",
        "Name Calling": "This sentence uses insulting language to attack a target.",
        "Loaded Language": "This sentence uses emotionally strong wording to influence perception.",
        "Exaggeration": "This sentence overstates facts to strengthen its claim.",
        "Appeal to Authority": "This sentence relies on authority instead of evidence.",
        "Black-and-White Thinking": "This sentence presents only two extreme choices.",
    }

    return explanations.get(
        technique,
        "This sentence contains persuasive language."
    )


# Neutral rewrite generator
def neutral_rewrite(sentence):

    replacements = {
        "terrible": "concerning",
        "dangerous": "serious",
        "crisis": "issue",
        "destroying": "affecting",
        "shocking": "unexpected",
        "extremely": "",
        "very": ""
    }

    words = sentence.split()

    updated_words = []

    for word in words:

        clean_word = word.lower()

        if clean_word in replacements:
            updated_words.append(replacements[clean_word])
        else:
            updated_words.append(word)

    return " ".join(updated_words)


# MAIN PROCESSING FUNCTION
def process_file():

    input_file = "task2_sentences_with_techniques.csv"
    output_file = "final_explainable_output.csv"

    df = pd.read_csv(input_file)

    output_rows = []

    for _, row in df.iterrows():

        sentence = row["sentence_text"]
        technique = row["technique"]

        # If multiple techniques exist, pick first one
        technique = technique.split(",")[0].strip()

        risk_score, risk_level = calculate_risk_score(technique)

        explanation = generate_explanation(technique)

        rewrite = neutral_rewrite(sentence)

        output_rows.append([
            sentence,
            technique,
            risk_score,
            risk_level,
            explanation,
            rewrite
        ])

    output_df = pd.DataFrame(
        output_rows,
        columns=[
            "Sentence",
            "Technique",
            "Risk Score",
            "Risk Level",
            "Explanation",
            "Neutral Rewrite"
        ]
    )

    output_df.to_csv(output_file, index=False)

    print("✅ File generated successfully:", output_file)


# RUN SCRIPT
if __name__ == "__main__":
    process_file()