from generator import Data2botSchemaGenerator

if __name__ == "__main__":
    input_file = "./data/data_1.json"
    output_file = "./schema/output_schema.json"

    schema_generator = Data2botSchemaGenerator(input_file, output_file)
    schema_generator.generate_and_save_schema()
