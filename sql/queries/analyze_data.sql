/* All data */

SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta" FROM fact_prediction;
SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta 4h-6h", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta 4h-6h" FROM fact_prediction WHERE prediction_length >= 4 AND prediction_length <= 6;
SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta 7h-12h", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta 7h-12h" FROM fact_prediction WHERE prediction_length >= 7 AND prediction_length <= 12;
SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta 13h-18h", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta 13h-18h" FROM fact_prediction WHERE prediction_length >= 13 AND prediction_length <= 18;
SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta 19h-24h", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta 19h-24h" FROM fact_prediction WHERE prediction_length >= 19 AND prediction_length <= 24;
SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta 25h-30h", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta 25h-30h" FROM fact_prediction WHERE prediction_length >= 25 AND prediction_length <= 30;
SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta 31h-36h", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta 31h-36h" FROM fact_prediction WHERE prediction_length >= 31 AND prediction_length <= 36;
SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta 37h-41h", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta 37h-41h" FROM fact_prediction WHERE prediction_length >= 37 AND prediction_length <= 41;

SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta" FROM fact_prediction;
SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta 4h-6h", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta 4h-6h" FROM fact_prediction WHERE prediction_length >= 4 AND prediction_length <= 6;
SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta 7h-12h", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta 7h-12h" FROM fact_prediction WHERE prediction_length >= 7 AND prediction_length <= 12;
SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta 13h-18h", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta 13h-18h" FROM fact_prediction WHERE prediction_length >= 13 AND prediction_length <= 18;
SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta 19h-24h", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta 19h-24h" FROM fact_prediction WHERE prediction_length >= 19 AND prediction_length <= 24;
SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta 25h-30h", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta 25h-30h" FROM fact_prediction WHERE prediction_length >= 25 AND prediction_length <= 30;
SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta 31h-36h", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta 31h-36h" FROM fact_prediction WHERE prediction_length >= 31 AND prediction_length <= 36;
SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta 37h-41h", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta 37h-41h" FROM fact_prediction WHERE prediction_length >= 37 AND prediction_length <= 41;

/* 2018-10-27 to 2018-12-31 */

SELECT COUNT(*), AVG(t2mean2m_delta) AS "AVG t2mean2m_delta", AVG(ABS(t2mean2m_delta)) AS "AVG ABS t2mean2m_delta" FROM fact_prediction WHERE prediction_date >= 57 AND prediction_date <= 122;
SELECT COUNT(*), AVG(t2mean2m_delta) AS "AVG t2mean2m_delta 4h-6h", AVG(ABS(t2mean2m_delta)) AS "AVG ABS t2mean2m_delta 4h-6h" FROM fact_prediction WHERE prediction_length >= 4 AND prediction_length <= 6 AND prediction_date >= 57 AND prediction_date <= 122;
SELECT COUNT(*), AVG(t2mean2m_delta) AS "AVG t2mean2m_delta 7h-12h", AVG(ABS(t2mean2m_delta)) AS "AVG ABS t2mean2m_delta 7h-12h" FROM fact_prediction WHERE prediction_length >= 7 AND prediction_length <= 12 AND prediction_date >= 57 AND prediction_date <= 122;
SELECT COUNT(*), AVG(t2mean2m_delta) AS "AVG t2mean2m_delta 13h-18h", AVG(ABS(t2mean2m_delta)) AS "AVG ABS t2mean2m_delta 13h-18h" FROM fact_prediction WHERE prediction_length >= 13 AND prediction_length <= 18 AND prediction_date >= 57 AND prediction_date <= 122;
SELECT COUNT(*), AVG(t2mean2m_delta) AS "AVG t2mean2m_delta 19h-24h", AVG(ABS(t2mean2m_delta)) AS "AVG ABS t2mean2m_delta 19h-24h" FROM fact_prediction WHERE prediction_length >= 19 AND prediction_length <= 24 AND prediction_date >= 57 AND prediction_date <= 122;
SELECT COUNT(*), AVG(t2mean2m_delta) AS "AVG t2mean2m_delta 25h-30h", AVG(ABS(t2mean2m_delta)) AS "AVG ABS t2mean2m_delta 25h-30h" FROM fact_prediction WHERE prediction_length >= 25 AND prediction_length <= 30 AND prediction_date >= 57 AND prediction_date <= 122;
SELECT COUNT(*), AVG(t2mean2m_delta) AS "AVG t2mean2m_delta 31h-36h", AVG(ABS(t2mean2m_delta)) AS "AVG ABS t2mean2m_delta 31h-36h" FROM fact_prediction WHERE prediction_length >= 31 AND prediction_length <= 36 AND prediction_date >= 57 AND prediction_date <= 122;
SELECT COUNT(*), AVG(t2mean2m_delta) AS "AVG t2mean2m_delta 37h-41h", AVG(ABS(t2mean2m_delta)) AS "AVG ABS t2mean2m_delta 37h-41h" FROM fact_prediction WHERE prediction_length >= 37 AND prediction_length <= 41 AND prediction_date >= 57 AND prediction_date <= 122;

SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta" FROM fact_prediction WHERE prediction_date >= 57 AND prediction_date <= 122;
SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta 4h-6h", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta 4h-6h1" FROM fact_prediction WHERE prediction_length >= 4 AND prediction_length <= 6 AND prediction_date >= 57 AND prediction_date <= 122;
SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta 7h-12h", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta 7h-12h" FROM fact_prediction WHERE prediction_length >= 7 AND prediction_length <= 12 AND prediction_date >= 57 AND prediction_date <= 122;
SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta 13h-18h", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta 13h-18h" FROM fact_prediction WHERE prediction_length >= 13 AND prediction_length <= 18 AND prediction_date >= 57 AND prediction_date <= 122;
SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta 19h-24h", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta 19h-24h" FROM fact_prediction WHERE prediction_length >= 19 AND prediction_length <= 24 AND prediction_date >= 57 AND prediction_date <= 122;
SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta 25h-30h", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta 25h-30h" FROM fact_prediction WHERE prediction_length >= 25 AND prediction_length <= 30 AND prediction_date >= 57 AND prediction_date <= 122;
SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta 31h-36h", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta 31h-36h" FROM fact_prediction WHERE prediction_length >= 31 AND prediction_length <= 36 AND prediction_date >= 57 AND prediction_date <= 122;
SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta 37h-41h", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta 37h-41h" FROM fact_prediction WHERE prediction_length >= 37 AND prediction_length <= 41 AND prediction_date >= 57 AND prediction_date <= 122;

SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta" FROM fact_prediction;
SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta 4h-6h", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta 4h-6h" FROM fact_prediction WHERE prediction_length >= 4 AND prediction_length <= 6 AND prediction_date >= 57 AND prediction_date <= 122;
SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta 7h-12h", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta 7h-12h" FROM fact_prediction WHERE prediction_length >= 7 AND prediction_length <= 12 AND prediction_date >= 57 AND prediction_date <= 122;
SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta 13h-18h", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta 13h-18h" FROM fact_prediction WHERE prediction_length >= 13 AND prediction_length <= 18 AND prediction_date >= 57 AND prediction_date <= 122;
SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta 19h-24h", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta 19h-24h" FROM fact_prediction WHERE prediction_length >= 19 AND prediction_length <= 24 AND prediction_date >= 57 AND prediction_date <= 122;
SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta 25h-30h", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta 25h-30h" FROM fact_prediction WHERE prediction_length >= 25 AND prediction_length <= 30 AND prediction_date >= 57 AND prediction_date <= 122;
SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta 31h-36h", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta 31h-36h" FROM fact_prediction WHERE prediction_length >= 31 AND prediction_length <= 36 AND prediction_date >= 57 AND prediction_date <= 122;
SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta 37h-41h", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta 37h-41h" FROM fact_prediction WHERE prediction_length >= 37 AND prediction_length <= 41 AND prediction_date >= 57 AND prediction_date <= 122;

/* 2019-01-01 to 2019-02-28 */

