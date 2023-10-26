import unittest
import json
from generator import Data2botSchemaGenerator


class TestData2botSchemaGenerator(unittest.TestCase):
    def setUp(self):
        self.input_file = "./data/test/data_1.json"
        self.output_file = "./data/test/test_output.json"

    def tearDown(self):
        # Clean up after each test by removing the test output file.
        import os
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_generate_json_schema(self):
        # Initialize the Data2botSchemaGenerator and call generate_json_schema.
        schema_generator = Data2botSchemaGenerator(self.input_file, self.output_file)
        schema = schema_generator.generate_json_schema()

        # Verify that the generated schema matches the expected schema.
        expected_schema = {
              "battle": {
                "type": "ARRAY",
                "tag": "",
                "description": "",
                "required": False
              },
              "joiner": {
                "type": "ARRAY",
                "tag": "",
                "description": "",
                "required": False
              },
              "participantIds": {
                "type": "ENUM",
                "tag": "",
                "description": "",
                "required": False
              }
            }
        self.assertEqual(schema, expected_schema)

    def test_generate_and_save_schema(self):
        # Initialize the Data2botSchemaGenerator and call generate_and_save_schema.
        schema_generator = Data2botSchemaGenerator(self.input_file, self.output_file)
        schema_generator.generate_and_save_schema()

        # Read the saved schema from the output file.
        with open(self.output_file, "r") as file:
            saved_schema = json.load(file)

        # Verify that the saved schema matches the expected schema.
        expected_schema = {
              "battle": {
                "type": "ARRAY",
                "tag": "",
                "description": "",
                "required": False
              },
              "joiner": {
                "type": "ARRAY",
                "tag": "",
                "description": "",
                "required": False
              },
              "participantIds": {
                "type": "ENUM",
                "tag": "",
                "description": "",
                "required": False
              }
            }
        self.assertEqual(saved_schema, expected_schema)


if __name__ == '__main__':
    unittest.main()
