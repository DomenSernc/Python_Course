cities = {
    "London": {
        "country": "UK",
        "population": "9 million",
        "fact": "117 museums",
        },

    "Paris": {
        "country": "France",
        "population": "2 million",
        "fact": "city of light",
        },  

    "Ljubljana": {
        "country": "Slovenia",
        "population": "300 thousand",
        "fact": "was once called Laibach",
        }  
    }

for city, data in cities.items():
    print(f"\nCity: {city}")
    
    drzava = f"{data['country']}"
    populacija = f"{data['population']}"
    podatek = f"{data['fact']}"


    print(f"\tCountry: {drzava.title()}")
    print(f"\tPopulation: {populacija.title()}")
    print(f"\tFact: {podatek.title()}")