SELECT COUNT(*), AVG(t2mean2m_delta) AS "AVG t2mean2m_delta", AVG(ABS(t2mean2m_delta)) AS "AVG ABS t2mean2m_delta" FROM fact_prediction WHERE prediction_date >= 123 AND prediction_date <= 181;
SELECT COUNT(*), AVG(t2mean2m_delta) AS "AVG t2mean2m_delta 4h-6h", AVG(ABS(t2mean2m_delta)) AS "AVG ABS t2mean2m_delta 4h-6h" FROM fact_prediction WHERE prediction_length >= 4 AND prediction_length <= 6 AND prediction_date >= 123 AND prediction_date <= 181;
SELECT COUNT(*), AVG(t2mean2m_delta) AS "AVG t2mean2m_delta 7h-12h", AVG(ABS(t2mean2m_delta)) AS "AVG ABS t2mean2m_delta 7h-12h" FROM fact_prediction WHERE prediction_length >= 7 AND prediction_length <= 12 AND prediction_date >= 123 AND prediction_date <= 181;
SELECT COUNT(*), AVG(t2mean2m_delta) AS "AVG t2mean2m_delta 13h-18h", AVG(ABS(t2mean2m_delta)) AS "AVG ABS t2mean2m_delta 13h-18h" FROM fact_prediction WHERE prediction_length >= 13 AND prediction_length <= 18 AND prediction_date >= 123 AND prediction_date <= 181;
SELECT COUNT(*), AVG(t2mean2m_delta) AS "AVG t2mean2m_delta 19h-24h", AVG(ABS(t2mean2m_delta)) AS "AVG ABS t2mean2m_delta 19h-24h" FROM fact_prediction WHERE prediction_length >= 19 AND prediction_length <= 24 AND prediction_date >= 123 AND prediction_date <= 181;
SELECT COUNT(*), AVG(t2mean2m_delta) AS "AVG t2mean2m_delta 25h-30h", AVG(ABS(t2mean2m_delta)) AS "AVG ABS t2mean2m_delta 25h-30h" FROM fact_prediction WHERE prediction_length >= 25 AND prediction_length <= 30 AND prediction_date >= 123 AND prediction_date <= 181;
SELECT COUNT(*), AVG(t2mean2m_delta) AS "AVG t2mean2m_delta 31h-36h", AVG(ABS(t2mean2m_delta)) AS "AVG ABS t2mean2m_delta 31h-36h" FROM fact_prediction WHERE prediction_length >= 31 AND prediction_length <= 36 AND prediction_date >= 123 AND prediction_date <= 181;
SELECT COUNT(*), AVG(t2mean2m_delta) AS "AVG t2mean2m_delta 37h-41h", AVG(ABS(t2mean2m_delta)) AS "AVG ABS t2mean2m_delta 37h-41h" FROM fact_prediction WHERE prediction_length >= 37 AND prediction_length <= 41 AND prediction_date >= 123 AND prediction_date <= 181;

SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta" FROM fact_prediction WHERE prediction_date >= 57 AND prediction_date <= 122;
SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta 4h-6h", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta 4h-6h" FROM fact_prediction WHERE prediction_length >= 4 AND prediction_length <= 6 AND prediction_date >= 123 AND prediction_date <= 181;
SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta 7h-12h", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta 7h-12h" FROM fact_prediction WHERE prediction_length >= 7 AND prediction_length <= 12 AND prediction_date >= 123 AND prediction_date <= 181;
SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta 13h-18h", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta 13h-18h" FROM fact_prediction WHERE prediction_length >= 13 AND prediction_length <= 18 AND prediction_date >= 123 AND prediction_date <= 181;
SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta 19h-24h", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta 19h-24h" FROM fact_prediction WHERE prediction_length >= 19 AND prediction_length <= 24 AND prediction_date >= 123 AND prediction_date <= 181;
SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta 25h-30h", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta 25h-30h" FROM fact_prediction WHERE prediction_length >= 25 AND prediction_length <= 30 AND prediction_date >= 123 AND prediction_date <= 181;
SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta 31h-36h", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta 31h-36h" FROM fact_prediction WHERE prediction_length >= 31 AND prediction_length <= 36 AND prediction_date >= 123 AND prediction_date <= 181;
SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta 37h-41h", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta 37h-41h" FROM fact_prediction WHERE prediction_length >= 37 AND prediction_length <= 41 AND prediction_date >= 123 AND prediction_date <= 181;

SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta" FROM fact_prediction;
SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta 4h-6h", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta 4h-6h" FROM fact_prediction WHERE prediction_length >= 4 AND prediction_length <= 6 AND prediction_date >= 123 AND prediction_date <= 181;
SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta 7h-12h", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta 7h-12h" FROM fact_prediction WHERE prediction_length >= 7 AND prediction_length <= 12 AND prediction_date >= 123 AND prediction_date <= 181;
SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta 13h-18h", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta 13h-18h" FROM fact_prediction WHERE prediction_length >= 13 AND prediction_length <= 18 AND prediction_date >= 123 AND prediction_date <= 181;
SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta 19h-24h", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta 19h-24h" FROM fact_prediction WHERE prediction_length >= 19 AND prediction_length <= 24 AND prediction_date >= 123 AND prediction_date <= 181;
SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta 25h-30h", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta 25h-30h" FROM fact_prediction WHERE prediction_length >= 25 AND prediction_length <= 30 AND prediction_date >= 123 AND prediction_date <= 181;
SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta 31h-36h", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta 31h-36h" FROM fact_prediction WHERE prediction_length >= 31 AND prediction_length <= 36 AND prediction_date >= 123 AND prediction_date <= 181;
SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta 37h-41h", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta 37h-41h" FROM fact_prediction WHERE prediction_length >= 37 AND prediction_length <= 41 AND prediction_date >= 123 AND prediction_date <= 181;
)
/* 2019-03-01 to 2019-04-01 */

SELECT COUNT(*), AVG(t2mean2m_delta) AS "AVG t2mean2m_delta", AVG(ABS(t2mean2m_delta)) AS "AVG ABS t2mean2m_delta" FROM fact_prediction WHERE prediction_date >= 182 AND prediction_date <= 213;
SELECT COUNT(*), AVG(t2mean2m_delta) AS "AVG t2mean2m_delta 4h-6h", AVG(ABS(t2mean2m_delta)) AS "AVG ABS t2mean2m_delta 4h-6h" FROM fact_prediction WHERE prediction_length >= 4 AND prediction_length <= 6 AND prediction_date >= 182 AND prediction_date <= 213;
SELECT COUNT(*), AVG(t2mean2m_delta) AS "AVG t2mean2m_delta 7h-12h", AVG(ABS(t2mean2m_delta)) AS "AVG ABS t2mean2m_delta 7h-12h" FROM fact_prediction WHERE prediction_length >= 7 AND prediction_length <= 12 AND prediction_date >= 182 AND prediction_date <= 213;
SELECT COUNT(*), AVG(t2mean2m_delta) AS "AVG t2mean2m_delta 13h-18h", AVG(ABS(t2mean2m_delta)) AS "AVG ABS t2mean2m_delta 13h-18h" FROM fact_prediction WHERE prediction_length >= 13 AND prediction_length <= 18 AND prediction_date >= 182 AND prediction_date <= 213;
SELECT COUNT(*), AVG(t2mean2m_delta) AS "AVG t2mean2m_delta 19h-24h", AVG(ABS(t2mean2m_delta)) AS "AVG ABS t2mean2m_delta 19h-24h" FROM fact_prediction WHERE prediction_length >= 19 AND prediction_length <= 24 AND prediction_date >= 182 AND prediction_date <= 213;
SELECT COUNT(*), AVG(t2mean2m_delta) AS "AVG t2mean2m_delta 25h-30h", AVG(ABS(t2mean2m_delta)) AS "AVG ABS t2mean2m_delta 25h-30h" FROM fact_prediction WHERE prediction_length >= 25 AND prediction_length <= 30 AND prediction_date >= 182 AND prediction_date <= 213;
SELECT COUNT(*), AVG(t2mean2m_delta) AS "AVG t2mean2m_delta 31h-36h", AVG(ABS(t2mean2m_delta)) AS "AVG ABS t2mean2m_delta 31h-36h" FROM fact_prediction WHERE prediction_length >= 31 AND prediction_length <= 36 AND prediction_date >= 182 AND prediction_date <= 213;
SELECT COUNT(*), AVG(t2mean2m_delta) AS "AVG t2mean2m_delta 37h-41h", AVG(ABS(t2mean2m_delta)) AS "AVG ABS t2mean2m_delta 37h-41h" FROM fact_prediction WHERE prediction_length >= 37 AND prediction_length <= 41 AND prediction_date >= 182 AND prediction_date <= 213;

SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta" FROM fact_prediction WHERE prediction_date >= 57 AND prediction_date <= 122;
SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta 4h-6h", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta 4h-6h" FROM fact_prediction WHERE prediction_length >= 4 AND prediction_length <= 6 AND prediction_date >= 182 AND prediction_date <= 213;
SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta 7h-12h", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta 7h-12h" FROM fact_prediction WHERE prediction_length >= 7 AND prediction_length <= 12 AND prediction_date >= 182 AND prediction_date <= 213;
SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta 13h-18h", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta 13h-18h" FROM fact_prediction WHERE prediction_length >= 13 AND prediction_length <= 18 AND prediction_date >= 182 AND prediction_date <= 213;
SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta 19h-24h", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta 19h-24h" FROM fact_prediction WHERE prediction_length >= 19 AND prediction_length <= 24 AND prediction_date >= 182 AND prediction_date <= 213;
SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta 25h-30h", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta 25h-30h" FROM fact_prediction WHERE prediction_length >= 25 AND prediction_length <= 30 AND prediction_date >= 182 AND prediction_date <= 213;
SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta 31h-36h", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta 31h-36h" FROM fact_prediction WHERE prediction_length >= 31 AND prediction_length <= 36 AND prediction_date >= 182 AND prediction_date <= 213;
SELECT COUNT(*), AVG(tmin2m_delta) AS "AVG tmin2m_delta 37h-41h", AVG(ABS(tmin2m_delta)) AS "AVG ABS tmin2m_delta 37h-41h" FROM fact_prediction WHERE prediction_length >= 37 AND prediction_length <= 41 AND prediction_date >= 182 AND prediction_date <= 213;

SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta" FROM fact_prediction;
SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta 4h-6h", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta 4h-6h" FROM fact_prediction WHERE prediction_length >= 4 AND prediction_length <= 6 AND prediction_date >= 182 AND prediction_date <= 213;
SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta 7h-12h", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta 7h-12h" FROM fact_prediction WHERE prediction_length >= 7 AND prediction_length <= 12 AND prediction_date >= 182 AND prediction_date <= 213;
SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta 13h-18h", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta 13h-18h" FROM fact_prediction WHERE prediction_length >= 13 AND prediction_length <= 18 AND prediction_date >= 182 AND prediction_date <= 213;
SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta 19h-24h", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta 19h-24h" FROM fact_prediction WHERE prediction_length >= 19 AND prediction_length <= 24 AND prediction_date >= 182 AND prediction_date <= 213;
SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta 25h-30h", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta 25h-30h" FROM fact_prediction WHERE prediction_length >= 25 AND prediction_length <= 30 AND prediction_date >= 182 AND prediction_date <= 213;
SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta 31h-36h", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta 31h-36h" FROM fact_prediction WHERE prediction_length >= 31 AND prediction_length <= 36 AND prediction_date >= 182 AND prediction_date <= 213;
SELECT COUNT(*), AVG(tmax2m_delta) AS "AVG tmax2m_delta 37h-41h", AVG(ABS(tmax2m_delta)) AS "AVG ABS tmax2m_delta 37h-41h" FROM fact_prediction WHERE prediction_length >= 37 AND prediction_length <= 41 AND prediction_date >= 182 AND prediction_date <= 213;
