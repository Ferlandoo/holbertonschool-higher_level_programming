import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        # Create a test rectangle
        self.rectangle = Rectangle(5, 10, 2, 3, 1)

    def test_attributes(self):
        # Test attributes initialization
        self.assertEqual(self.rectangle.width, 5)
        self.assertEqual(self.rectangle.height, 10)
        self.assertEqual(self.rectangle.x, 2)
        self.assertEqual(self.rectangle.y, 3)
        self.assertEqual(self.rectangle.id, 1)

    def test_width_invalid_type(self):
        # Test width setter with invalid type
        with self.assertRaises(TypeError):
            self.rectangle.width = 'abc'

    def test_width_invalid_value(self):
        # Test width setter with invalid value
        with self.assertRaises(ValueError):
            self.rectangle.width = -5

    def test_height_invalid_type(self):
        # Test height setter with invalid type
        with self.assertRaises(TypeError):
            self.rectangle.height = 'abc'

    def test_height_invalid_value(self):
        # Test height setter with invalid value
        with self.assertRaises(ValueError):
            self.rectangle.height = -10

    def test_x_invalid_type(self):
        # Test x setter with invalid type
        with self.assertRaises(TypeError):
            self.rectangle.x = 'abc'

    def test_x_invalid_value(self):
        # Test x setter with invalid value
        with self.assertRaises(ValueError):
            self.rectangle.x = -2

    def test_y_invalid_type(self):
        # Test y setter with invalid type
        with self.assertRaises(TypeError):
            self.rectangle.y = 'abc'

    def test_y_invalid_value(self):
        # Test y setter with invalid value
        with self.assertRaises(ValueError):
            self.rectangle.y = -3

    def test_area(self):
        # Test area calculation
        self.assertEqual(self.rectangle.area(), 5 * 10)

    def test_display(self):
        # Test display method
        expected_output = "\n\n  #####\n  #####\n  #####\n  #####\n  #####\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.rectangle.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_to_dictionary(self):
        # Test to_dictionary method
        expected_dict = {'x': 2, 'width': 5, 'id': 1, 'height': 10, 'y': 3}
        self.assertEqual(self.rectangle.to_dictionary(), expected_dict)

    def test_update(self):
        # Test update method
        self.rectangle.update(10, 20, 3, 4, 5)
        self.assertEqual(self.rectangle.id, 10)
        self.assertEqual(self.rectangle.width, 20)
        self.assertEqual(self.rectangle.height, 3)
        self.assertEqual(self.rectangle.x, 4)
        self.assertEqual(self.rectangle.y, 5)


if __name__ == '__main__':
    unittest.main()
