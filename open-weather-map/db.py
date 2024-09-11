import sqlite3

def create_owm_db():
    conn = sqlite3.connect('./owm.db')
    cursor = conn.cursor()

    with conn:
        cursor.execute(
            "DROP TABLE IF EXISTS CityWeather;")

        cursor.execute(
            "CREATE TABLE CityWeather( \
                city TEXT, \
                temperature_C REAL, \
                humidity INTEGER, \
                description_de TEXT, \
                description_en TEXT);"
            )
