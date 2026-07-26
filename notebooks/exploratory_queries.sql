-- Exploratory Queries for Nifty 100 Financial Analytics
SELECT company_id, roe, roce, debt_to_equity 
FROM financial_ratios 
WHERE year = 2024 
ORDER BY roe DESC 
LIMIT 10;
