import xmltodict
import json


class XmlImporter():
    @classmethod
    def import_data(cls, name_file):
        if ".xml" not in name_file:
            raise ValueError("Arquivo inválido")
        with open(name_file, "r") as file:
            dict_file = xmltodict.parse(file.read())
            records = dict_file["dic"]["entry"]
            converted_to_dict = json.loads(json.dumps(records))
            teste = []
            for i in list(converted_to_dict):
                if len(i["@id"]) == 5:
                    teste.append(i["@id"])
            return teste


if __name__ == "__main__":
    print(XmlImporter().import_data("dicionarioXML/A.xml"))
