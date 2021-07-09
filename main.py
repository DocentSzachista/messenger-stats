from file_parser import FileParser
from data_handler import give_me_given_char_occurence
from data_handler import count_ammount_of_messages
from data_handler import count_the_longest_message
#from data_handler import sort_given_values_to_person


#list_of_message_data = parse_json("Lis.json")

#sorted_dict = give_me_given_char_occurence(list_of_message_data, "xD")
#print(sorted_dict)
#print(count_ammount_of_messages(list_of_message_data))
if __name__ == "__main__":
    FileParse = FileParser("Lis.json")
    list_of_authors = FileParse.retrieve_authors()
    list_of_message_data = FileParse.retrieve_messages()
    print(count_ammount_of_messages(list_of_message_data))
    #print(list_of_authors)
   # print(list_of_message_data)
    dictionary = give_me_given_char_occurence(list_of_message_data, list_of_authors)
    print(dictionary.values())
    print(count_the_longest_message(list_of_message_data, list_of_authors))