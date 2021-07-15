import json
#otworz plik JSON aby potem uzyskac slownik zawierajacy informacje o autorach i caly kontent wiadomosci

class FileParser:
    """class to process messenger JSON files"""
    def __init__(self, filename) -> None:
        self.jsonData=self.__parse_json(filename)
   
    def __parse_json(self, filename)->dict:
        """read whole content of a JSON file and return it as a dictionary of lists of dictionaries.
        files are decoded from latin and later encoded to UTF-8 cause polish signs :) """
        with open(filename, 'r', encoding='raw_unicode_escape') as file:
            list_of_dictonaries= json.loads(file.read().encode('raw_unicode_escape').decode())
            return list_of_dictonaries
    
    def retrieve_authors(self)->list:
        """just a getter function to return a list of conversation participants"""
        listing = self.jsonData.get("participants")
        listing = [element.get("name") for element in listing ]
        return listing
    
    def retrieve_messages(self)->list:
        """retrieve a list of dicts containing details about sent messages"""
        return self.jsonData.get("messages")
        