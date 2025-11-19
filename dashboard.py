import pandas as pd
import matplotlib.pyplot as plt
import os

# Ensure output directory exists
os.makedirs("output", exist_ok=True)

# Load trend data
df = pd.read_csv("data/trends.csv")

# Group by category
category_scores = df.groupby("category")["score"].mean().sort_values(ascending=False)

# Top 8 individual trends
top_trends = df.sort_values(by="score", ascending=False).head(8)

# Generate bar chart for category scores
plt.figure(figsize=(8, 5))
category_scores.plot(kind="bar")
plt.title("Average Trend Score by Category")
plt.xlabel("Category")
plt.ylabel("Average Score")
plt.tight_layout()
plt.savefig("output/category_scores.png")
plt.close()

# Generate bar chart for top trends
plt.figure(figsize=(10, 5))
plt.barh(top_trends["trend"], top_trends["score"])
plt.title("Top 8 Fashion Trends")
plt.xlabel("Trend Score")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("output/top_trends.png")
plt.close()

# Generate HTML report
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Fashion Trend Dashboard</title>
    <style>
        body {{
            font-family: 'Helvetica Neue', Arial, sans-serif;
            background-color: #f8f8f8;
            margin: 40px;
            color: #333;
        }}
        h1 {{
            text-align: center;
            font-size: 36px;
            color: #111;
        }}
        h2 {{
            color: #222;
            margin-top: 40px;
        }}
        .chart {{
            margin: 30px auto;
            text-align: center;
        }}
        img {{
            width: 80%;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.15);
        }}
        .footer {{
            margin-top: 50px;
            font-size: 14px;
            text-align: center;
            color: #555;
        }}
    </style>
</head>

<body>

    <h1>Fashion Trend Dashboard</h1>

    <h2>Average Trend Score by Category</h2>
    <div class="chart">
        <img src="category_scores.png" alt="Category Scores Chart">
    </div>

    <h2>Top 8 Trending Items</h2>
    <div class="chart">
        <img src="top_trends.png" alt="Top Trends Chart">
    </div>

    <div class="footer">
        <p>Generated automatically using Python, Pandas & Matplotlib.</p>
        <p>Created by Yharelis Ribic — Fashion Tech & Digital Media.</p>
    </div>

</body>
</html>
"""

# Write HTML file
with open("output/report.html", "w") as f:
    f.write(html_content)

print("Dashboard generated! Check the 'output' folder for report.html")

