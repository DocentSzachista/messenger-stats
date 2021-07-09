import json
#otworz plik JSON aby potem uzyskac slownik zawierajacy informacje o autorach i caly kontent wiadomosci
""""""
class FileParser:
    def __init__(self, filename) -> None:
        self.jsonData=self._parse_json(filename)

    def _parse_json(self, filename)->dict:
        with open(filename, 'r', encoding='UTF-8') as file:
            list_of_dictonaries= json.load(file)
            return list_of_dictonaries
    def retrieve_authors(self)->list:
        listing = self.jsonData.get("participants")
        listing = [element.get("name") for element in listing ]
        return listing
    """retrieve a list of dicts containing details about sent messages"""
    def retrieve_messages(self)->list:
        return self.jsonData.get("messages")
