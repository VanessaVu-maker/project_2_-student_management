from DTO import StudentDTO
from .dbprovider import DBProvider


class StudentDAL:
    def __init__(self):
        #Khoi tao object DBProvider de giao tiep voi Database gian tiep thong qua DBProvdider
        self.__dbProvider = DBProvider()
        self.__createTableIfNotExists()

    def __createTableIfNotExists(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS Students(
                Code VARCHAR(6) PRIMARY KEY,
                FullName NVARCHAR(50),
                Birthday VARCHAR(20),
                Sex TINYINT(1),
                Address NVARCHAR(500),
                Phone VARCHAR(20),
                Email VARCHAR(250)
            );
        '''
        self.__dbProvider.exec(sql)

    #Them 
    def insert(self, st: StudentDTO):
        rowCount = 0
        try: 
            sql = '''
                INSERT INTO Students(Code, FullName, Birthday, Sex, Address, Phone, Email)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            '''
            params = (st.Code, st.FullName, st.Birthday, st.Sex, st.Address, st.Phone, st.Email)
            rowCount = self.__dbProvider.exec(sql, params)
        except Exception as err:
            print(err)
        return rowCount
    
    #Sua
    def update(self, st: StudentDTO):
        rowCount = 0
        try:
            sql = '''
                UPDATE Students 
                SET 
                    FullName = %s,
                    Birthday = %s,
                    Sex = %s,
                    Address = %s,
                    Phone = %s,
                    Email = %s
                WHERE Code = %s
            '''
            params = (st.FullName, st.Birthday, st.Sex, st.Address, st.Phone, st.Email, st.Code)
            rowCount = self.__dbProvider.exec(sql, params)
        except Exception as err:
            print(err)
        return rowCount

    #Xoa
    def delete(self, code:str): #khi xoa thi chi can code nen k can truyen vao StudentDTO
        rowCount = 0
        try:
            sql = '''
                DELETE 
                FROM Students
                WHERE Code = %s
            '''
            params = (code,) #can phai co dau , de dinh nghia tuple co mot phan tu (vi chi co 1 %s)
            rowCount = self.__dbProvider.exec(sql, params)
        except Exception as err:
            print(err)
        return rowCount
    
    #Lay tat ca ban ghi 
    def get(self):
        stDtos = []
        try:
            sql = 'SELECT * FROM Students'
            sts = self.__dbProvider.get(sql)
            stDtos = list(map(lambda st: StudentDTO(st[0], 
                                                    st[1], 
                                                    st[2], 
                                                    st[3], 
                                                    st[4], 
                                                    st[5], 
                                                    st[6]),
                            sts))
        except Exception as err:
            print(err)
        return stDtos

    #Lay mot ban ghi theo Code
    def getByCode(self, code: str):
        stDto = None
        try:
            sql = '''
                SELECT * FROM Students
                WHERE Code = %s
            '''
            params = (code, )
            st = self.__dbProvider.getOne(sql, params)
            # Chuyen tuple sang StudentDTO
            stDto = StudentDTO (st[0],
                            st[1], 
                            st[2], 
                            st[3], 
                            st[4], 
                            st[5], 
                            st[6]) if st is not None else None
        except Exception as err:
            print(err)
        return stDto
        
    def search(self, text: str):
        stDtos = []
        try:
            sql = '''
                SELECT * FROM Students
                WHERE Code = %s
                    OR FullName LIKE %s
                    OR Email LIKE %s
            '''
            params=(text, f'%{text}%', f'%{text}%')
            sts = self.__dbProvider.get(sql, params) #tim kiem co the ra nhieu ket qua nen chon get 
            stDtos = list(map(lambda st: StudentDTO(st[0], 
                                                    st[1], 
                                                    st[2], 
                                                    st[3], 
                                                    st[4], 
                                                    st[5], 
                                                    st[6]),
                            sts))
        except Exception as err:
            print(err)
        return stDtos
    
    #Kiem tra ma ton tai
    def checkExists(self, code: str):
        st = None
        try:
            sql = '''
                SELECT  * FROM Students
                WHERE Code = %s
            '''
            params = (code,)
            st = self.__dbProvider.getOne(sql, params)
        except Exception as err:
            print(err)
        return st is not None #return True neu co ton tai, False neu khong ton tai

#Kich ban test
import unittest
class StudentDALTest(unittest.TestCase):
    def setUp(self):
        self.__stDAL = StudentDAL()
    
    def testCheckExistIsTrue(self):
        #Arrange
        st = StudentDTO('PY9999', 'Test', '01/01/2000', 1, 'Test', '1234567890', 'test@test.com')
        self.__stDAL.insert(st)
        expectedResult = True

        #Act
        actualResult = self.__stDAL.checkExists(st.Code)

        #Assert
        self.assertEqual(expectedResult, actualResult)

        #Teardown for this test case
        self.__stDAL.delete(st.Code)
    
    def testGetByCodeIsNone(self):

        #Arrange
        codeNotExists = 'PY9999' #Day la ma khong ton tai torn DTB
        expectedResult = None

        #Act
        actualResult = self.__stDAL.getByCode(codeNotExists)

        #Assert
        self.assertEqual(expectedResult, actualResult)

    def testGetByCodeIsNotNone(self):

        #Arrange
        st = StudentDTO('PY9999', 'Test', '01/01/2000', 1, 'Test', '1234567890', 'test@test.com')
        self.__stDAL.insert(st)
        expectedResult = st

        #Act
        actualResult = self.__stDAL.getByCode(st.Code)

        #Assert
        self.assertEqual(expectedResult.Code, actualResult.Code) #khi ma so sanh 2 class, no k the bang nhau duoc mac du co nhung thuoc tinh nhu nhau, vi vay phai tach ra tung cai mot)
        self.assertEqual(expectedResult.FullName, actualResult.FullName)
        self.assertEqual(expectedResult.BirthDay, actualResult.BirthDay)
        self.assertEqual(expectedResult.Sex, actualResult.Sex)
        self.assertEqual(expectedResult.Address, actualResult.Address)
        self.assertEqual(expectedResult.Phone, actualResult.Phone)
        self.assertEqual(expectedResult.Email, actualResult.Email)

        #Teardown for this test case
        self.__stDAL.delete(st.Code)
    # TODO
        
    def tearDown(self):
        pass