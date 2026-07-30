-- Transform raw ER visit data into an analytics-ready view

CREATE OR REPLACE VIEW PORTFOLIO_DB.ANALYTICS.ER_VISITS_CLEAN AS
SELECT
    year::INTEGER AS year,
    measure_type,
    leading_10_ranking::INTEGER AS leading_10_ranking,
    measure,
    demographic_group,
    subgroup,
    estimate_type,
    visit_count,
    se,
    ci_low,
    ci_high,
    CASE
        WHEN reliable = 'Yes' THEN TRUE
        WHEN reliable = 'No' THEN FALSE
        ELSE NULL
    END AS is_reliable
FROM PORTFOLIO_DB.RAW.ER_VISITS;

-- Validate transformed view
USE SCHEMA PORTFOLIO_DB.ANALYTICS;

SELECT *
FROM ER_VISITS_CLEAN
LIMIT 10;