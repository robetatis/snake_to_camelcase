from SnakeToCamelCase import SnakeToCamelCase

if __name__ == '__main__':
    input_string = '{"first_name": "John", "last_name": "Doe"}'
    converter = SnakeToCamelCase(input_string)
    converter.run()
    print('input string:', input_string)
    print('output string:', converter.string_camel)

