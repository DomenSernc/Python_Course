favorite_places = {
    "Domen": ["London", "Berlin", "Prague"],
    "Jayson": ["Ljubljana", "Washington"],
    "Eva": "Paris",
}

for person, places in favorite_places.items():
    #method .items() returns a list of key-value pairs
    print(f"{person}: {places}")