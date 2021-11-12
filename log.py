"""
Author : LA

Description : Log data to display on console and save them into log file if needed.
Version : Public V1

Example : 
    # Init logger
    log = Log(log_in_file=True, encoding='utf-8', filename='log.txt', filemode='a', logger_name='LOG TEST', format='%(name)s - %(asctime)s - %(levelname)s: %(message)s')
    self.logger = log.get_logger()
    
    # Use object like this :
    self.logger.info("This is a test")
"""
    

import logging, logging.handlers


class Log():


    def __init__(self, log_in_file=bool, encoding=str, filename=str, filemode=str , logger_name=str, format=str) -> None :
        """
            Function parameters : log_in_file=bool, encoding=str, filename=str, filemode=str, logger_name=str, format=str -> None
            Note when not using file for saving log : If log_in_file is False, encoding, filename and filemode can be set to None
        """
        # set format
        self.formatter = logging.Formatter(format)
        
        # Set logger name and logger level
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.INFO)
        
        if (log_in_file) : # check if user want to save log
            self.set_log_file(encoding=encoding, filename=filename, filemode=filemode)
        
        self.set_log_console() # Use to display log on console
        

    
    def set_log_file(self, encoding=str, filename=str, filemode=str) -> None:
        """
        Description : Log data into file
        Function parameters : encoding=str, filename=str, filemode=str, logger_name=str -> None
        Note : log_in_file need to be set as True to use this function
        """
        # set file to get log
        handler = logging.handlers.WatchedFileHandler(encoding=encoding,filename=filename, mode=filemode)
        # create formatter for file log
        handler.setFormatter(self.formatter)
        # add file to logger to send log to it
        self.logger.addHandler(handler)
    


    def set_log_console(self) -> None:
        """
        Description : Show log data into console
        Function parameters : self
        """
        # create console handler and set level to info
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        
        # create formatter for console
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
    


    def get_logger(self) -> object:
        """
        Description : Return logger to use in own code
        Return : logger as object
        """
        return self.logger