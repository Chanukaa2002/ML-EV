import numpy as np
import pandas as pd
import random
from datetime import datetime, timedelta
import os

# -----------------------------
# Helper function to create path
def mkpath(name):
    base_path = os.path.join(os.path.dirname(__file__), "..", "data")
    os.makedirs(base_path, exist_ok=True)
    return os.path.join(base_path, name)

# -----------------------------
# Sri Lanka cities and conditions
cities = ["Colombo", "Galle", "Kandy", "Matara", "Kurunegala", "Anuradhapura", "Trincomalee", "Jaffna", "Batticaloa", "Ratnapura"]
road_types = ["city","highway","rural","coastal"]
weathers = ["sunny","cloudy","light_rain","heavy_rain","monsoon"]
time_of_day_buckets = ["morning","afternoon","evening","night"]

# Vehicle models
vehicle_models = [
    {"make":"Nissan", "model":"Leaf", "eff_kwh_per_km":0.16, "weight_kg":1500},
    {"make":"MG", "model":"ZS EV", "eff_kwh_per_km":0.18, "weight_kg":1650},
    {"make":"BYD", "model":"Atto 3", "eff_kwh_per_km":0.17, "weight_kg":1700},
    {"make":"Tesla", "model":"Model 3", "eff_kwh_per_km":0.15, "weight_kg":1620},
]

# Charging stations
charging_stations = []
station_types = ["AC_7kW","AC_22kW","DC_50kW","DC_120kW"]
for i, city in enumerate(cities, start=1):
    for j in range(3):
        charging_stations.append({
            "station_id": f"CS_{i:02d}_{j+1}",
            "name": f"ChargePoint {city} #{j+1}",
            "city": city,
            "charger_type": random.choice(station_types),
            "num_ports": random.choice([1,2,3]),
            "avg_wait_min": random.randint(0,30),
            "operational": random.choices([True, False], weights=[0.95,0.05])[0]
        })
charging_stations_df = pd.DataFrame(charging_stations)

# -----------------------------
# Helper for origin-destination sampling
def sample_od():
    o = random.choice(cities)
    d = random.choice([c for c in cities if c != o])
    idx_o = cities.index(o)
    idx_d = cities.index(d)
    base = abs(idx_o - idx_d) * 40 + 20
    distance = max(5, int(np.random.normal(base, base * 0.25)))
    elev_gain = int(abs(idx_o - idx_d) * random.uniform(10,50) + (50 if ("Kandy" in (o,d) or "Ratnapura" in (o,d)) else 0))
    return o, d, distance, elev_gain

# -----------------------------
N_TRIPS = 10000  # number of synthetic trips

# 1) Driving Style Dataset
driving_rows = []
for tid in range(N_TRIPS):
    trip_id = f"TR{tid+1:06d}"
    driver_id = f"DRV{random.randint(1,400):04d}"
    vehicle = random.choice(vehicle_models)
    origin, dest, distance_km, elev_gain_m = sample_od()
    trip_duration_min = max(3, int(distance_km / max(10, np.random.normal(45,10)) * 60))
    avg_speed = round(distance_km / (trip_duration_min/60.0) + np.random.normal(0,3), 2)
    max_speed = round(avg_speed + abs(np.random.normal(10,7)), 2)
    style_latent = random.choices(["eco","normal","aggressive"], weights=[0.25,0.6,0.15])[0]
    if style_latent == "eco":
        accel_mean = round(np.random.normal(0.45, 0.15),3)
        accel_std = round(abs(np.random.normal(0.25,0.1)),3)
        braking_intensity = round(abs(np.random.normal(0.25,0.15)),3)
    elif style_latent == "normal":
        accel_mean = round(np.random.normal(0.9, 0.3),3)
        accel_std = round(abs(np.random.normal(0.6,0.25)),3)
        braking_intensity = round(abs(np.random.normal(0.45,0.25)),3)
    else:
        accel_mean = round(np.random.normal(1.8, 0.5),3)
        accel_std = round(abs(np.random.normal(1.2,0.4)),3)
        braking_intensity = round(abs(np.random.normal(1.1,0.4)),3)
    road_type = random.choice(road_types)
    weather = random.choices(weathers, weights=[0.35,0.25,0.15,0.15,0.10])[0]
    time_of_day = random.choice(time_of_day_buckets)
    # label based on simple heuristic
    if accel_mean < 0.6 and accel_std < 0.5 and braking_intensity < 0.4:
        style_label = "Eco"
    elif accel_mean > 1.4 or accel_std > 1.0 or braking_intensity > 0.9:
        style_label = "Aggressive"
    else:
        style_label = "Normal"
    driving_rows.append({
        "trip_id": trip_id, "driver_id": driver_id, "vehicle_make": vehicle["make"], "vehicle_model": vehicle["model"],
        "origin": origin, "destination": dest, "distance_km": distance_km, "elevation_gain_m": elev_gain_m,
        "trip_date": (datetime.now() - timedelta(days=random.randint(0,365))).strftime("%Y-%m-%d %H:%M:%S"),
        "avg_speed": max(0.0, round(avg_speed,2)), "max_speed": max(0.0, round(max_speed,2)),
        "acceleration_mean": max(0.0, accel_mean), "acceleration_std": accel_std, "braking_intensity": braking_intensity,
        "trip_duration_min": trip_duration_min, "road_type": road_type, "weather": weather,
        "time_of_day": time_of_day, "driving_style": style_label
    })
