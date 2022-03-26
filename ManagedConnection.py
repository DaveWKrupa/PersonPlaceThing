import psycopg2
from contextlib import contextmanager
from Configuration import Configuration
from CustomExceptions import DatabaseConnectionError, ExceptionString


class ManagedConnection:
    @staticmethod
    @contextmanager
    def get_managed_connection():
        conn = None
        try:
            # read connection parameters using Configuration class
            params = Configuration.config(filename='database.ini',
                                          section='postgresql')

            # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            yield conn
        except psycopg2.Error as e:
            raise DatabaseConnectionError(
                ExceptionString.get_exception_string(e))
        finally:
            if conn is not None:
                conn.close()

    @staticmethod
    @contextmanager
    def get_managed_cursor():
        conn = None
        try:
            # read connection parameters using Configuration class
            params = Configuration.config(
                filename='database.ini', section='postgresql')

            # connect to the PostgreSQL server
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            yield cur
        except psycopg2.Error as e:
            raise DatabaseConnectionError(
                ExceptionString.get_exception_string(e))
        finally:
            if cur is not None:
                cur.close()
            if conn is not None:
                conn.close()
