import xmltodict
import json
from database import create_words


class XmlImporter():
    @classmethod
    def import_data(cls, name_file):
        if ".xml" not in name_file:
            raise ValueError("Arquivo inválido")
        with open(name_file, "r") as file:
            dict_file = xmltodict.parse(file.read())
            records = dict_file["dic"]["entry"]
            converted_to_dict = json.loads(json.dumps(records))
            list_with_five_len = []
            for i in list(converted_to_dict):
                if len(i["@id"]) == 5:
                    list_with_five_len.append({"word": i["@id"]})
            create_words(list_with_five_len)
            return list_with_five_len


def main():
    XmlImporter().import_data("dicionarioXML/A.xml")
    XmlImporter().import_data("dicionarioXML/B.xml")
    XmlImporter().import_data("dicionarioXML/C.xml")
    XmlImporter().import_data("dicionarioXML/D.xml")
    XmlImporter().import_data("dicionarioXML/E.xml")
    XmlImporter().import_data("dicionarioXML/F.xml")
    XmlImporter().import_data("dicionarioXML/G.xml")
    XmlImporter().import_data("dicionarioXML/H.xml")
    XmlImporter().import_data("dicionarioXML/I.xml")
    XmlImporter().import_data("dicionarioXML/J.xml")
    XmlImporter().import_data("dicionarioXML/L.xml")
    XmlImporter().import_data("dicionarioXML/M.xml")
    XmlImporter().import_data("dicionarioXML/N.xml")
    XmlImporter().import_data("dicionarioXML/O.xml")
    XmlImporter().import_data("dicionarioXML/P.xml")
    XmlImporter().import_data("dicionarioXML/Q.xml")
    XmlImporter().import_data("dicionarioXML/R.xml")
    XmlImporter().import_data("dicionarioXML/S.xml")
    XmlImporter().import_data("dicionarioXML/T.xml")
    XmlImporter().import_data("dicionarioXML/U.xml")
    XmlImporter().import_data("dicionarioXML/V.xml")
    XmlImporter().import_data("dicionarioXML/W.xml")
    XmlImporter().import_data("dicionarioXML/X.xml")
    XmlImporter().import_data("dicionarioXML/Z.xml")


if __name__ == "__main__":
    main()
