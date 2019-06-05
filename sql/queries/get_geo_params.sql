/* Bolszewo - Cedry Małe */
SELECT min(x) AS "min x", max(x)  AS "max x", 
       min(y) AS "min y", max(y)  AS "max y" 
FROM dim_location 
WHERE langitude > 54.27248258415296 AND langitude < 54.61688338418353
    AND longitude > 18.17666407394085 AND longitude < 18.88028663455148;

/* 131, 149, 145, 153 /*

/* Lidzbark - Ostrów Mazowiecka */
SELECT min(x) AS "min x", max(x)  AS "max x", 
       min(y) AS "min y", max(y)  AS "max y" 
FROM dim_location 
WHERE langitude > 52.79559391678067 AND langitude < 53.26058428867436
    AND longitude > 19.823542973783265 AND longitude < 21.898069637271004;

/* 175, 228, 106, 117 /*

/* Katowice - Zakopane */
SELECT min(x) AS "min x", max(x)  AS "max x", 
       min(y) AS "min y", max(y)  AS "max y" 
FROM dim_location 
WHERE langitude > 49.291731446084945 AND langitude < 50.2515617199834
    AND longitude > 19.035009483944236 AND longitude < 19.985581547693716;

/* 154, 178, 13, 38 /*
