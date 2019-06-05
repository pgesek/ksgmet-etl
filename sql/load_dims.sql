COPY dim_date (id, date, year, month, day)
FROM '<path>/date.csv' DELIMITER ',' CSV HEADER;

COPY dim_location (id, x, y, europe)
FROM '<path>/location.csv' DELIMITER ',' CSV HEADER;

COPY dim_time (id, hour, minute)
FROM '<path>/time.csv' DELIMITER ',' CSV HEADER;

COPY dim_prediction_type (id, is_long, hours_ahead)
FROM '<path>/type.csv' DELIMITER ',' CSV HEADER;

UPDATE dim_location SET longitude = 13.236774 + y * 0.0378444945891919 WHERE europe = false;
UPDATE dim_location SET langitude = 48.802824 + y * 0.0378444945891919 WHERE europe = false;