driving_df = pd.DataFrame(driving_rows)
driving_df.to_csv(mkpath("driving_style_dataset_srilanka.csv"), index=False)

# 2) Energy Consumption Dataset
energy_rows = []
for _, row in driving_df.iterrows():
    vehicle = next(v for v in vehicle_models if v["model"] == row["vehicle_model"])
    base_eff = vehicle["eff_kwh_per_km"]
    style_mult = {"Eco":0.9, "Normal":1.0, "Aggressive":1.3}[row["driving_style"]]
    traffic_mult = {"city":1.05, "highway":0.95, "rural":1.0, "coastal":1.02}[row["road_type"]]
    weather_mult = {"sunny":1.0, "cloudy":1.01, "light_rain":1.03, "heavy_rain":1.08, "monsoon":1.12}[row["weather"]]
    elev_factor = 1 + (row["elevation_gain_m"] / (row["distance_km"]*100+1))*0.6
    noise = np.random.normal(0,0.02)
    energy_kwh = row["distance_km"] * base_eff * style_mult * traffic_mult * weather_mult * elev_factor * (1+noise)
    battery_capacity = random.choice([40,50,60,75])
    battery_start_pct = round(random.uniform(40,100),2)
    battery_start_kwh = battery_capacity * battery_start_pct / 100
    battery_end_kwh = max(0, battery_start_kwh - energy_kwh)
    battery_end_pct = round(battery_end_kwh / battery_capacity * 100,2)
    energy_rows.append({
        "trip_id": row["trip_id"], "vehicle_model": row["vehicle_model"], "distance_km": row["distance_km"],
        "driving_style": row["driving_style"], "road_type": row["road_type"], "weather": row["weather"],
        "elevation_gain_m": row["elevation_gain_m"], "avg_speed": row["avg_speed"],
        "energy_consumed_kWh": round(max(0.01, energy_kwh),3),
        "battery_capacity_kWh": battery_capacity, "battery_start_%": battery_start_pct, "battery_end_%": battery_end_pct
    })
energy_df = pd.DataFrame(energy_rows)
energy_df.to_csv(mkpath("energy_consumption_dataset_srilanka.csv"), index=False)

# 3) Battery Range Dataset
range_rows = []
for _, e in energy_df.iterrows():
    vehicle = next(v for v in vehicle_models if v["model"]==e["vehicle_model"])
    style_eff_mult = {"Eco":0.95,"Normal":1.0,"Aggressive":1.2}[e["driving_style"]]
    eff = vehicle["eff_kwh_per_km"]*style_eff_mult
    start_kwh = e["battery_capacity_kWh"]*e["battery_start_%"]/100
    max_possible_km = round(start_kwh / eff,2)
    predicted_remaining_km = max(0, round((start_kwh - e["energy_consumed_kWh"]) / eff,2))
    range_rows.append({
        "trip_id": e["trip_id"], "vehicle_model": e["vehicle_model"], "battery_capacity_kWh": e["battery_capacity_kWh"],
        "battery_start_%": e["battery_start_%"], "battery_start_kWh": round(start_kwh,3),
        "eff_kWh_per_km": round(eff,4), "max_possible_km": max_possible_km, "predicted_remaining_km": predicted_remaining_km
    })
