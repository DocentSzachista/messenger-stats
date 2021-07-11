import json
#otworz plik JSON aby potem uzyskac slownik zawierajacy informacje o autorach i caly kontent wiadomosci
"""class to process messenger JSON files"""
class FileParser:
    def __init__(self, filename) -> None:
        self.jsonData=self.__parse_json(filename)
    """read whole content of a JSON file and return it as a dictionary of lists of dictionaries.
       files are decoded from latin and later encoded to UTF-8 cause polish signs :) """
    def __parse_json(self, filename)->dict:
        with open(filename, 'r', encoding='raw_unicode_escape') as file:
            list_of_dictonaries= json.loads(file.read().encode('raw_unicode_escape').decode())
            return list_of_dictonaries
    """just a getter function to return a list of conversation participants"""
    def retrieve_authors(self)->list:
        listing = self.jsonData.get("participants")
        listing = [element.get("name") for element in listing ]
        return listing
    """retrieve a list of dicts containing details about sent messages"""
    def retrieve_messages(self)->list:
        return self.jsonData.get("messages")
        