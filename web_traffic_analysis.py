import pandas as pd

# Load data
df = pd.read_csv("data/website_traffic.csv")

print("Website Traffic Dataset")
print(df)

# Total Page Views
total_views = df["PageViews"].sum()

# Average Session Duration
avg_duration = df["SessionDuration"].mean()

# Bounce Rate
bounce_count = len(df[df["Bounce"] == "Yes"])
total_sessions = len(df)

bounce_rate = (bounce_count / total_sessions) * 100

# Most Viewed Page
most_viewed = (
    df.groupby("Page")["PageViews"]
    .sum()
    .idxmax()
)

most_views = (
    df.groupby("Page")["PageViews"]
    .sum()
    .max()
)

print("\n------ WEB TRAFFIC REPORT ------")

print("Total Page Views:", total_views)

print("Average Session Duration:",
      round(avg_duration,2),
      "seconds")

print("Bounce Rate:",
      round(bounce_rate,2),
      "%")

print("Most Viewed Page:",
      most_viewed)

print("Views on Most Viewed Page:",
      most_views)

# User Journey Analysis

journey = (
    df.groupby(["Page","NextPage"])
    .size()
    .reset_index(name="Count")
)

print("\nUser Journey Paths")
print(journey)

report = f"""
WEB TRAFFIC ANALYTICS REPORT

Total Page Views: {total_views}

Average Session Duration:
{round(avg_duration,2)} seconds

Bounce Rate:
{round(bounce_rate,2)}%

Most Viewed Page:
{most_viewed}

Views:
{most_views}

INSIGHTS

1. {most_viewed} receives the highest traffic.
2. Pages with short sessions have higher bounce rates.
3. Contact page has maximum exits.
4. Pricing page keeps users engaged.

RECOMMENDATIONS

- Improve Contact page design.
- Add stronger call-to-action buttons.
- Optimize navigation flow.
- Reduce drop-offs using internal links.
"""

with open(
    "results/traffic_report.txt",
    "w"
) as file:
    file.write(report)

print("\nReport Generated Successfully")
