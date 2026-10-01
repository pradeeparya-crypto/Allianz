import requests

def list_pokemon(limit=100):
	response = requests.get(f"https://pokeapi.co/api/v2/pokemon?limit={limit}")
	response.raise_for_status()
	return response.json()["results"]
#print(list_pokemon())

def get_pokemon_details(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
#print(get_pokemon_details("https://pokeapi.co/api/v2/pokemon/1/"))

def get_pokemon_abilities():
      pokemons = list_pokemon(10)
      result = []
      for pokeomon in pokemons:
            data = get_pokemon_details(pokeomon["url"])
            print(data)