def city_country(city, country):
    """Return a city and a country"""

    cityandcountry = f"{city} {country}"
    return cityandcountry.title()

destination = city_country("Ottawa", "Canada")
print(destination)

destination = city_country("London", "United Kingdom")
print(destination)

destination = city_country("Paris", "France")
print(destination)

