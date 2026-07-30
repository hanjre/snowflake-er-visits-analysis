from config import get_connection
import pandas as pd
import matplotlib.pyplot as plt

conn = get_connection()

query = """
SELECT
    year,
    visit_count,
    LAG(visit_count) OVER (ORDER BY year) AS previous_year,
    visit_count - LAG(visit_count) OVER (ORDER BY year) AS absolute_change,
    ROUND(
        100 * (
            visit_count / LAG(visit_count) OVER (ORDER BY year) - 1
        ),
        2
    ) AS pct_change
FROM ER_VISITS_CLEAN
WHERE measure = 'All diagnoses'
  AND demographic_group = 'Total'
  AND subgroup = 'All visits'
  AND estimate_type = 'Visit count'
  AND is_reliable = TRUE
ORDER BY year;
"""

try:
    df = pd.read_sql(query, conn)
finally:
    conn.close()

print("\nER Visit Trends")
print(df.to_string(index=False))

# Export analytical result
df.to_csv("outputs/er_visit_trends.csv", index=False)

# Plot visits in millions
df["VISITS_MILLIONS"] = df["VISIT_COUNT"] / 1_000_000

plt.figure(figsize=(10, 6))
plt.plot(
    df["YEAR"],
    df["VISITS_MILLIONS"],
    marker="o",
    linewidth=2
)

plt.title("U.S. Emergency Department Visits, 2016–2022")
plt.xlabel("Year")
plt.ylabel("Visits (millions)")
plt.grid(alpha=0.25)
plt.tight_layout()

plt.savefig(
    "outputs/er_visit_trends.png",
    dpi=200,
    bbox_inches="tight"
)

plt.show()

print("\nCreated:")
print("outputs/er_visit_trends.csv")
print("outputs/er_visit_trends.png")