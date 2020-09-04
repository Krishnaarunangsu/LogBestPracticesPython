from typing import Any, Union, Tuple
import database_connection_helper_abzooba_customer
from database_connection_helper_abzooba_customer import DatabaseConnectionHelper
from db_select_data import DatabaseSelect
import db_configuration

# Input data for Query
max: int = 50
min: int = 10

# Form the tuple from Input data
data: Tuple[int, int] = (max, min)


# Open Database Connection, get the data & Close the connection
db_conn_helper: Union[DatabaseConnectionHelper, Any]
with DatabaseConnectionHelper() as db_conn_helper:
    # db_cursor = db_conn_helper.__enter__
    print(f'Here:{db_conn_helper}')
    #db_select: Union[DatabaseSelect, Any]
    #with DatabaseSelect(db_conn_helper) as db_select:
        #result_set = db_select.get_row(db_configuration.prepared_statement, data)
        #print(result_set)

    # Close the Database Connection
    # db_conn_helper.__exit__()
