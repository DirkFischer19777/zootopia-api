import requests
import os
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv('API_KEY')



URL = "https://api.api-ninjas.com/v1/animals"
def fetch_data(animal_name):

  """ Loads animal data from the API """


  params = {"name": animal_name}

  response = requests.get(URL, params=params, headers={"X-Api-Key": API_KEY})

  if response.status_code == 200:
      return response.json()  # gibt ein Array von Tieren zurück
  else:
      print("Fehler beim Abrufen der API:", response.status_code)
      return []