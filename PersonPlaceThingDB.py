import uuid
import psycopg2
from ManagedConnection import ManagedConnection
from RecordID import RecordID
from CustomExceptions import InvalidTableNameError, DatabaseSQLError
from CustomExceptions import ExceptionString, InvalidParametersError
from Constants import TABLE_NAME_ERROR, NO_PARAMETERS_UPDATE_ERROR, NO_PARAMETERS_INSERT_ERROR


class PersonPlaceThingDB:

    @staticmethod
    def save(table_name, record_id, data):
        if record_id != uuid.UUID(int=0):
            return PersonPlaceThingDB.update(table_name, record_id, data)
        else:
            return PersonPlaceThingDB.create(table_name, data)

    @staticmethod
    def create(table_name, data):
        if PersonPlaceThingDB.__is_table_name_valid(table_name):

            sql = PersonPlaceThingDB.__get_insert_statement(
                table_name, data)

            new_id = RecordID.get_new_record_id()

            parameter_values = \
                PersonPlaceThingDB.__get_param_values_for_save(
                    new_id, data)

            PersonPlaceThingDB.__execute_sql_statement(sql, parameter_values)

            return new_id
        else:
            raise InvalidTableNameError(TABLE_NAME_ERROR, table_name)

    @staticmethod
    def read(table_name, data, record_id=None):
        sql = PersonPlaceThingDB.__get_select_statement(table_name, data, record_id)
        if len(data) > 0:
            parameter_values = \
                PersonPlaceThingDB.__get_param_values_for_read(
                    data, record_id)
        else:
            parameter_values = None

        return PersonPlaceThingDB.__get_records(table_name, sql, parameter_values, record_id)

    @staticmethod
    def read_where_like(table_name, data):
        sql = PersonPlaceThingDB.__get_select_where_like_statement(table_name, data)
        if len(data) > 0:
            parameter_values = \
                PersonPlaceThingDB.__get_param_values_for_read_where_like(data)
        else:
            parameter_values = None

        return PersonPlaceThingDB.__get_records(table_name, sql, parameter_values)

    @staticmethod
    def update(table_name, record_id, data):
        if PersonPlaceThingDB.__is_table_name_valid(table_name):

            sql = PersonPlaceThingDB.__get_update_statement(
                table_name, data)

            parameter_values = \
                PersonPlaceThingDB.__get_param_values_for_save(
                    record_id, data, False)

            PersonPlaceThingDB.__execute_sql_statement(sql, parameter_values)

            return record_id

        else:
            raise InvalidTableNameError(TABLE_NAME_ERROR, table_name)

    @staticmethod
    def delete(table_name, record_id):
        if PersonPlaceThingDB.__is_table_name_valid(table_name):

            sql = f"DELETE FROM {table_name} WHERE id = %s;"
            # RecordID class validates for uuid, then convert to string
            record_id = str(RecordID(record_id).record_id)
            PersonPlaceThingDB.__execute_sql_statement(
                sql, (record_id,))

        else:
            raise InvalidTableNameError(TABLE_NAME_ERROR, table_name)

    @staticmethod
    def exists(table_name, record_id):
        if PersonPlaceThingDB.__is_table_name_valid(table_name):

            sql = f"SELECT id FROM {table_name} WHERE id = %s"

            with ManagedConnection.get_managed_cursor() as cur:
                try:

                    cur.execute(sql, (RecordID(record_id).record_id,))

                    for _ in cur.fetchall():
                        return True  # record exists in db

                    return False

                except psycopg2.Error as de:
                    raise DatabaseSQLError(
                        ExceptionString.get_exception_string(de))

        else:
            raise InvalidTableNameError(TABLE_NAME_ERROR, table_name)

    @staticmethod
    def __execute_sql_statement(sql, parameter_values):
        with ManagedConnection.get_managed_connection() as conn:
            try:

                cur = conn.cursor()
                cur.execute(sql, parameter_values)
                conn.commit()
                cur.close()

            except psycopg2.Error as de:
                raise DatabaseSQLError(ExceptionString.get_exception_string(de))

    @staticmethod
    def __is_table_name_valid(table_name):
        # Make sure table name is a table in the db
        with ManagedConnection.get_managed_cursor() as cur:

            cur.execute("SELECT table_name \
                        FROM information_schema.tables \
                        WHERE table_schema = 'public'")

            for t_name in cur.fetchall():
                if t_name[0] == table_name:
                    return True

        return False

    @staticmethod
    def __get_select_statement(table_name, data, record_id=None):

        select_statement = f"SELECT * FROM {table_name}"
        if record_id:
            select_statement += " WHERE id = %s;"
        else:
            if len(data) == 0:
                return select_statement
            else:
                select_statement += " WHERE "
                add_an_and = False

                for k, v in data.items():
                    if not add_an_and:
                        select_statement += k + " = %s"
                        add_an_and = True
                    else:
                        select_statement += " AND " + k + " = %s"

            select_statement += ";"
        return select_statement

    @staticmethod
    def __get_select_where_like_statement(table_name, data):

        select_statement = f"SELECT * FROM {table_name}"

        if len(data) == 0:
            return select_statement
        else:
            select_statement += " WHERE "
            add_an_and = False

            for k, v in data.items():
                if not add_an_and:
                    select_statement += k + " LIKE %s"
                    add_an_and = True
                else:
                    select_statement += " AND " + k + " LIKE %s"

            select_statement += ";"
        return select_statement

    @staticmethod
    def __get_update_statement(table_name, data):
        if len(data) == 0:
            raise InvalidParametersError(NO_PARAMETERS_UPDATE_ERROR)
        else:
            update_statement = f"UPDATE {table_name}"
            update_statement += " SET "
            add_a_comma = False

            for k, v in data.items():
                if not add_a_comma:
                    update_statement += k + " = %s"
                    add_a_comma = True
                else:
                    update_statement += ", " + k + " = %s"

        update_statement += "WHERE id = %s;"
        return update_statement

    @staticmethod
    def __get_insert_statement(table_name, data):
        if len(data) == 0:
            raise InvalidParametersError(NO_PARAMETERS_INSERT_ERROR )
        else:
            insert_statement = f"INSERT INTO {table_name} (id"
            place_holders = ""

            for k, v in data.items():
                insert_statement += ", " + k
                place_holders += ", %s"

            insert_statement += ") VALUES (%s " + place_holders + ");"

        return insert_statement

    @staticmethod
    def __get_param_values_for_read(data, record_id=None):
        param_vals = list()
        if record_id:
            param_vals.append(str(record_id))
            return tuple(param_vals)
        else:

            for k, v in data.items():
                param_vals.append(v)

            return tuple(param_vals)

    @staticmethod
    def __get_param_values_for_read_where_like(data):
        param_vals = list()

        for k, v in data.items():
            param_vals.append('%' + str(v) + '%')

        return tuple(param_vals)

    @staticmethod
    def __get_param_values_for_save(record_id, data, record_id_first=True):
        param_vals = list()

        if record_id_first:
            # append the record_id first for insert
            param_vals.append(str(record_id))

        for k, v in data.items():
            param_vals.append(v)

        if not record_id_first:
            # append the record_id on the end for update
            param_vals.append(str(record_id))

        return tuple(param_vals)

    @staticmethod
    def __get_column_names(table_name):
        sql = "SELECT column_name FROM information_schema.columns " \
              "WHERE table_schema = 'public' " \
              f"AND table_name = '{table_name}'" \
              "ORDER BY ordinal_position;"

        column_names = list()

        with ManagedConnection.get_managed_cursor() as cur:

            cur.execute(sql)

            for column_name_tuple in cur.fetchall():
                column_names.append(column_name_tuple[0])

        return column_names

    @staticmethod
    def __get_records(table_name, sql, parameter_values=None, record_id=None):
        if PersonPlaceThingDB.__is_table_name_valid(table_name):

            column_names_list = \
                PersonPlaceThingDB.__get_column_names(table_name)

            with ManagedConnection.get_managed_cursor() as cur:
                try:
                    if not parameter_values and not record_id:
                        cur.execute(sql)
                    else:
                        cur.execute(sql, parameter_values)

                    result_list = list()

                    for row in cur.fetchall():
                        row_dict = dict()
                        for col in range(len(column_names_list)):
                            row_dict[column_names_list[col]] = row[col]
                        result_list.append(row_dict)

                    # this returns a list of dictionaries
                    # each dictionary containing a row's data
                    return result_list

                except psycopg2.Error as de:
                    raise DatabaseSQLError(
                        ExceptionString.get_exception_string(de))
        else:
            raise InvalidTableNameError(TABLE_NAME_ERROR, table_name)

