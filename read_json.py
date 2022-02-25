import json
from database import create_words


# ..source: https://www.geeksforgeeks.org/
# ..    reading-and-writing-json-to-a-file-in-python/
class JsonImporter():
    @classmethod
    def import_data(cls, name_file):
        if ".json" not in name_file:
            raise ValueError("Arquivo inválido")
        with open(name_file, 'r') as openfile:
            json_object = json.load(openfile)
            return list(json_object["words"])


def send_data_to_db(words):
    list_of_dict = []
    for i in words:
        list_of_dict.append({"word": i})
    create_words(list_of_dict)


# send_data_to_db(JsonImporter().import_data("database/sample.json"))
print(JsonImporter().import_data("database/sample.json"))
