# ShowsSorter

A simple tool that will take a provided directory, find list of any media files that matches a show described in a text file, 
and currently just displays them. As it evolves, it will take in another directory, create a directory with the name of the show,
and transfer any files matching the show names.

This is useful if a user downloads a bunch of different TV shows. By running this script (eventually), it should look for any shows
matching a text file with name of all shows, and copy/paste them to a different target folder.

main.py is the main file from where a show_finder object is created.
show_finder.py is the class containing various operations relevant to finding, sorting, copying shows.
my_common_functions.py is a collection of common methods for listing files, directories, checking if a string has a word in and where.
