# risk_scoring.py

def calculate_risk_score(technique):
    """
    Calculates propaganda risk score based on detected technique
    and assigns LOW / MEDIUM / HIGH risk levels.
    """

   
    base_score = 20

    
    technique_weights = {
        "Fear Appeal": 45,              # HIGH 
        "Name Calling": 35,             # HIGH 
        "Loaded Language": 30,          # MEDIUM
        "Exaggeration": 30,             # MEDIUM        
        "Appeal to Authority": 25,      # MEDIUM 
        "Black-and-White Thinking": 35, # HIGH 
        "General Persuasion": 0         # LOW 
    }

    # Calculate final score
    risk_score = base_score + technique_weights.get(technique, 0)

    # Cap score at 100
    risk_score = min(risk_score, 100)

    # Assign risk level
    if risk_score <= 30:
        risk_level = "LOW"
    elif risk_score <= 60:
        risk_level = "MEDIUM"
    else:
        risk_level = "HIGH"

    return risk_score, risk_level


# Test block
if __name__ == "__main__":
    sample = "Fear Appeal"
    score, level = calculate_risk_score(sample)

    print("Technique:", sample)
    print("Risk Score:", score)
    print("Risk Level:", level)

    