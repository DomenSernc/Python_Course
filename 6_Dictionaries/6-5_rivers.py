rivers = {
    "nile": "egypt",
    "soca": "slovenia",
    "missisipi": "USA",
}

for river, country in rivers.items():
    print (f"{river.title()} runs through {country.title()}.")

for river in rivers:
    print (river.title())

for country in rivers.values():
    print(country.title())