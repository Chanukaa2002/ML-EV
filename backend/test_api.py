"""Test the new API endpoints"""
import urllib.request
import json
import time

def test_endpoint(url, data, endpoint_name):
    """Test a POST endpoint"""
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    
    try:
        start_time = time.time()
        with urllib.request.urlopen(req, timeout=10) as response:
            result = json.loads(response.read().decode('utf-8'))
            elapsed = time.time() - start_time
            print(f"\n✅ SUCCESS - {endpoint_name} ({elapsed:.2f}s)")
            print(json.dumps(result, indent=2))
            return result
    except urllib.error.URLError as e:
        print(f"\n❌ CONNECTION ERROR - {endpoint_name}")
        print(f"Error: {e}")
        print("Make sure Flask backend is running on http://localhost:5000")
        return None
    except Exception as e:
        print(f"\n❌ ERROR - {endpoint_name}")
        print(f"Error: {str(e)}")
        return None

print("="*70)
print("  EV ROUTE OPTIMIZER - BACKEND API TESTING")
print("="*70)
print("\nMake sure Flask backend is running on http://localhost:5000")
print("="*70)

# Test 1: Driving Style Prediction
print("\n\n📊 TEST 1: Driving Style Prediction")
print("-" * 70)
driving_result = test_endpoint(
    'http://localhost:5000/api/driving/predict',
    {
        'distance_km': 50,
        'elevation_gain_m': 0,
        'avg_speed': 60,
        'max_speed': 80,
        'acceleration_mean': 1.2,
        'acceleration_std': 0.36,
        'braking_intensity': 1.5,
        'trip_duration_min': 50,
        'vehicle_make': 'MG',
        'vehicle_model': 'ZS EV',
        'road_type': 'city',
        'weather': 'sunny',
        'time_of_day': 'evening'
    },
    'Driving Style API'
)

# Test 2: Energy Prediction
print("\n\n⚡ TEST 2: Energy Consumption Prediction")
print("-" * 70)
energy_result = test_endpoint(
    'http://localhost:5000/api/energy/predict',
    {
        'distance_km': 50,
        'driving_style': 'Normal',
        'road_type': 'city',
        'weather': 'sunny',
        'elevation_gain_m': 0,
        'avg_speed': 60
    },
    'Energy Prediction API'
)

# Test 3: Battery Range Prediction
print("\n\n🔋 TEST 3: Battery Range Prediction")
print("-" * 70)
if energy_result and energy_result.get('success'):
    battery_result = test_endpoint(
        'http://localhost:5000/api/battery/predict',
        {
            'battery_capacity_kWh': 50.3,
            'battery_percent': 80,
            'efficiency_kWh_per_km': energy_result.get('efficiency_kWh_per_km', 0.171)
        },
        'Battery Range API'
    )
else:
    print("⏭️  Skipped (Energy test failed)")
    battery_result = None

# Test 4: Optimal Path
print("\n\n🗺️  TEST 4: Optimal Path Prediction")
print("-" * 70)
if energy_result and energy_result.get('success') and driving_result and driving_result.get('success'):
    path_result = test_endpoint(
        'http://localhost:5000/api/optimal-path/predict',
        {
            'distance_km': 50,
            'road_type': 'city',
            'traffic_level': 'medium',
            'weather': 'sunny',
            'driving_style': driving_result.get('predicted_driving_style', 'Normal'),
            'predicted_energy_kWh': energy_result.get('predicted_energy_kWh', 8.5),
            'predicted_range_km': 200,
            'battery_remaining_percent': 80
        },
        'Optimal Path API'
    )
else:
    print("⏭️  Skipped (Previous tests failed)")
    path_result = None

# Summary
print("\n\n" + "="*70)
print("  TEST SUMMARY")
print("="*70)
tests_passed = sum([
    1 if driving_result and driving_result.get('success') else 0,
    1 if energy_result and energy_result.get('success') else 0,
    1 if battery_result and battery_result.get('success') else 0,
    1 if path_result and path_result.get('success') else 0
])
print(f"\n✅ Tests Passed: {tests_passed}/4")
print(f"{'❌' if tests_passed < 4 else '✅'} Tests Failed: {4 - tests_passed}/4")

if tests_passed == 4:
    print("\n🎉 ALL TESTS PASSED! Backend APIs are working correctly.")
    print("\nNext Steps:")
    print("1. Open UI/pages/route-optimizer.html in a browser")
    print("2. Test the complete route optimization flow")
    print("3. Check browser console for any errors")
    print("4. Verify all predictions are from backend (check Network tab)")
else:
    print("\n⚠️  SOME TESTS FAILED!")
    print("Please check:")
    print("1. Flask backend is running")
    print("2. All required packages are installed")
    print("3. CSV dataset files exist in backend/data/")
    print("4. No errors in Flask console")

print("\n" + "="*70)

