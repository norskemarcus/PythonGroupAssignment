import requests

def fetch_pokemon_data(pokemon_name):
    # Define the base URL of the PokeAPI
    base_url = "https://pokeapi.co/api/v2/pokemon/"

    try:
        # Send an HTTP GET request to fetch data for the specified Pokémon
        response = requests.get(f"{base_url}{pokemon_name.lower()}")

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Display information about the Pokémon
            print(f"Name: {data['name'].capitalize()}")
            print(f"ID: {data['id']}")
            print("Abilities:")
            for ability in data['abilities']:
                print(f"- {ability['ability']['name'].capitalize()}")
        else:
            print(f"Error: Unable to fetch data. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Input the name of the Pokémon you want to fetch
    pokemon_name = input("Enter the name of the Pokémon: ")
    fetch_pokemon_data(pokemon_name)
