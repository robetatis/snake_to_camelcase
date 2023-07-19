import json
import re
import copy

class SnakeToCamelCase:

    def __init__(self, string_snake_raw):
        self.string_snake_raw = string_snake_raw

    def read_snake(self):
        self.string_snake = json.loads(self.string_snake_raw)

    def run(self):
        self.read_snake()
        self.string_camel = copy.deepcopy(self.string_snake)
        for key_snake in self.string_snake.keys():
            key_1st_cap = re.search('_+([a-z])', key_snake).group(1).upper()
            key_camel = re.sub('_+[a-z]', key_1st_cap, key_snake)
            self.string_camel[key_camel] = self.string_camel.pop(key_snake)
