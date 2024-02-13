import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rect = Rectangle(5, 10, 1, 2, 100)

    def test_width(self):
        self.assertEqual(self.rect.width, 5)
        self.rect.width = 8
        self.assertEqual(self.rect.width, 8)

    def test_height(self):
        self.assertEqual(self.rect.height, 10)
        self.rect.height = 12
        self.assertEqual(self.rect.height, 12)

    def test_x(self):
        self.assertEqual(self.rect.x, 1)
        self.rect.x = 3
        self.assertEqual(self.rect.x, 3)

    def test_y(self):
        self.assertEqual(self.rect.y, 2)
        self.rect.y = 4
        self.assertEqual(self.rect.y, 4)

    def test_area(self):
        self.assertEqual(self.rect.area(), 50)

    def test_display(self):
        # Add your test logic here
        pass

    def test_str(self):
        # Add your test logic here
        pass

    def test_update(self):
        # Add your test logic here
        pass

    def test_to_dictionary(self):
        # Add your test logic here
        pass

if __name__ == '__main__':
    unittest.main()
