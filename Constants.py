import collections
import uuid

DatabaseResult = collections.namedtuple('DatabaseResult', ['succeeded', 'record_id', 'message', 'error'])

NULL_RECORD_ID = uuid.UUID(int=0)

TABLE_NAME_ERROR = "The table name passed in does not exist in the database."
PHONE_FORMAT_ERROR = "Phone numbers can contain only numbers, dashes, dots and spaces."
ZIP_CODE_FORMAT_ERROR = "ZipCodes can only contain numbers and dashes."
PERSON_NAME_VALIDATION_ERROR = "First name and last name required."
SHORT_DESCRIPTION_VALIDATION_ERROR = "Short description is required."
NO_PARAMETERS_UPDATE_ERROR = "No parameters found for update statement."
NO_PARAMETERS_INSERT_ERROR = "No parameters found for insert statement."
RECORD_NOT_FOUND = "Record not found"
NOTHING_TO_DELETE = "Nothing to delete"
ERROR_SAVING_RECORD = "Error saving record"
ERROR_LOADING_RECORD = "Error loading record"
RECORD_SAVED = "Record saved"
RECORD_LOADED = "Record loaded"
RECORD_DELETED = "Record deleted"
ERROR_DELETING_RECORD = "Error deleting record"


YYYY_MM_DD = "YYYY-MM-DD"
YYYY_MM_DD_FORMAT = "%Y-%m-%d"
HH_MM_SS = "HH:MM:SS-ZZ:ZZ"
HH_MM_SS_FORMAT = "%H:%M:%S%z"
YYYY_MM_DD_HH_MM_SS_FORMAT = "%Y-%m-%d %H:%M:%S%z"
YYYY_MM_DD_HH_MM_SS = "YYYY-MM-DD HH:MM:SS-ZZ:ZZ"






