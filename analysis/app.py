import streamlit as st
import pandas as pd
import re
from risk_scoring import calculate_risk_score


# Technique detection
def classify_technique(sentence):

    sentence = sentence.lower()

    if any(word in sentence for word in ["fear", "danger", "threat", "risk"]):
        return "Fear Appeal"

    elif any(word in sentence for word in ["corrupt", "failure", "disaster"]):
        return "Name Calling"

    elif any(word in sentence for word in ["shocking", "terrible", "amazing"]):
        return "Loaded Language"

    elif any(word in sentence for word in ["always", "never", "everyone"]):
        return "Exaggeration"

    elif any(word in sentence for word in ["experts say", "according to", "researchers"]):
        return "Appeal to Authority"

    elif any(word in sentence for word in ["either", "or"]):
        return "Black-and-White Thinking"

    else:
        return "General Persuasion"


# Explanation generator
def generate_explanation(technique):

    explanations = {
        "Fear Appeal": "Creates fear to influence opinion.",
        "Name Calling": "Uses insulting labels to attack a target.",
        "Loaded Language": "Uses emotionally strong wording.",
        "Exaggeration": "Overstates facts to strengthen claims.",
        "Appeal to Authority": "Relies on authority instead of evidence.",
        "Black-and-White Thinking": "Presents only extreme choices."
    }

    return explanations.get(
        technique,
        "No strong propaganda indicators detected."
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


# ---------------- STREAMLIT UI ----------------

st.title("🧠 Propaganda Detection System")
st.write("Paste a paragraph to detect propaganda techniques sentence-by-sentence.")

user_input = st.text_area("Enter text to analyze:")

if st.button("Analyze"):

    if user_input.strip() == "":
        st.warning("Please enter some text.")

    else:

        # Split paragraph into sentences
        sentences = re.split(r'(?<=[.!?])\s+', user_input.strip())

        results = []

        st.subheader("Results")

        for sentence in sentences:

            if sentence.strip() == "":
                continue

            technique = classify_technique(sentence)
            risk_score, risk_level = calculate_risk_score(technique)
            explanation = generate_explanation(technique)
            rewrite = neutral_rewrite(sentence)

            st.markdown(f"### Sentence: {sentence}")

            st.write("Technique:", technique)
            st.write("Risk Score:", risk_score)

            st.progress(risk_score)

            if risk_level == "LOW":
                st.success(f"Risk Level: {risk_level}")
            elif risk_level == "MEDIUM":
                st.warning(f"Risk Level: {risk_level}")
            else:
                st.error(f"Risk Level: {risk_level}")

            st.info(explanation)
            st.success(f"Neutral Rewrite: {rewrite}")

            results.append({
                "Sentence": sentence,
                "Technique": technique,
                "Risk Score": risk_score,
                "Risk Level": risk_level,
                "Explanation": explanation,
                "Neutral Rewrite": rewrite
            })

        # Download CSV report
        results_df = pd.DataFrame(results)

        st.download_button(
            label="Download Full Analysis Report (CSV)",
            data=results_df.to_csv(index=False),
            file_name="propaganda_paragraph_analysis.csv",
            mime="text/csv"
        )


        