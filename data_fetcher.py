import requests

def fetch_data(animal_name):

  """ Loads animal data from the API """
  API_KEY = "tEPzQEsWwciI03HXq7n+IA==RR4fNvH4lVhGTxGa"
  url = "https://api.api-ninjas.com/v1/animals"
  params = {"name": animal_name}

  response = requests.get(url, params=params, headers={"X-Api-Key": API_KEY})

  if response.status_code == 200:
      return response.json()  # gibt ein Array von Tieren zurück
  else:
      print("Fehler beim Abrufen der API:", response.status_code)
      return []