from RecordID import RecordID
from PersonPlaceThingDB import PersonPlaceThingDB
from Constants import SHORT_DESCRIPTION_VALIDATION_ERROR, \
    ERROR_SAVING_RECORD, ERROR_LOADING_RECORD, NOTHING_TO_DELETE, \
    ERROR_DELETING_RECORD, RECORD_NOT_FOUND, \
    RECORD_LOADED, RECORD_SAVED, NULL_RECORD_ID, DatabaseResult
from Enums import ColumnNamesEnum


class PPTBaseItem:
    def __init__(self, table_name, data_saved_callback_func=None,
                 invalid_data_callback_func=None, record_id=None,
                 short_description=None, long_description=None, tags=None,
                 last_updated=None):
        self.__data_saved_callback_func = data_saved_callback_func
        self._invalid_data_callback_func = invalid_data_callback_func
        self._table_name = table_name
        self._record_id = RecordID(record_id).record_id
        self.short_description = short_description
        self.long_description = long_description
        self._last_updated = last_updated
        self._tags = tags
        if not self._tags:
            self._tags = list()
        elif not isinstance(self._tags, list):
            self._tags = list()

    @property
    def record_id(self):
        return self._record_id

    @property
    def tags(self):
        return self._tags

    def add_tags(self, *args):
        if not isinstance(self._tags, list):
            self._tags = list()
        for arg in args:
            if not isinstance(arg, list):
                self._tags.append(str(arg).lower())
            else:
                lower_case_tags = map(lambda x: x.lower(), arg)
                self._tags.extend(list(lower_case_tags))

    def remove_tag(self, tag):
        if not isinstance(self._tags, list):
            self._tags = list()
        else:
            if self._tags.count(tag) > 0:
                self._tags = \
                    list(filter(lambda val: val != tag,
                                self._tags))

    def _get_ppt_base_item_string(self):
        lines = []
        if self.short_description:
            lines.append(self.short_description)
        if self.long_description:
            lines.append(self.long_description)
        if len(self._tags) > 0:
            lines.append(",".join(self._tags))
        return lines

    def _init_ppt_base_item(self):
        self._record_id = None
        self._record_id = RecordID().record_id
        self.short_description = None
        self.long_description = None
        self._tags = list()
        self.error_message = None
        self._last_updated = None

    def _save_record(self, data=None):

        if not self.short_description:
            self._fire_invalid_data_callback_func(SHORT_DESCRIPTION_VALIDATION_ERROR)
            error = DatabaseResult(False, self._record_id,
                                   ERROR_SAVING_RECORD,
                                   SHORT_DESCRIPTION_VALIDATION_ERROR)
            return error

        record_data = {ColumnNamesEnum.SHORT_DESCRIPTION:
                           self.short_description,
                       ColumnNamesEnum.LONG_DESCRIPTION:
                           self.long_description,
                       ColumnNamesEnum.TAGS: self._tags}

        if data:
            for k, v in data.items():
                record_data[k] = v

        return_val = PersonPlaceThingDB().save(self._table_name,
                                               self._record_id,
                                               self._last_updated,
                                               record_data)

        if return_val.succeeded:
            # reload the base item data
            # unless this was called from PPTCalendarItem
            # which passes is the data argument
            # PPTCalendarItem will load itself after save
            if not data:
                # reload the data to get the last_updated value
                # from the DB
                self._load_ppt_base_item(return_val.record_id)
                self._fire_data_saved_callback_func(self._table_name
                                                    + ": " + RECORD_SAVED)
        elif not data:
            self._fire_invalid_data_callback_func(self._table_name
                                                  + ": " + return_val.message +
                                                  " " + return_val.error)

        return return_val

    def _delete_record(self):
        if self.record_id and self.record_id != NULL_RECORD_ID:
            return_val = \
                PersonPlaceThingDB().delete(self._table_name, self.record_id)
            if return_val.succeeded:
                self._fire_data_saved_callback_func(return_val.message)
                self._init_ppt_base_item()
            else:
                self._fire_invalid_data_callback_func(return_val.message
                                                      + " " +
                                                      return_val.error)
            return return_val
        else:
            self._fire_invalid_data_callback_func(ERROR_DELETING_RECORD
                                                  + " " +
                                                  NOTHING_TO_DELETE)
            return DatabaseResult(False, self._record_id,
                                  ERROR_DELETING_RECORD, NOTHING_TO_DELETE)

    def _load_ppt_base_item(self, record_id):
        data = PersonPlaceThingDB().read(self._table_name, {}, record_id)
        if len(data) == 1:
            self._record_id = record_id
            self.short_description = \
                data[0][ColumnNamesEnum.SHORT_DESCRIPTION]
            self.long_description = \
                data[0][ColumnNamesEnum.LONG_DESCRIPTION]
            self._tags = data[0][ColumnNamesEnum.TAGS]
            self._last_updated = data[0][ColumnNamesEnum.LAST_UPDATED]
            return DatabaseResult(True, self._record_id, RECORD_LOADED, "")
        else:
            self._fire_invalid_data_callback_func(RECORD_NOT_FOUND
                                                  + " " + self._table_name
                                                  + " " + RECORD_NOT_FOUND)
            self._init_ppt_base_item()
            return DatabaseResult(False, self._record_id,
                                  ERROR_LOADING_RECORD,
                                  self._table_name + " " +
                                  RECORD_NOT_FOUND)

    def _fire_data_saved_callback_func(self, message):
        if self.__data_saved_callback_func:
            self.__data_saved_callback_func(table_name=self._table_name,
                                            record_id=self.record_id,
                                            message=message)

    def _fire_invalid_data_callback_func(self, message):
        if self._invalid_data_callback_func:
            self._invalid_data_callback_func(table_name=self._table_name,
                                              record_id=self.record_id,
                                              message=message)


