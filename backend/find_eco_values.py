from controllers.driving_script_controller import predict_driving_style_controller

# Test progressively more eco-friendly values
test_cases = [
    ("Ultra Eco", {
        'distance_km': 50,
        'elevation_gain_m': 50,
        'avg_speed': 40,
        'max_speed': 50,
        'acceleration_mean': 0.5,
        'acceleration_std': 0.15,
        'braking_intensity': 0.5,
        'trip_duration_min': 75,
        'vehicle_make': 'MG',
        'vehicle_model': 'ZS EV',
        'road_type': 'highway',
        'weather': 'sunny',
        'time_of_day': 'morning'
    }),
    ("Moderate Eco", {
        'distance_km': 50,
        'elevation_gain_m': 100,
        'avg_speed': 45,
        'max_speed': 55,
        'acceleration_mean': 0.8,
        'acceleration_std': 0.24,
        'braking_intensity': 0.8,
        'trip_duration_min': 67,
        'vehicle_make': 'MG',
        'vehicle_model': 'ZS EV',
        'road_type': 'city',
        'weather': 'clear',
        'time_of_day': 'morning'
    }),
]

for name, data in test_cases:
    result = predict_driving_style_controller(data)
    print(f"{name}: {result['predicted_driving_style']} ({result.get('confidence_score', 0):.2%})")
