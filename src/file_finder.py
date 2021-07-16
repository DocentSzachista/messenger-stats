import os 


def file_finder(directory = os.path.dirname(__file__)) -> list:
    """finds .json files under given directory 
    
    Parameters
    ----------
    directory : str 
        string which is directory to a folder where it is supposed to look for JSON files
        (default: gets a directory from file path )
    
    Returns
    -------
    list of paths of JSON files 
    
    """
    return [ directory+"/"+fileName for fileName in os.listdir(directory) if fileName.endswith(".json") ]