import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def setUp(self):
        self.square = Square(5)

    def test_init(self):
        self.assertEqual(self.square.size, 5)
        self.assertEqual(self.square.x, 0)
        self.assertEqual(self.square.y, 0)
        self.assertIsNone(self.square.id)

    def test_str(self):
        expected_output = "[Square] (1) 0/0 - 5"
        self.assertEqual(str(self.square), expected_output)

    def test_size(self):
        self.assertEqual(self.square.size, 5)
        self.square.size = 10
        self.assertEqual(self.square.size, 10)

    def test_update(self):
        self.square.update(10)
        self.assertEqual(self.square.id, 10)
        self.square.update(20, 2, 3, 15)
        self.assertEqual(self.square.id, 20)
        self.assertEqual(self.square.size, 2)
        self.assertEqual(self.square.x, 3)
        self.assertEqual(self.square.y, 15)

    def test_to_dictionary(self):
        expected_output = {'id': 1, 'size': 5, 'x': 0, 'y': 0}
        self.assertEqual(self.square.to_dictionary(), expected_output)

if __name__ == '__main__':
    unittest.main()
