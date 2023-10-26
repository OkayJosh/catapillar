# Data2bot Schema Generator

This Python project provides a JSON Schema generator called Data2bot 
Schema Generator that can infer JSON schema from input JSON data and 
save the schema to an output file. The schema is generated based on the
structure of the input data, and additional attributes such as "tag," 
"description," and "required" can be customized.

## Getting Started

Follow these steps to clone the repository, set up a virtual environment, run the tests, and start the application:

1. **Clone the Repository:**

    ```bash
    git clone <repo_url>
    ```

2. **Create a Virtual Environment:**

    It's recommended to create a virtual environment to manage project dependencies. You can use Python's built-in `venv` module to create one. Navigate to the project directory and run:

    ```bash
    python -m venv venv
    ```

    Activate the virtual environment:

    - On Windows:

    ```bash
    venv\Scripts\activate
    ```

    - On macOS and Linux:

    ```bash
    source venv/bin/activate
    ```

3. **Run the Tests:**

    Run the test suite using the following command:

    ```bash
    python -m unittest tests.TestData2botSchemaGenerator
    ```

    This will ensure that the JSON Schema Generator works as expected.

4. **Run the Application:**

    To use the JSON Schema Generator, you can create an instance of the `Data2botSchemaGenerator` class and use its methods in your application. Here's an example:

    ```python
    from generator import Data2botSchemaGenerator

    input_file = "input.json"
    output_file = "output_schema.json"
    
    schema_generator = Data2botSchemaGenerator(input_file, output_file)
    schema_generator.generate_and_save_schema()
    ```

    Replace `input.json` with your input JSON file, and `output_schema.json` with your desired output schema file. This code will generate the JSON schema and save it to the specified output file.

## Contributing

If you'd like to contribute to this project, please follow these guidelines:

- Fork the repository on GitHub.
- Create a new branch for your feature or bug fix.
- Make your changes and test them.
- Submit a pull request to the main repository.

Please make sure to follow the existing code style and add relevant test cases for new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
