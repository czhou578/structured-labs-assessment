from preswald import text, plotly, connect, get_df, table, text, slider, query
import pandas as pd
import plotly.express as px

text("# Welcome to Preswald!")
text("This is my first app using Preswald. 🎉")

# Load the CSV
connect()  # load in all sources, which by default is the sample_csv
# Add this right after get_df to check if data was loaded
df = get_df('sample_csv')
if df is None:
    text("❌ Failed to load data. Check if the file exists.")
    # Provide a fallback or exit early
else:
    text(f"✅ Data loaded successfully with {len(df)} rows")

sql = "SELECT * FROM sample_csv WHERE Age > 50"
filtered_df = query(sql, "sample_csv")

text("# My Data Analysis App")
table(filtered_df, title="Filtered Data")

threshold = slider("BMI Threshold", min_val=0, max_val=100, default=50)
table(df[df["BMI"] > threshold], title="Dynamic Data View")

# ✅ Corrected Plot
fig = px.scatter(df, x="Height_cm", y="BMI", color="Gender", title="Height vs. BMI")
plotly(fig)
