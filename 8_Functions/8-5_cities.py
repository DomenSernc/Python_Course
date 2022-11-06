def describe_city(city, country):
    print(f"{city} is in {country}.")

describe_city("London", "United Kingdom")

def describe_city_1(city, country = "United Kingdom"):
    print(f"{city} is in {country}.")

describe_city_1("Manchester")
describe_city_1("Liverpool")
describe_city_1("Birmingham")