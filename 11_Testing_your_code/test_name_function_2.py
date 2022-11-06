import unittest
from name_function_2 import get_formatted_name

#1
class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
#2
        formatted_name = get_formatted_name('janis', 'joplin')
#3
        self.assertEqual(formatted_name, 'Janis Joplin')
        #The line says, “Compare the value in formatted_name to the string 'Janis Joplin'.

#4
if __name__ == '__main__':
        unittest.main()