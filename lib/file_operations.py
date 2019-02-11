import os
from lib.logger import Logger


class FileOperations(object):

    @staticmethod
    def get_list_of_dirs(source_directory):
        for root, dirs, files in os.walk(source_directory):
            directories = []
            for each_dir in dirs:
                directories.append(each_dir)
            return directories

    @staticmethod
    def make_directory(dir_name):
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        return dir_name

    @staticmethod
    def rename_directory (source, destination):
        try:
            os.rename(source, destination)
            msg = source + " has been renamed to: " + destination
            print(msg)
            Logger.write_log(message=msg)
            return True
        except OSError as Err:
            msg = "OS error: {0}".format(Err)
            print(msg)
            Logger.write_log(message=msg)
            return False

    @staticmethod
    def get_list_of_files(source_directory):
        file_names = []
        for root, dirs, files in os.walk(source_directory):
            for file in files:
                file_name = os.path.join(root, file)
                file_names.append(file_name)
        return file_names

