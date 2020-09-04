from db_connection import MyDB

sql = "SELECT * FROM mytest LIMIT 10"

with MyDB() as test:
    resultSet = test.query(sql)
    print(resultSet)
