import unittest

from city_functions import city_country
#we've imported a function from a file city_functions so we don't have to write it again

class CitiesTestCase(unittest.TestCase):
    """Test for city_functions"""
    def test_city_country(self):
        london_england = city_country("london", "england")
        self.assertEqual(london_england, "London, England")

    def test_city_country_population(self):
        london_england = city_country("london", "england", "8900000")
        self.assertEqual(london_england, "London, England, 8900000")


if __name__ == '__main__':
        unittest.main()