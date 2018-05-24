# ShowsSorter

A simple tool that looks for known TV shows in a given directory and moves it to a destination directory. For example, if a download folder
"Download" contains multiple episodes of a tv show like McGyver, Westworld, etc, the algorithm will initially create a list of applicable
files, and move them to a destination directory, create the show name and place all files in there. So, all episodes of McGyver should go under //McGyver/McGyverS01E01.mkv for example.

This is quite useful when a user downloads a vast amount of different TV shows and wishes to sort them into folders. Instead of manual copy paste, this does it fairly quickly.

"shows.txt" has the list of shows. The user can edit and add them. The parser will automatically remove the '\n' when reading.
"log.txt" creates a log of all IO operations as well as the number of files moved. A log file can be provided optionally; if not the program will generate one.
main.py is the main file from where a show_finder object is created and tasked. The method transfer_shows will do the magic.
show_finder.py is the class containing various operations relevant to finding, sorting, copying shows.
my_common_functions.py is a collection of common methods for listing files, creating directories, renaming files, checking if a string has a word in and where.

The current limitation of this code is that it can only match the name of the show if it exists in the filename. If there are creative variations of the show name in the filename, it won't catch it. For example, if Westworld is written with a zero instead of the letter O, it will not catch it.
