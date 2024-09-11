import sqlite3

class DBManager:
    def __init__(self, db_name, db_connector) -> None:
        self.db_name = db_name
        self.db_connector = db_connector
        # self.conn = sqlite3.connect('./owm.db')
        # self.cursor = self.conn.cursor()

    # def create_table
    # with conn:
    #     cursor.execute(
    #         "DROP TABLE IF EXISTS CityWeather;")

    #     cursor.execute(
    #         "CREATE TABLE CityWeather( \
    #             city TEXT, \
    #             temperature_C REAL, \
    #             humidity INTEGER, \
    #             description_de TEXT, \
    #             description_en TEXT);"
    #         )
