import requests
base_url="https://pokeapi.co/api/v2/"

def get_pokemon_name(name):
    url=f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code==200:
        pokemon_data=response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

pokemon_name = 'giratina'
pokemon_info=get_pokemon_name(pokemon_name)
if pokemon_info:
    print(f"Name: {pokemon_info['name']}")
    print(f"Id: {pokemon_info['id']}")
    # print(f"Abilities: {pokemon_info['abilities']}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")