from database.DB_connect import DBConnect
from model.contiguity import Contiguity
from model.country import Country


class DAO():

    @staticmethod
    def getAllCountry():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT *
                    FROM country
                    ORDER BY StateNme"""
        cursor.execute(query, )
        for row in cursor:
            result.append(Country(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllConnection(anno):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """SELECT *
                FROM contiguity
                WHERE year <= %s
                and state1no < state2no"""
        cursor.execute(query, (anno,))
        for row in cursor:
            result.append(Contiguity(**row))

        cursor.close()
        conn.close()
        return result