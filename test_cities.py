import unittest
from city_functions import get_city_country


class CityCountryTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'"""

    def test_city_country(self):
        """Do data in the form 'Warsaw, Poland' are manned properly?"""
        formatted_text = get_city_country('warsaw', 'poland')
        self.assertEqual(formatted_text, 'Warsaw, Poland')

    def test_city_country_population(self):
        """Do data in the form 'Warsaw, Poland - population 3600000' are manned properly?"""
        formatted_text = get_city_country('warsaw', 'poland', 3600000)
        self.assertEqual(formatted_text, 'Warsaw, Poland - population 3600000'
                                         '')


if __name__ == '__main__':
    unittest.main()
