class DatabaseSelect(object):

    def __init__(self, db_cursor):
        """
        Initializes the class
        :param db_cursor:
        :return
        """
        self.db_cursor = db_cursor
        self.result_set = None
        print(db_cursor)

    def __enter__(self):
        """

        :return:
        """

    def get_row(self, sql: object, data: object = None) -> object:
        """
        Get Data from Database

        :type data: object
        :return:
        :param sql:
        :param data:
        :return:
        """
        self.db_cursor.execute(sql, data)
        self.result_set = self.db_cursor.fetchall()
        return self.result_set

    def __exit__(self, exception_type: object, exception_val: object, trace: object) -> object:
        """
        Once the with block is over, the __exit__ method would be called
        with that, you close the connection

        :rtype: object
        :param exception_type:
        :param exception_val:
        :param trace:
        :return:
        """
        try:
           self.db_cursor.close()
           # self.db_conn.close()
        except AttributeError: # isn't closable
           print('Not closeable.')
           return True # exception handled successfully
