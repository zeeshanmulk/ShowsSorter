# author: Zeeshan Mulk
# This is a work in progress. This tool will find any files in a given directory that matches a specific show name.
# For example, if a directory contains multiple video files, it will only sort out files that has filenames such as
# "Westworld", "Persona", etc. The show names are stored in a text file called "Shows.txt". This can be manually edited
# to add more shows.


from show_finder import showFinder

# source_directory is where all the shows are currently located.
source_directory = r"d:\Hmm"
target_directory = r"d:\TV Shows"

# Create a test object with the provided directory
test = showFinder(source_directory, target_directory)

# This moves all applicable files from the source_directory to the target_directory under show names.
test.transfer_shows()





