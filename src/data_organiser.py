from os import path

from file_parser import FileParser
from file_finder  import file_finder
from data_handler import *
from diagram_creator import generate_figures

class DataOrganiser:
    """Class that handles formatting the data for diagrams"""
    def __init__(self) -> None:
        self.listOfFiles = file_finder("messenger-statistics/jsons")
    
    def printDetectedFiles(self) -> None:
        """prints every filename with .json extension"""
        print(self.listOfFiles)
        for pathname in self.listOfFiles:
            print(pathname)


    def makeDiagramsForEachFile(self, save=True) -> None:
        """process every file and save a fig to a file """
        for pathname in self.listOfFiles:
            tempDict = {}
            fileParser = FileParser(pathname)
            tempDict.update( {"ilosc wystapien xD w wiadomosciach" : give_me_given_char_occurence(fileParser.retrieve_messages(), fileParser.retrieve_authors(), "xD")})
            tempDict.update( {"ilosc napisanych wiadomosci" : count_ammount_of_messages(fileParser.retrieve_messages()) })
            tempDict.update( {"Najdluzsza wiadomosc": count_the_longest_message(fileParser.retrieve_messages(), fileParser.retrieve_authors())})
            tempDict.update( {"Ilosc wycofania wiadomosci do wyslania":  count_ammount_of_messages_deleted(fileParser.retrieve_messages(), fileParser.retrieve_authors())})
            generate_figures(tempDict, path.basename(pathname), to_save=save)
            
