# from memory_profiler import profile
import numpy as np
import pandas as pd
import pyodbc


class DbAccessor:

    # @profile
    def __init__(self, instance, dbname, user, password):
        print("start:__init__")
        connection = "DRIVER={SQL Server};SERVER=" + instance + ";uid=" + user + \
                     ";pwd=" + password + ";DATABASE=" + dbname
        try:
            self.conn = pyodbc.connect(connection, autocommit=False)
        except pyodbc.Error as e:
            print("error:__init__")
            print(e)

        print("end:__init__")

    # @profile
    def query_df(self, sql, parameters):
        print("start:query")

        try:
            cursor = self.conn.cursor()

            if parameters is None:
                cursor.execute(sql)
            else:
                cursor.execute(sql, parameters)

            rows = cursor.fetchall()
            df = pd.DataFrame(np.array(rows))
            cursor.close()

        except AttributeError as e:
            print("error:query")
            print(e)
            df = None

        except pyodbc.Error as e:
            print("error:query")
            print(e)
            df = None

        return df

    # @profile
    def execute(self, sql, parameters):
        try:
            cursor = self.conn.cursor()

            if parameters is None:
                cursor.execute(sql)
            else:
                cursor.execute(sql, parameters)

            rowcount = cursor.rowcount
            cursor.close()

        except AttributeError as e:
            print("error:query")
            print(e)
            rowcount = -1
            self.conn.rollback()

        except pyodbc.Error as e:
            print("error:query")
            print(e)
            rowcount = -1
            self.conn.rollback()

        finally:
            self.conn.commit()

        return rowcount

    def __del__(self):
        print("start:__del__")

        try:
            self.conn.close()

        except AttributeError as e:
            print("error:__del__")
            print(e)

        print("end:__del__")
