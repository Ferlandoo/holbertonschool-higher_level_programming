import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):

    def setUp(self):
        # Initialize some test objects
        self.rectangle1 = Rectangle(1, 2, 3, 4)
        self.rectangle2 = Rectangle(5, 6, 7, 8)
        self.square1 = Square(10, 11, 12)
        self.square2 = Square(20, 21, 22)

    def tearDown(self):
        # Clean up created files
        try:
            os.remove("Rectangle.json")
            os.remove("Square.json")
        except FileNotFoundError:
            pass

    def test_save_to_file(self):
        # Test saving objects to file
        Rectangle.save_to_file([self.rectangle1, self.rectangle2])
        Square.save_to_file([self.square1, self.square2])
        self.assertTrue(os.path.isfile("Rectangle.json"))
        self.assertTrue(os.path.isfile("Square.json"))

    def test_load_from_file(self):
        # Test loading objects from file
        Rectangle.save_to_file([self.rectangle1, self.rectangle2])
        Square.save_to_file([self.square1, self.square2])
        rectangles = Rectangle.load_from_file()
        squares = Square.load_from_file()
        self.assertEqual(len(rectangles), 2)
        self.assertEqual(len(squares), 2)
        self.assertIsInstance(rectangles[0], Rectangle)
        self.assertIsInstance(rectangles[1], Rectangle)
        self.assertIsInstance(squares[0], Square)
        self.assertIsInstance(squares[1], Square)

    def test_to_json_string(self):
        # Test converting objects to JSON string
        rectangle_json = Rectangle.to_json_string([self.rectangle1.to_dictionary(), self.rectangle2.to_dictionary()])
        square_json = Square.to_json_string([self.square1.to_dictionary(), self.square2.to_dictionary()])
        self.assertIsInstance(rectangle_json, str)
        self.assertIsInstance(square_json, str)

    def test_from_json_string(self):
        # Test converting JSON string to objects
        rectangle_json = Rectangle.to_json_string([self.rectangle1.to_dictionary(), self.rectangle2.to_dictionary()])
        square_json = Square.to_json_string([self.square1.to_dictionary(), self.square2.to_dictionary()])
        rectangles = Rectangle.from_json_string(rectangle_json)
        squares = Square.from_json_string(square_json)
        self.assertIsInstance(rectangles, list)
        self.assertIsInstance(squares, list)
        self.assertEqual(len(rectangles), 2)
        self.assertEqual(len(squares), 2)
        self.assertIsInstance(rectangles[0], dict)
        self.assertIsInstance(rectangles[1], dict)
        self.assertIsInstance(squares[0], dict)
        self.assertIsInstance(squares[1], dict)

    def test_create(self):
        # Test creating objects from dictionary
        rectangle_dict = {'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5}
        square_dict = {'id': 6, 'size': 7, 'x': 8, 'y': 9}
        rectangle = Rectangle.create(**rectangle_dict)
        square = Square.create(**square_dict)
        self.assertIsInstance(rectangle, Rectangle)
        self.assertIsInstance(square, Square)
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(square.id, 6)
        self.assertEqual(rectangle.width, 2)
        self.assertEqual(square.size, 7)
        self.assertEqual(rectangle.x, 4)
        self.assertEqual(square.x, 8)
        self.assertEqual(rectangle.y, 5)
        self.assertEqual(square.y, 9)


if __name__ == '__main__':
    unittest.main()
