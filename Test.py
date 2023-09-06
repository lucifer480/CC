import unittest
from Main import to_upper

class MyTestCase(unittest.TestCase):
    def test_to_upper(self):
        name = "Utkarsh"
        upper_name = to_upper(name)
        self.assertEqual(upper_name, "Utkarsh")

if __name__ == '__main__':
    unittest.main()