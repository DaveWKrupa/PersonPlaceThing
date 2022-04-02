import sys


class ExceptionString:
    @staticmethod
    def get_exception_string(err):
        # get details about the exception
        err_type, err_obj, traceback = sys.exc_info()

        # get the line number when exception occurred
        line_num = traceback.tb_lineno
        return f"ERROR: {err}"


class InvalidTableNameError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


class InvalidParametersError(Exception):
    def __init__(self, message):
        self.message = message


class DatabaseConnectionError(Exception):
    def __init__(self, message):
        self.message = message


class DatabaseSQLError(Exception):
    def __init__(self, message):
        self.message = message


class InvalidRecordIDError(Exception):
    def __init__(self, message):
        self.message = message






