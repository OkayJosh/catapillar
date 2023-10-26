import json


class Data2botSchemaGenerator:
    def __init__(self, input_file: str, output_file: str):
        """
        Initialize the Data2botSchemaGenerator.

        Args:
            input_file (str): Path to the input JSON file.
            output_file (str): Path to the output schema JSON file.
        """
        self.input_file = input_file
        self.output_file = output_file

    def generate_json_schema(self):
        """
        Generate a JSON schema based on the input JSON data.

        Returns:
            dict: The generated JSON schema.
        """
        schema = {}
        with open(self.input_file, "r") as file:
            json_data = json.load(file)
            message = json_data.get('message', None)
            if message:
                for key, value in message.items():
                    schema[key] = {
                        "type": self.infer_data_type(value),
                        "tag": "",
                        "description": "",
                        "required": False
                    }
        return schema

    @staticmethod
    def infer_data_type(data):
        """
        Infer the data type of a value.

        Args:
            data: The value to infer the data type for.

        Returns:
            str: The inferred data type.
        """
        if isinstance(data, str):
            return "STRING"
        elif isinstance(data, int):
            return "INTEGER"
        elif isinstance(data, bool):
            return "BOOLEAN"
        elif isinstance(data, list):
            return "ENUM"
        elif isinstance(data, dict):
            return "ARRAY"
        else:
            return "unknown"

    def save_schema_to_file(self, schema):
        """
        Save the JSON schema to an output file.

        Args:
            schema (dict): The JSON schema to save.
        """
        with open(self.output_file, "w") as file:
            json.dump(schema, file, indent=2)

    def generate_and_save_schema(self):
        """
        Generate the JSON schema and save it to the specified output file.
        """
        schema = self.generate_json_schema()
        self.save_schema_to_file(schema)
