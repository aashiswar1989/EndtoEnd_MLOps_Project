import sys

class CustomException(Exception):
    def __init__(self, error_messge, error_detail:sys):
        super().__init__()
        self.error_message = error_messge

        _,_,exc_tb = error_detail.exc_info()
        self.line_no = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename


    def __str__(self):
        return f"Error occured in file [{self.line_no}] at line no [{self.file_name}]. Error message is [{self.error_message}]"


if __name__ == "__main__":
    try:
        a = 1/0

    except Exception as e:
        raise CustomException(e, sys)