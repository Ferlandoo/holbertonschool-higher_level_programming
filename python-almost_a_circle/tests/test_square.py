import unittest
from square import Square


class TestSquare(unittest.TestCase):

    def setUp(self):
        # Create a test square
        self.square = Square(5, 2, 3, 1)

    def test_attributes(self):
        # Test attributes initialization
        self.assertEqual(self.square.width, 5)
        self.assertEqual(self.square.height, 5)
        self.assertEqual(self.square.x, 2)
        self.assertEqual(self.square.y, 3)
        self.assertEqual(self.square.id, 1)

    def test_size_property(self):
        # Test size property
        self.assertEqual(self.square.size, 5)

    def test_size_setter(self):
        # Test size setter
        self.square.size = 10
        self.assertEqual(self.square.size, 10)
        self.assertEqual(self.square.width, 10)
        self.assertEqual(self.square.height, 10)

    def test_update(self):
        # Test update method
        self.square.update(10, 20, 4, 5)
        self.assertEqual(self.square.id, 10)
        self.assertEqual(self.square.size, 20)
        self.assertEqual(self.square.x, 4)
        self.assertEqual(self.square.y, 5)

    def test_to_dictionary(self):
        # Test to_dictionary method
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(self.square.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