range_df = pd.DataFrame(range_rows)
range_df.to_csv(mkpath("battery_range_dataset_srilanka.csv"), index=False)

# 4) Charging Station Recommender Dataset
charge_rows = []
for _, row in driving_df.iterrows():
    origin, dest = row["origin"], row["destination"]
    candidates = [s for s in charging_stations if s["city"] in {origin,dest}]
    if len(candidates)<3:
        intermediate = random.choice([c for c in cities if c not in {origin,dest}])
        candidates += [s for s in charging_stations if s["city"]==intermediate]
    sample_cands = random.sample(candidates, min(3,len(candidates)))
    best_score = 1e9
    best_station = None
    for s in sample_cands:
        base = 5 if s["city"] in {origin,dest} else random.randint(10,60)
        power_factor = 0.8 if "DC" in s["charger_type"] else 1.0
        avail = 1 if s["operational"] else 0.01
        score = base*power_factor/(avail+0.001) + s["avg_wait_min"]*0.1
        if score<best_score:
            best_score = score
            best_station = s
        charge_rows.append({
            "trip_id": row["trip_id"], "station_id": s["station_id"], "station_name": s["name"], "station_city": s["city"],
            "charger_type": s["charger_type"], "num_ports": s["num_ports"], "avg_wait_min": s["avg_wait_min"],
            "operational": s["operational"], "distance_from_route_km": base, "is_recommended": int(s["station_id"]==best_station["station_id"])
        })
charge_df = pd.DataFrame(charge_rows)
charge_df.to_csv(mkpath("charging_recommender_dataset_srilanka.csv"), index=False)

# 5) Optimal Route Dataset
route_rows = []
for tid in range(1000):
    origin = random.choice(cities)
    dest = random.choice([c for c in cities if c!=origin])
    base_distance = random.randint(20,120)
    routes = []
    for r in ["A","B","C"]:
        route_distance = max(5,int(base_distance*random.uniform(0.85,1.25)))
        avg_speed = max(20,int(np.random.normal(50,12)))
        traffic_level = random.choice(["low","medium","high"])
        time_min = int(route_distance/max(10,avg_speed)*60*(1 + (0.2 if traffic_level=="high" else 0.05 if traffic_level=="medium" else 0)))
        veh = random.choice(vehicle_models)
        style = random.choices(["Eco","Normal","Aggressive"], weights=[0.25,0.6,0.15])[0]
        weather = random.choice(weathers)
        style_mult = {"Eco":0.9,"Normal":1.0,"Aggressive":1.3}[style]
        weather_mult = {"sunny":1.0,"cloudy":1.01,"light_rain":1.03,"heavy_rain":1.08,"monsoon":1.12}[weather]
        energy_est = route_distance*veh["eff_kwh_per_km"]*style_mult*weather_mult
        routes.append({
            "route_label": r, "route_distance_km": route_distance, "avg_speed_kmh": avg_speed,
            "traffic_level": traffic_level, "estimated_time_min": time_min,
            "estimated_energy_kWh": round(energy_est,3), "driving_style": style,
            "vehicle_model": veh["model"], "weather": weather
        })
    best = min(routes, key=lambda x: 0.7*x["estimated_energy_kWh"] + 0.3*(x["estimated_time_min"]/60.0))
    for r in routes:
        route_rows.append({
            "origin": origin, "destination": dest, "route_id": f"{origin}_{dest}_{r['route_label']}",
            **r, "is_optimal": int(r["route_label"]==best["route_label"])
        })
route_df = pd.DataFrame(route_rows)
route_df.to_csv(mkpath("optimal_route_dataset_srilanka.csv"), index=False)

# Charging stations master CSV
charging_stations_df.to_csv(mkpath("charging_stations_master_srilanka.csv"), index=False)

print("Datasets generated in ./datasets folder!")
