import json
#otworz plik JSON aby potem uzyskac slownik zawierajacy informacje o autorach i caly kontent wiadomosci

class FileParser:
    """class to process messenger JSON files"""
    def __init__(self, filename) -> None:
        self.jsonData=self.__parse_json(filename)
   
    def __parse_json(self, filename)->dict:
        """read whole content of a JSON file 
        
        function saves the content of JSON file to a dictionary of lists of dictionaries.
        files contens are decoded from latin and encoded to UTF-8 during saving into a data structure 
         
        Parameters
        ----------
        filename: str
            string containing information the name and location of a file to read
            
        Returns
        -------
        dict that contains the data about conversation 
         """
        with open(filename, 'r', encoding='raw_unicode_escape') as file:
            list_of_dictonaries= json.loads(file.read().encode('raw_unicode_escape').decode())
            return list_of_dictonaries
    
    def retrieve_authors(self)->list:
        """ getter function to return a list of a conversation's participants
        
        Returns
        -------
        list of conversation's participants 
        """
        listing = self.jsonData.get("participants")
        listing = [element.get("name") for element in listing ]
        return listing
    
    def retrieve_messages(self)->list:
        """retrieve a list of dicts containing details about sent messages
        
        Returns
        -------
        list of conversation's details
        """
        return self.jsonData.get("messages")
        