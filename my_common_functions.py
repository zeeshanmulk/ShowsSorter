# Author Zeeshan Mulk
# A list of functions that I commonly use in my programs.
import os
import logging

# This returns the list of all directories in the provided source_directory as a list.
def get_list_of_dirs (source_directory):
    for root, dirs, files in os.walk (source_directory):
        d = []
        for each_dir in dirs:
            d.append(each_dir)

        return d
# This creates the directory at the passed on dir_name and returns the path.
def make_directory (dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    return (dir_name)

# This renames a file or a directory.
def rename_directory (source, destination):
    try:
        os.rename(source, destination)
        string = source + " has been renamed to: " + destination
        print(string)
        logging.info(string)
        return True
    except OSError as Err:
        print("OS error: {0}".format(Err))
        return False

# This writes a text file with some content. Not used in this demonstration yet.
def write_text_file(filename, filecontent):
    try:
         with open (filename, "a") as f:
             for item in filecontent:
                 print(item)
                 f.write(item + "\n")
    except IOError:
        print ("An error has occoured.")

# This opens a filename with a multiple entries, sorts them and re-writes it. Not used in this demonstration yet.
def sort_text_file(filename):
    try:
        # Empty list to store the lines in the file.
        m = []

        with open (filename, "r") as f:
            lines = f.readlines()
            for l in lines:
                # Writes the lines to the internal array. Strips the newline with [-1].
                m.append(l[:-1])
        with open (filename, "w") as f:
            for item in sorted(m):
                # Writes back to the same file with the newline added after each line.
                f.write(item + "\n")
    except IOError:
        print ("An error has occoured.")


# This returns a list of all files also included in sub-directories.
# The list returns the full pathname.
def get_list_of_files (source_directory):
    file_names = []
    for root, dirs, files in os.walk (source_directory):
        for file in files:
            file_name = os.path.join (root, file)
            file_names.append(file_name)
    return file_names


# This method takes in a search string, a bunch of words to look for in the string and returns the exact
# phrase in the search string that matches any words passed. So, if "blahblahblahWestworldS01E01" is passed with
# "Westworld", "Persona" as words, it will return just "Westworld". If a null object is returned, that means nothing was
# found. That is taken care of anywhere this method is called from.
def codeword (searchText, searchWords):
    start, endPos = 0,0
    searchText=searchText.upper()
    # Need to improve the code to include variation of same codes
    for word in searchWords:
        word = word.upper()
        if word in searchText:
            start = searchText.find(word)
            startPos = searchText.find(word) + len(word)
            endPos = startPos
            while ( endPos  < len(searchText)):
                # If char is NOT a digit or is NOT a '-', stop and break search searchText[endPos].isdigit() == False
                if  searchText[endPos] != '-' and searchText[endPos].isdigit() == False:
                    break
                endPos = endPos + 1

    return searchText[start:endPos]
