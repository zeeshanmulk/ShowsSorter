import pytest
from lib.logger import Logger


class TestLogger(object):

    def test_initialize_no_params(self):
        Logger.initialize()
        assert (Logger.log_filename == 'log.txt')
        assert (Logger.log_success == True)

    def test_initialize_params(self):
        file_name = "Temp.txt"
        Logger.initialize(log_filename=file_name)
        assert (Logger.log_filename == file_name)
        assert (Logger.log_success == True)

