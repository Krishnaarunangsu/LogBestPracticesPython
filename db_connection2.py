import pyodbc

# Using ContextManager Design
class DatabaseTest(object):
    def __init__(self, db_local):
        self.db_local = db_local
        self.db_conn = None
        self.db_cursor = None
        self.resultset = None

    def __enter__(self):
        # This ensure, whenever an object is created using "with"
        # this magic method is called, where you can create the connection.
        self.db_conn = pyodbc.connect(**self.db_local)
        self.db_cursor = self.db_conn.cursor()

    def __exit__(self, exception_type: object, exception_val: object, trace: object) -> object:
        """

        :rtype:
        """
        # once the with block is over, the __exit__ method would be called
        # with that, you close the connection
        try:
           self.db_cursor.close()
           self.db_conn.close()
        except AttributeError: # isn't closable
           print('Not closeable.')
           return True # exception handled successfully

    def get_row(self, sql: object, data: object = None) -> object:
        self.db_cursor.execute(sql)
        self.resultset = self.db_cursor.fetchall()
        return self.resultset

db_config =  {
            'host':"127.0.0.1",                 # database host
            'port': 3306,                       # port
            'user':"root",                      # username
            'password':"admin",                   # password
            'db':"test",                        # database
            'charset':'utf8'                    # charset encoding
            }


sql = "SELECT * FROM mytest LIMIT 10"

with DatabaseTest(db_config) as test:
    resultSet = test.get_row(sql)
    print(resultSet)
