CREATE TABLE "fact_prediction" (
  "id" int PRIMARY KEY,
  "type" int,
  "prediction_date" int,
  "prediction_time" int,
  "made_on_date" int,
  "made_on_time" int,
  "location" int,
  "acm_convective_percip_predicted" double,
  "acm_convective_percip_actual" double,
  "acm_convective_percip_delta" double,
  "acm_total_percip_predicted" double,
  "acm_total_percip_actual" double,
  "acm_total_percip_delta" double,
  "domain_percip_type_fr_predicted" double,
  "domain_percip_type_fr_actual" double,
  "domain_percip_type_fr_delta" double,
  "domain_percip_type_r_predicted" double,
  "domain_percip_type_r_actual" double,
  "domain_percip_type_r_delta" double,
  "domain_percip_type_ip_predicted" double,
  "domain_percip_type_ip_actual" double,
  "domain_percip_type_ip_delta" double,
  "domain_percip_type_s_predicted" double,
  "domain_percip_type_s_actual" double,
  "domain_percip_type_s_delta" double,
  "fsi_predicted" double,
  "fsi_actual" double,
  "fsi_delta" double,
  "lifted_index_predicted" double,
  "lifted_index_actual" double,
  "lifted_index_delta" double,
  "low_cloud_fraction_predicted" double,
  "low_cloud_fraction_actual" double,
  "low_cloud_fraction_delta" double,
  "mid_cloud_fraction_predicted" double,
  "mid_cloud_fraction_actual" double,
  "mid_cloud_fraction_delta" double,
  "high_cloud_fraction_predicted" double,
  "high_cloud_fraction_actual" double,
  "high_cloud_fraction_delta" double,
  "shelter_dewpoint_predicted" double,
  "shelter_dewpoint_actual" double,
  "shelter_dewpoint_delta" double,
  "shelter_rel_humid_predicted" double,
  "shelter_rel_humid_actual" double,
  "shelter_rel_humid_delta" double,
  "shelter_temperature_predicted" double,
  "shelter_temperature_actual" double,
  "shelter_temperature_delta" double,
  "skin_temperature_predicted" double,
  "skin_temperature_actual" double,
  "skin_temperature_delta" double,
  "soil_temperature_predicted" double,
  "soil_temperature_actual" double,
  "soil_temperature_delta" double,
  "surface_pressure_predicted" double,
  "surface_pressure_actual" double,
  "surface_pressure_delta" double,
  "surface_rel_humid_predicted" double,
  "surface_rel_humid_actual" double,
  "surface_rel_humid_delta" double,
  "t2mean2m_predicted" double,
  "t2mean2m_actual" double,
  "t2mean2m_delta" double,
  "tmax2m_predicted" double,
  "tmax2m_actual" double,
  "tmax2m_delta" double,
  "tmin2m_predicted" double,
  "tmin2m_actual" double,
  "tmin2m_delta" double,
  "u_storm_motion_6km_predicted" double,
  "u_storm_motion_6km_actual" double,
  "u_storm_motion_6km_delta" double,
  "u_wind_on_10m_predicted" double,
  "u_wind_on_10m_actual" double,
  "u_wind_on_10m_delta" double,
  "visibility_predicted" double,
  "visibility_actual" double,
  "visibility_delta" double,
  "v_storm_motion_6km_predicted" double,
  "v_storm_motion_6km_actual" double,
  "v_storm_motion_6km_delta" double,
  "v_wind_on_10m_predicted" double,
  "v_wind_on_10m_actual" double,
  "v_wind_on_10m_delta" double,
  "wind_gust_predicted" double,
  "wind_gust_actual" double,
  "wind_gust_delta" double,
  "wvc_predicted" double,
  "wvc_actual" double,
  "wvc_delta" double
);

CREATE TABLE "dim_prediction_type" (
  "id" int PRIMARY KEY,
  "isLong" boolean
);

CREATE TABLE "dim_date" (
  "id" int PRIMARY KEY,
  "date" date NOT NULL UNIQUE,
  "year" int NOT NULL,
  "month" int NOT NULL,
  "day" NOT NULL,
  UNIQUE("day", "month", "year")
);

CREATE TABLE "dim_time" (
  "id" int PRIMARY KEY,
  "hour" int NOT NULL
  "minute" NOT NULL,
  UNIQUE("hour", "minute")
);

CREATE TABLE "dim_location" (
  "id" int,
  "x" int,
  "y" int,
  "langitude" double,
  "longitude" double,
  UNIQUE("x", "y"),
  UNIQUE("langitude", "longitude")
);

ALTER TABLE "fact_prediction" ADD FOREIGN KEY ("type") REFERENCES "dim_prediction_type" ("id");

ALTER TABLE "fact_prediction" ADD FOREIGN KEY ("prediction_date") REFERENCES "dim_date" ("id");

ALTER TABLE "fact_prediction" ADD FOREIGN KEY ("prediction_time") REFERENCES "dim_time" ("id");

ALTER TABLE "fact_prediction" ADD FOREIGN KEY ("made_on_date") REFERENCES "dim_date" ("id");

ALTER TABLE "fact_prediction" ADD FOREIGN KEY ("made_on_time") REFERENCES "dim_time" ("id");

ALTER TABLE "fact_prediction" ADD FOREIGN KEY ("location") REFERENCES "dim_location" ("id");