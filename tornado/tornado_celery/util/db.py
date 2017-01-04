# coding:utf-8
import psycopg2


class DB():

    def __init__(self, DB_HOST, DB_PORT, DB_USER, DB_PWD, DB_NAME):
        self.DB_HOST = DB_HOST
        self.DB_PORT = DB_PORT
        self.DB_USER = DB_USER
        self.DB_PWD = DB_PWD
        self.DB_NAME = DB_NAME

        self.conn = self.getConnection()

    def getConnection(self):
        return psycopg2.connect(
            host=self.DB_HOST,
            port=self.DB_PORT,
            user=self.DB_HOST,
            password=self.DB_PWD
        )

    def query(self, sqlString):
        cursor = self.conn.cursor()
        cursor.execute(sqlString)
        result = cursor.dictfetchall()
        cursor.close()
        self.conn.close()
        return result

    def update(self, sqlString):
        cursor = self.conn.cursor()
        cursor.execute(sqlString)
        self.conn.commit()
        cursor.close()
        self.conn.close()
        return True
