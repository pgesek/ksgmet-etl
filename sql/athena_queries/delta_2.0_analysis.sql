SELECT
    COUNT(*) AS 'count',
    AVG(t2mean2m_delta) AS 'average t2mean2m delta',
    AVG(ABS(t2mean2m_delta)) AS 'average abs t2mean2m delta',
    AVG(acm_total_percip_actual) AS 'average actual total percip',
    AVG(acm_total_percip_predicted) AS 'average predicted total percip',
    AVG(acm_convective_percip_actual) AS 'average actual convective percip',
    AVG(acm_convective_percip_predicted) AS 'average predicted convective percip',
    AVG(prediction_length) AS 'average prediction length',
    t2mean2m_delta > 2.0 AS 't2mean2m delta > 2.0'
FROM november
GROUP BY t2mean2m_delta > 2.0