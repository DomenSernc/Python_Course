def car_info(manufacturer, model_name, **car_data):
    #the ** double stars call for a dictionary, where manufacturer and model_name are the two default
    #keys of a dictinoary. other keys are optional.
    """Make a function about car data"""

    car_data["corporation"] = manufacturer
    car_data["model"] = model_name
    return car_data

car_information = car_info("Audi", "A8",
                            color = "blue",
                            horse_power = 130,
                            year_of_manufacture = 2015,)

print(car_information)