SELECT COUNT(*), AVG(t2mean2m_delta), AVG(ABS(t2mean2m_delta)) FROM fact_prediction;
SELECT COUNT(*), AVG(t2mean2m_delta), AVG(ABS(t2mean2m_delta)) FROM fact_prediction WHERE prediction_length >= 4 AND prediction_length <= 6;
SELECT COUNT(*), AVG(t2mean2m_delta), AVG(ABS(t2mean2m_delta)) FROM fact_prediction WHERE prediction_length >= 7 AND prediction_length <= 12;
SELECT COUNT(*), AVG(t2mean2m_delta), AVG(ABS(t2mean2m_delta)) FROM fact_prediction WHERE prediction_length >= 13 AND prediction_length <= 18;
SELECT COUNT(*), AVG(t2mean2m_delta), AVG(ABS(t2mean2m_delta)) FROM fact_prediction WHERE prediction_length >= 19 AND prediction_length <= 24;
SELECT COUNT(*), AVG(t2mean2m_delta), AVG(ABS(t2mean2m_delta)) FROM fact_prediction WHERE prediction_length >= 25 AND prediction_length <= 30;
SELECT COUNT(*), AVG(t2mean2m_delta), AVG(ABS(t2mean2m_delta)) FROM fact_prediction WHERE prediction_length >= 31 AND prediction_length <= 36;
SELECT COUNT(*), AVG(t2mean2m_delta), AVG(ABS(t2mean2m_delta)) FROM fact_prediction WHERE prediction_length >= 37 AND prediction_length <= 41;