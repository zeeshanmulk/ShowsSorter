# author Zeeshan MUlk
# This Python file contains a showFinder class.
# This file make uses of my own functions which are imported as myFunc

import my_common_functions as myFunc
import logging

class showFinder():

    # Initializes a bunch of variables.
    _default_log_file = "log.txt"
    _shows_filename = "shows.txt"
    _shows = ["Westworld"]
    _shows_initialized = False
    _extensions = ["mp4", "avi", "mpg", "mkv", "wmv", "flv"]

    # This constructor takes in the directory name as a string and does the following:
    # It formats the source directory correctly. Strips any "/" or "\\" and adds "/".
    # It formats the target directory correctly. Strips any "/" or "\\" and adds "/".
    # It initialises a log file. If no log file path is provided, a default "log.txt" is used.
    # It imports the name of the shows from the file "shows.txt". If it doesn't exist, uses the global variable.
    # It generates list of all the files in the provided directory and its subdirectories.
    # Finally, it generates a list of common media files with the extensions provided.
    def __init__(self, directory_name, target_directory, log_file = _default_log_file):
        self._directory_name = self._initialize_directory(directory_name)
        self._target_directory = self._initialize_directory(target_directory)
        self._initilize_log_file(log_file)
        self._initialize_shows()
        self._all_file_names = myFunc.get_list_of_files(self._directory_name)
        self._eligible_files = self._initialize_eligible_files(self._all_file_names)

    # Strips any slashes or backwards slashes and finally adds in a "/" so all directories should end with "/"
    def _initialize_directory(self, directory_name):
        temp = directory_name.rstrip("/")
        temp = temp.rstrip("\\")
        return temp + "/"

    # Just initializes the log file.
    def _initilize_log_file(self, log_file):
        if log_file == None:
            logging.basicConfig(filename=self._default_logfile, level=logging.INFO, format='%(asctime)s %(message)s',
                                datefmt='%m/%d/%Y %I:%M:%S %p')
        else:
            try:
                logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s %(message)s',
                                    datefmt='%m/%d/%Y %I:%M:%S %p')
            except IOError as Err:
                print ("OS error: {0}".format(Err))
                print ("Creating default log {0}".format(self._default_logfile))
                logging.basicConfig(filename=self._default_logfile, level=logging.INFO, format='%(asctime)s %(message)s',
                                    datefmt='%m/%d/%Y %I:%M:%S %p')

    # Returns the current directory name if called as an object.
    def __str__(self):
        return self._directory_name

    # Opens the "shows.txt" filename and adds it to an internal list called _shows.
    # If there is an error, a _shows with some show names are provided above.
    def _initialize_shows(self):
        try:
            with open (self._shows_filename, "r") as f:
                lines = f.readlines()
                for line in lines:
                    # This get rids of the newline operator.
                    line = line.strip()
                    self._shows.append(line)
                print ("Codes loaded successfully")
                self._shows_initlaized = True
        except IOError:
            print("An error has occured")

    # This iterates through the list of files in the target directory and returns a list that contains
    # common media extensions that is already defined above. Then if the showname matches, it adds it to an internal list.
    # The filename is split using a "." and [-1], that returns the extension from the string. This is used to match
    # the list of extensions.
    def _initialize_eligible_files(self, list_of_files):
        e_files = []
        for ext in self._extensions:
            for file in list_of_files:
                # Checks if the extension matches.
                if file.split('.')[-1] == ext:
                    if myFunc.codeword(file, self._shows):
                        e_files.append(file)

        return e_files

    # Returns the name of shows that is obtained from the "shows.txt" file.
    def get_name_of_shows(self):
        return self._shows

    # Returns a list of eligible media files that can be actioned upon.
    def list_all_files(self):
        for file in self._eligible_files:
            print (file)

    # Transfer the shows from the destination folder to the target folder.
    # The logic is simple. First it goes through all the eligible files in the list. Then it checks if the show name is present
    # in the filename. If so, it creates a new string of what the final path of the file can be like.
    # First, it creates the show name in the target folder, and if that is a success,
    # The file will be renamed from actual disk location to target disk location.
    # A break is added to ensure that the same file is not processed again.
    # This also tracks how many files were process and its printed to the user.
    def transfer_shows(self):
        files_moved = 0
        for file_with_path in self._eligible_files:
            for show in self._shows:
                if show in file_with_path:
                    # Determines the target show directory and filename
                    target_show_directory = self._target_directory + show
                    filename = file_with_path.split('/')[-1]
                    target_show_with_filename = target_show_directory + "/" + filename

                    # Creates the directory and renames the source file to target file
                    if (myFunc.make_directory(target_show_directory)):
                        myFunc.rename_directory(file_with_path, target_show_with_filename)
                        files_moved += 1
                        # The break ensures that the same file is not processed again with the current show.
                        break


        msg = "Total files moved: " + str(files_moved)
        print (msg)
        logging.info((msg))





