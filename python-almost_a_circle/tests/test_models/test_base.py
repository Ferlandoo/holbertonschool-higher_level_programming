import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_init_with_id(self):
        base = Base(1)
        self.assertEqual(base.id, 1)

    def test_init_without_id(self):
        base = Base()
        self.assertIsNotNone(base.id)

    def test_to_json_string(self):
        base = Base(1)
        json_string = base.to_json_string([{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}])
        self.assertEqual(json_string, '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]')

    def test_save_to_file(self):
        base1 = Base(1)
        base2 = Base(2)
        Base.save_to_file([base1, base2])
        # Add assertions to check if the file was saved correctly

    def test_from_json_string(self):
        json_string = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        objects = Base.from_json_string(json_string)
        self.assertEqual(len(objects), 2)
        self.assertEqual(objects[0]['id'], 1)
        self.assertEqual(objects[1]['name'], 'Jane')

    def test_create(self):
        dictionary = {'id': 1, 'name': 'John'}
        base = Base.create(**dictionary)
        self.assertEqual(base.id, 1)
        self.assertEqual(base.name, 'John')

    def test_load_from_file(self):
        # Create a test file with some objects
        objects = Base.load_from_file()
        self.assertEqual(len(objects), 2)
        self.assertEqual(objects[0].id, 1)
        self.assertEqual(objects[1].name, 'Jane')


if __name__ == '__main__':
    unittest.main()
