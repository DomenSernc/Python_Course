"""Functions for working with cities"""

def city_country(city, country, population=""):
    #putting the population in an empty default value makes it optional
    """Return a string"""
    if population:
        city_country_result = f"{city.title()}, {country.title()}, {population.title()}"
    else: 
        city_country_result = f"{city.title()}, {country.title()}"
    return city_country_result



