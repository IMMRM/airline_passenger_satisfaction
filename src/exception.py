import sys
import logging
from src.logger import logging


def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    filename=exc_tb.tb_frame.f_code.co_filename
    line_num=exc_tb.tb_lineno
    error_message="Error occurred in python script name [{0}] at Line Number [{1}] with Error message: [{2}]".format(filename,line_num,error)
    
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
'''
if(__name__=="__main__"):
    try:
        a=1/0
    except Exception as e:
        logging.info("Division by zero")
        raise CustomException(e,sys)'''
        
        