import pandas as pd
import matplotlib.pyplot as plt

# Load output file
df = pd.read_csv("final_explainable_output.csv")

# Technique Frequency Bar Chart


technique_counts = df["Technique"].value_counts()

plt.figure(figsize=(8,5))
technique_counts.plot(kind="bar")
plt.title("Technique Frequency Distribution")
plt.xlabel("Technique")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("technique_frequency_bar_chart.png")
plt.close()



# Risk Level Pie Chart


risk_counts = df["Risk Level"].value_counts()

plt.figure(figsize=(6,6))
risk_counts.plot(kind="pie", autopct="%1.1f%%")
plt.title("Risk Level Distribution")
plt.ylabel("")

plt.savefig("risk_level_pie_chart.png")
plt.close()


print("✅ Charts generated successfully!")