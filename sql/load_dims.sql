COPY dim_date (id, date, year, month, day)
FROM '<path>/date.csv' DELIMITER ',' CSV HEADER;

COPY dim_location (id, x, y, europe)
FROM '<path>/location.csv' DELIMITER ',' CSV HEADER;

COPY dim_time (id, hour, minute)
FROM '<path>/time.csv' DELIMITER ',' CSV HEADER;

COPY dim_prediction_type (id, is_long, hours_ahead)
FROM '<path>/type.csv' DELIMITER ',' CSV HEADER;
