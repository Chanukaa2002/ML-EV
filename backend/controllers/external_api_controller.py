import os
import json
import urllib.parse
import urllib.request
from typing import Any, Dict, Optional


class WeatherAPIError(Exception):
	pass


def _build_openweather_url(lat: float, lon: float, api_key: str, units: str = "metric") -> str:
	base = "https://api.openweathermap.org/data/2.5/weather"
	params = {
		"lat": f"{lat:.6f}",
		"lon": f"{lon:.6f}",
		"appid": api_key,
		"units": units,
	}
	return f"{base}?{urllib.parse.urlencode(params)}"

def get_weather_controller(lat: float, lon: float, units: str = "metric") -> Dict[str, Any]:

	api_key = "1eda4b17d9557443f2f7c025bf0d502e"
	if not api_key:
		raise WeatherAPIError("Missing OPENWEATHER_API_KEY environment variable")

	url = _build_openweather_url(lat, lon, api_key, units)

	try:
		with urllib.request.urlopen(url, timeout=10) as resp:
			if resp.status != 200:
				raise WeatherAPIError(f"OpenWeather request failed with status {resp.status}")
			payload = json.loads(resp.read().decode("utf-8"))
	except Exception as e:
		raise WeatherAPIError(str(e))

	# Extract a concise, stable subset of fields
	main = payload.get("main", {})
	wind = payload.get("wind", {})
	weather_list = payload.get("weather", []) or [{}]
	sys = payload.get("sys", {})

	curated: Dict[str, Any] = {
		"coords": {"lat": lat, "lon": lon},
		"location": {
			"city": payload.get("name"),
			"country": sys.get("country"),
		},
		"weather": {
			"temp": main.get("temp"),
			"feels_like": main.get("feels_like"),
			"humidity": main.get("humidity"),
			"pressure": main.get("pressure"),
			"wind_speed": wind.get("speed"),
			"wind_deg": wind.get("deg"),
			"condition": weather_list[0].get("main"),
			"description": weather_list[0].get("description"),
			"icon": weather_list[0].get("icon"),
		},
		"timestamp": payload.get("dt"),
		"units": units,
		"source": "openweathermap",
	}

	return curated
