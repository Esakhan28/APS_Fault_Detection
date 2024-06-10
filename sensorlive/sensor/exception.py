import sys
import os 


def error_message_detail(error, error_detail:sys):
    
    _,_,exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename

    error_message="error occured and the file name is [{0}] and the linenumber is [{1}]and error is [{2}]".format(
    filename,exc_tb.tb_lineno,str(error))
    
    return error_message



class SensorException(Exception):
    
    def __init__(self,error_message,error_detail:sys):

        super().__init__(error_message)


     
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
        
    def __str__(self):
        return  self.error_message