SELECT COUNT(*) AS claim_count
FROM enterprise_data_platform_dev.claims_silver;

SELECT claim_status, COUNT(*) AS status_count
FROM enterprise_data_platform_dev.claims_silver
GROUP BY claim_status
ORDER BY claim_status;

SELECT provider_id, SUM(claim_amount) AS total_claim_amount
FROM enterprise_data_platform_dev.claims_silver
GROUP BY provider_id
ORDER BY total_claim_amount DESC;

SELECT *
FROM enterprise_data_platform_dev.claims_silver
ORDER BY claim_id;
