CREATE TABLE "fact_prediction" (
  "id" SERIAL PRIMARY KEY,
  "type" int,
  "prediction_date" int,
  "prediction_time" int,
  "prediction_length" int,
  "prediction_timestamp" timestamp with time zone,
  "prediction_type" varchar(50),
  "location" int,
  "actual_diff" int,
  "acm_convective_percip_predicted" NUMERIC,
  "acm_convective_percip_actual" NUMERIC,
  "acm_convective_percip_delta" NUMERIC,
  "acm_convective_percip_local_max_predicted" NUMERIC DEFAULT 0.0,
  "acm_convective_percip_local_max_actual" NUMERIC DEFAULT 0.0,
  "acm_convective_percip_local_max_delta" NUMERIC,
  "acm_convective_percip_local_min_predicted" NUMERIC DEFAULT 0.0,
  "acm_convective_percip_local_min_actual" NUMERIC DEFAULT 0.0,
  "acm_convective_percip_local_min_delta" NUMERIC,
  "acm_total_percip_local_max_actual" NUMERIC,
  "acm_total_percip_local_max_predicted" NUMERIC,
  "acm_total_percip_local_max_delta" NUMERIC,
  "acm_total_percip_local_min_actual" NUMERIC,
  "acm_total_percip_local_min_predicted" NUMERIC,
  "acm_total_percip_local_min_delta" NUMERIC,
  "acm_total_percip_predicted" NUMERIC,
  "acm_total_percip_actual" NUMERIC,
  "acm_total_percip_delta" NUMERIC,
  "avg_total_cld_frac_predicted" NUMERIC,
  "avg_total_cld_frac_actual" NUMERIC,
  "avg_total_cld_frac_delta" NUMERIC,
  "domain_percip_type_fr_predicted" NUMERIC,
  "domain_percip_type_fr_actual" NUMERIC,
  "domain_percip_type_fr_delta" NUMERIC,
  "domain_percip_type_r_predicted" NUMERIC,
  "domain_percip_type_r_actual" NUMERIC,
  "domain_percip_type_r_delta" NUMERIC,
  "domain_percip_type_ip_predicted" NUMERIC,
  "domain_percip_type_ip_actual" NUMERIC,
  "domain_percip_type_ip_delta" NUMERIC,
  "domain_percip_type_s_predicted" NUMERIC,
  "domain_percip_type_s_actual" NUMERIC,
  "domain_percip_type_s_delta" NUMERIC,
  "fsi_predicted" NUMERIC,
  "fsi_actual" NUMERIC,
  "fsi_delta" NUMERIC,
  "lifted_index_predicted" NUMERIC,
  "lifted_index_actual" NUMERIC,
  "lifted_index_delta" NUMERIC,
  "low_cloud_fraction_predicted" NUMERIC,
  "low_cloud_fraction_actual" NUMERIC,
  "low_cloud_fraction_delta" NUMERIC,
  "mid_cloud_fraction_predicted" NUMERIC,
  "mid_cloud_fraction_actual" NUMERIC,
  "mid_cloud_fraction_delta" NUMERIC,
  "high_cloud_fraction_predicted" NUMERIC,
  "high_cloud_fraction_actual" NUMERIC,
  "high_cloud_fraction_delta" NUMERIC,
  "shelter_dewpoint_predicted" NUMERIC,
  "shelter_dewpoint_actual" NUMERIC,
  "shelter_dewpoint_delta" NUMERIC,
  "shelter_rel_humid_predicted" NUMERIC,
  "shelter_rel_humid_actual" NUMERIC,
  "shelter_rel_humid_delta" NUMERIC,
  "shelter_temperature_predicted" NUMERIC,
  "shelter_temperature_actual" NUMERIC,
  "shelter_temperature_delta" NUMERIC,
  "skin_temperature_predicted" NUMERIC,
  "skin_temperature_actual" NUMERIC,
  "skin_temperature_delta" NUMERIC,
  "soil_temperature_predicted" NUMERIC,
  "soil_temperature_actual" NUMERIC,
  "soil_temperature_delta" NUMERIC,
  "surface_pressure_predicted" NUMERIC,
  "surface_pressure_actual" NUMERIC,
  "surface_pressure_delta" NUMERIC,
  "surface_rel_humid_predicted" NUMERIC,
  "surface_rel_humid_actual" NUMERIC,
  "surface_rel_humid_delta" NUMERIC,
  "t2mean2m_predicted" NUMERIC,
  "t2mean2m_actual" NUMERIC,
  "t2mean2m_delta" NUMERIC,
  "tmax2m_predicted" NUMERIC,
  "tmax2m_actual" NUMERIC,
  "tmax2m_delta" NUMERIC,
  "tmin2m_predicted" NUMERIC,
  "tmin2m_actual" NUMERIC,
  "tmin2m_delta" NUMERIC,
  "u_storm_motion_6km_predicted" NUMERIC,
  "u_storm_motion_6km_actual" NUMERIC,
  "u_storm_motion_6km_delta" NUMERIC,
  "u_wind_on_10m_predicted" NUMERIC,
  "u_wind_on_10m_actual" NUMERIC,
  "u_wind_on_10m_delta" NUMERIC,
  "visibility_predicted" NUMERIC,
  "visibility_actual" NUMERIC,
  "visibility_delta" NUMERIC,
  "v_storm_motion_6km_predicted" NUMERIC,
  "v_storm_motion_6km_actual" NUMERIC,
  "v_storm_motion_6km_delta" NUMERIC,
  "v_wind_on_10m_predicted" NUMERIC,
  "v_wind_on_10m_actual" NUMERIC,
  "v_wind_on_10m_delta" NUMERIC,
  "wind_gust_predicted" NUMERIC,
  "wind_gust_actual" NUMERIC,
  "wind_gust_delta" NUMERIC,
  "wvc_predicted" NUMERIC,
  "wvc_actual" NUMERIC,
  "wvc_delta" NUMERIC,
  "x" int,
  "y" int
);

CREATE TABLE "dim_prediction_type" (
  "id" int PRIMARY KEY,
  "is_long" boolean NOT NULL,
  "hours_ahead" integer NOT NULL
);

CREATE TABLE "dim_date" (
  "id" int PRIMARY KEY,
  "date" date NOT NULL UNIQUE,
  "year" int NOT NULL,
  "month" int NOT NULL,
  "day" int NOT NULL,
  UNIQUE("day", "month", "year")
);

CREATE TABLE "dim_time" (
  "id" int PRIMARY KEY,
  "hour" int NOT NULL,
  "minute" int NOT NULL,
  UNIQUE("hour", "minute")
);

CREATE TABLE "dim_location" (
  "id" int PRIMARY KEY,
  "x" int NOT NULL,
  "y" int NOT NULL,
  "europe" boolean NOT NULL,
  "langitude" NUMERIC,
  "longitude" NUMERIC,
  UNIQUE("x", "y", "europe")
);

ALTER TABLE "fact_prediction" ADD FOREIGN KEY ("type") REFERENCES "dim_prediction_type" ("id");

ALTER TABLE "fact_prediction" ADD FOREIGN KEY ("prediction_date") REFERENCES "dim_date" ("id");

ALTER TABLE "fact_prediction" ADD FOREIGN KEY ("prediction_time") REFERENCES "dim_time" ("id");

ALTER TABLE "fact_prediction" ADD FOREIGN KEY ("location") REFERENCES "dim_location" ("id");

CREATE INDEX pred_length_index ON fact_prediction (prediction_length);
CREATE INDEX pred_date_index ON fact_prediction (prediction_date);
CREATE INDEX pred_coordinates ON fact_prediction (x, y);
