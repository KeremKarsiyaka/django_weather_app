from django.shortcuts import render

def home(request):
	import json
	import requests

	api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=0EE1AB06-2844-40B1-A33D-34CF9EF61B02")
	
	try:
		api = json.loads(api_request.content)
	except Exception as e:
		api = "Error..."

	return render(request, 'home.html', {'api': api})


def about(request):
	return render(request, 'about.html', {})