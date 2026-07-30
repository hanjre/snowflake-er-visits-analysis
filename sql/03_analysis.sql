-- Analyze annual U.S. emergency department visit trends

USE DATABASE PORTFOLIO_DB;
USE SCHEMA ANALYTICS;
USE WAREHOUSE COMPUTE_WH;

-- Annual visit totals with confidence intervals
SELECT
    year,
    visit_count,
    ci_low,
    ci_high
FROM ER_VISITS_CLEAN
WHERE measure = 'All diagnoses'
  AND demographic_group = 'Total'
  AND subgroup = 'All visits'
  AND estimate_type = 'Visit count'
  AND is_reliable = TRUE
ORDER BY year;


-- Year-over-year change
WITH annual_visits AS (
    SELECT
        year,
        visit_count
    FROM ER_VISITS_CLEAN
    WHERE measure = 'All diagnoses'
      AND demographic_group = 'Total'
      AND subgroup = 'All visits'
      AND estimate_type = 'Visit count'
      AND is_reliable = TRUE
)

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
FROM annual_visits
ORDER BY year;