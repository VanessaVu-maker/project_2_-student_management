import mysql.connector

class DBProvider:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.passwd = 'vuthanhvanvuthanhvan27072017'
        self.db = 'big02db'
        self.conn = None
        self.cur = None
        # Khoi tao object DBProvider se tao Database neu chua ton tai
        self.__createDBIfNotExist()

    # Tao Database neu chua ton tai
    def __createDBIfNotExist(self):
        try:
            sql = f'CREATE DATABASE IF NOT EXISTS {self.db};'
            conn = mysql.connector.connect (host=self.host,
                                            user=self.user, 
                                            passwd = self.passwd) # bat o day vi co connect
            cur = conn.cursor()
            cur.execute(sql)
        except Exception as err:
            print(err)
        finally:
            conn.close()

    # Ket noi toi MySQL Database
    def connect(self):
        try:
            self.conn = mysql.connector.connect(host=self.host,
                                                user=self.user, 
                                                passwd = self.passwd, 
                                                db=self.db) # bat o day vi co connect

            self.cur = self.conn.cursor()
        except Exception as err:
            print(err)
    
    # Dong ket noi toi database
    def close(self):
        # Neu dang ket noi thi moi dong ket noi
        if self.conn is not None and self.cur is not None:
            self.conn.close()
            self.conn = None
            self.cur = None

    # Thuc thi cau lenh SQL o dang chinh sua du lieu: INSERT, UPDATE, DELETE
    def exec(self, sql: str, *params):
        rowCount = 0 #de trong truong hop loi, return rowCount ve se bang 0
        try:
            self.connect()

            self.cur.execute(sql, *params) #param that bai: sql ko dung cu phap, constrainst, primakey key
            self.conn.commit()
            rowCount = self.cur.rowcount 
        except Exception as err: # co the chia ra nhieu loai loi, nhieu loai except
            print(err)
        finally: #trong bat cu truong hop nao deu can phai dong ket noi, vi vay cho vao block finally
            self.close()
        return rowCount #dam bao return kbh xay ra ngoai le

    # Thuc thi cau lenh SQL o dang truy van du lieu: SELECT
    # Truy van nhieu ban ghi
    def get(self, sql: str, *params):
        res = []
        try:
            self.connect()

            self.cur.execute(sql, *params) # co the co loi
            res = [row for row in self.cur.fetchall()]
        except Exception as err:
            print(err)
        finally:
            self.close()
        return res

    # Truy van nhieu ban ghi
    def getOne(self, sql: str, *params):
        res = None
        try:
            self.connect()

            self.cur.execute(sql, *params) #co the co loi
            res = self.cur.fetchone()
        except Exception as err:
            print(err)
        finally:
            self.close()
        return res

