SELECT MIN(t2mean2m_predicted), MIN(tmin2m_predicted), MIN(tmax2m_predicted),
	   MAX(t2mean2m_predicted), MAX(tmin2m_predicted), MAX(tmax2m_predicted) 
FROM fact_prediction;
