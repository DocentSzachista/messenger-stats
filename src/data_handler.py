# #Sortuj szukany rodzaj danych do danej osoby
# def sort_given_values_to_person(list_of_dicts_of_data, data_to_be_collected)->dict:
#     dictionary_of_desired_values ={}
#     for dict in list_of_dicts_of_data:
#         if dict.get(data_to_be_collected) is not None:
#             dictionary_of_desired_values.setdefault(dict.get("sender_name"),[]).append(dict.get(data_to_be_collected))
#     return dictionary_of_desired_values


#TODO think of exception that could be thrown and make exception handling  

#wydobadz z listy slownikow wybrany ciag znakow i zlicz jego ilosc (uzycie str.count() by dostac mniej zaklamane wyniki)
def give_me_given_char_occurence(list_of_data, authors, substring="xD", author_to_ignore=None )->dict:
    """ count an ammount of given char occurences in a chat messages

    Parameters
    ----------
    list_of_data: list
        list of dictionaries holding the data about conversation

    authors: list
        list of chats participants

    substring: str, opt
        given string/char to look in chat (default is "xD")

    author_to_ignore: str, opt 
        name of the participant to ignore, should be used when we don't care about particular user (default is "sxcqw", will change it later for something more convenient)
    Returns
    -------

    dict holding the overall number of appearance of given string for each participant of the chat

    """

    #desired_values={name: [value.get("content") for value in list_of_data if value.get("content") is not None and str(value.get("content")).capitalize().find(substring.capitalize())!=-1 ] for name in authors if name.find(author_to_ignore)==-1 }
    desired_values= {k:0 for k in authors if author_to_ignore == None or k.find(author_to_ignore)== -1 }
    for dict in list_of_data:
        value = dict.get("content")
        if value is not None:
            if author_to_ignore == None or author_to_ignore not in dict.get("sender_name") :
                if  substring.lower() in str(value).lower() or   substring in str(value):
                    desired_values.update({dict.get("sender_name"): desired_values.get(dict.get("sender_name"))+1})
    return desired_values

#wydobadz z listy slownikow ilosc wiadomosci do wybranych osob
def count_ammount_of_messages(list_of_data, author_to_ignore=None) -> dict:
    """ count an ammount of written messages by each of the participants

    Parameters
    ----------
    list_of_data: list
        list of dictionaries holding the data about conversation
    
    author_to_ignore: str, opt 
        name of the participant to ignore, should be used when we don't care about particular user (default is "sxcqw", will change it later for something more convenient)

    Returns
    -------

    dict holding the overall number of appearance of given string for each participant of the chat

    """
    desired_values={}
    for dict in list_of_data:
        if(dict.get("content") is not None):
            if author_to_ignore ==None or author_to_ignore != dict.get("sender_name"):
                value = desired_values.setdefault(dict.get("sender_name"),0)
                if value is not None:
                    desired_values.update({dict.get("sender_name"): value+1})
    return desired_values

#policz dlugosci wiadomosci 
def count_the_longest_message(list_of_data, authors, author_to_ignore=None)-> dict:
    """ finds the longests message lenght

    Parameters
    ----------
    
    list_of_data: list
        list of dictionaries holding the data about conversation

    authors: list
        list of chats participants

    Returns
    -------

    dict holding information about the longest message written by each participant
    
    """
    desired_values= {k:0 for k in authors if author_to_ignore == None or k.find(author_to_ignore)== -1 }
    for dict in list_of_data:
        if author_to_ignore ==None or author_to_ignore != dict.get("sender_name"):
            value = dict.get("content")
            temp_max = desired_values.get(dict.get("sender_name"))
            if value is not None and temp_max < len(value): 
                        desired_values.update({dict.get("sender_name"): len(value)})
    return desired_values
    
#policz ile kto wiadomosci cofnal wyslanie wiadomosci
def count_ammount_of_messages_deleted(list_of_data, authors, author_to_ignore=None)->dict:
    """ finds the longests message lenght

    Parameters
    ----------
    
    list_of_data: list
        list of dictionaries holding the data about conversation

    authors: list
        list of chats participants

    Returns
    -------

    dict holding information how many messages were deleted by each participant
    
    """
    desired_values= {k:0 for k in authors if author_to_ignore == None or k.find(author_to_ignore)== -1 }
    for dict in list_of_data:
        if author_to_ignore ==None or author_to_ignore != dict.get("sender_name"):
            if dict.get("is_unsent") is True:
                desired_values.update( {dict.get("sender_name") : desired_values.get(dict.get("sender_name"))+1} )
    return desired_values