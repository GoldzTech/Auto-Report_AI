import pandas as pd
from report import generate_report
from ai_summary import generate_summary_ai

def main():
    #1. Load data
    df = pd.read_csv("data.csv")

    #2. Calculate metrics
    total = df["value"].sum()
    average = df["value"].mean()
    highest = df["value"].max()

    #3. Generate AI summary
    print("💡Generating AI summary...")
    summary = generate_summary_ai(total, average, highest)

    #4. Generate PDF
    generate_report(total, average, highest, summary)
    print("✅ Report generated successfully! Check 'report.pdf'.")

if __name__ == "__main__":
    main()
    