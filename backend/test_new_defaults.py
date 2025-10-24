from controllers.driving_script_controller import predict_driving_style_controller

# Test with new default values
result = predict_driving_style_controller({
    'distance_km': 50,
    'elevation_gain_m': 100,
    'avg_speed': 50,
    'max_speed': 65,
    'acceleration_mean': 1.0,
    'acceleration_std': 0.3,
    'braking_intensity': 1.0,
    'trip_duration_min': 60,
    'vehicle_make': 'MG',
    'vehicle_model': 'ZS EV',
    'road_type': 'city',
    'weather': 'clear',
    'time_of_day': 'morning'
})

print('Predicted Style:', result['predicted_driving_style'])
print('Confidence:', f"{result.get('confidence_score', 0):.2%}")
