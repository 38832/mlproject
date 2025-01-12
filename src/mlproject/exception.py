import sys
from src.mlproject.logger import logging

def error_message_detail(error_message, error_details):
    _, _, exc_tb = error_details.exc_info()  # Changed from error_detail to error_details
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name[{0}] line number [{1}] error message [{2}]".format(file_name, exc_tb.tb_lineno, error_message)
    return error_message  # Added return statement


class CustomException(Exception):
    def __init__(self, error_message, error_details):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_details)  # Corrected argument
        
    def __str__(self):
        return self.error_message
   