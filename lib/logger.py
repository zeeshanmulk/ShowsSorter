import logging


class Logger(object):

    log_filename = 'log.txt'
    log_success = False

    @staticmethod
    def initialize(log_filename=None):
        if log_filename is not None:
            Logger.log_filename = log_filename

        try:
            logging.basicConfig(filename=Logger.log_filename,
                                level=logging.INFO,
                                format='%(asctime)s %(message)s',
                                datefmt='%m/%d/%Y %I:%M:%S %p')
            Logger.log_success = True
        except IOError as Err:
            print("OS error: {0}".format(Err))

    @staticmethod
    def write_log(message):
        if Logger.log_success:
            logging.info(message)
