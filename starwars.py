import requests

def get_planet_name(planet_url):

    planet_info = requests.get(planet_url)

    if (planet_info):
        planet_json = planet_info.json()

        return planet_json['name']

def get_films_names(films_url):

    films_names = []

    for film_url in films_url:

        film_info = requests.get(film_url)

        if film_info:

            film_json = film_info.json()

            films_names = films_names + [film_json['title']]

    return films_names


name = input("Introduzca el nombre del personaje para buscar: ")

# The API endpoint
url = "https://swapi.dev/api/people"

# A GET request to the API
response = requests.get(url)

if (response):
    response_json = response.json()

    people = response_json["results"]

    for person in people:
        if name != person['name']:
            continue
        else:
            planet_url = person['homeworld']
            films_url = person['films']

            planet_name = get_planet_name(planet_url)
            films_names = get_films_names(films_url)

            print(f'{name} pertenece al planeta {planet_name}')

            for film_name in films_names:
                print(f'Aparece en la película {film_name}')



else:
    print(response)
