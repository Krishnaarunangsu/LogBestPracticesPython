import pyodbc


class MyDB(object):

    def __init__(self):
        """
        Initializes the Database Connection and the Database cursor
        """
        self._db_connection = pyodbc.connect('host', 'user', 'password', 'db')
        self._db_cur = self._db_connection.cursor()

    def query(self, query: object, params: object) -> object:
        """
        Args:
            :param query:
            :param params:

        Returns:
            :return: result:
        """
        try:
            result = self._db_cur.execute(query,params)
        except Exception as error:
            print('error executing query "{}", error: {}'.format(query, error))
            return None
        else:
            return result
        # return self._db_cur.execute(query, params)

    def __del__(self):
        """
        Closes the Database Connection and the Database cursor
        :return:
        """
        self._db_cur.close()
        self._db_connection.close()


#Sample SQL
sql = "SELECT * FROM mytest LIMIT 10"

with MyDB() as test:
    resultSet = test.query(sql)
    print(resultSet)
