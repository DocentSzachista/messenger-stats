from data_organiser import DataOrganiser


if __name__ == "__main__":
    dataOrganiser = DataOrganiser()
    dataOrganiser.printDetectedFiles()
    dataOrganiser.makeDiagramsForEachFile()
    # list_of_files = file_finder("./")
    # print (list_of_files)

    # FileParse = FileParser(list_of_files[0])
    # list_of_authors = FileParse.retrieve_authors()
    # list_of_message_data = FileParse.retrieve_messages()
    # dicts = count_ammount_of_messages(list_of_message_data)
    # dictionary = give_me_given_char_occurence(list_of_message_data, list_of_authors)
    # longest = count_the_longest_message(list_of_message_data, list_of_authors)
    # deletions = count_ammount_of_messages_deleted(list_of_message_data, list_of_authors)

    # data_for_diagrams = { "liczba wiadomosci" : dicts,
    #                  "Wystapienia w wiadomosci xD" : dictionary,
    #                      "najdlusza wiadomosc": longest,
    #                          "Ilosc usuniec wiadomosci"  : deletions }
    # generate_figures(data_for_diagrams, "Piotr", "bar")

  