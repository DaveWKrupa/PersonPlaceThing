import uuid
from CustomExceptions import InvalidRecordIDError


class RecordID:
    def __init__(self, record_id=None):
        self.__record_id = None
        self.record_id = record_id

    @property
    def record_id(self):
        return self.__record_id if self.__record_id is not None else uuid.UUID(int=0)

    @record_id.setter
    def record_id(self, value):
        if value is not None:
            if self.__is_valid_uuid(value):
                self.__record_id = value
            else:
                raise InvalidRecordIDError("Record ID must be in uuid format.")

    @staticmethod
    def get_new_record_id():
        return uuid.uuid4()

    @staticmethod
    def __is_valid_uuid(value):
        try:
            uuid.UUID(str(value))
            return True
        except ValueError:
            return False




