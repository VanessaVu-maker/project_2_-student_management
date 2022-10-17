from DTO import SubjectDTO
from .dbprovider import DBProvider


class SubjectDAL:
    def __init__(self):
        #Khoi tao object DBProvider de giao tiep voi Database gian tiep thong qua DBProvdider
        self.__dbProvider = DBProvider()
        self.__createTableIfNotExists()

    def __createTableIfNotExists(self):
        try:
            sql = '''
                CREATE TABLE IF NOT EXISTS Subjects (
                    `Code` VARCHAR(5),
                    `Name` NVARCHAR(50) NOT NULL UNIQUE,
                    PRIMARY KEY (Code)
                );
            '''
        except Exception as err:
            print(err)
        self.__dbProvider.exec(sql)

    #Them 
    def insert(self, sub: SubjectDTO):
        try:
            sql = '''
                INSERT INTO Subjects(Code, Name)
                VALUES (%s, %s)
            '''
            params = (sub.Code, sub.Name)
        except Exception as err:
            print(err)
        return self.__dbProvider.exec(sql, params)
    
    #Sua
    def update(self, sub: SubjectDTO):
        try:
            sql = '''
                UPDATE Subjects 
                SET 
                    Name = %s
                WHERE Code = %s
            '''
            params = (sub.Name, sub.Code)
        except Exception as err:
            print(err)
        return self.__dbProvider.exec(sql, params)

    #Xoa
    def delete(self, code:str): #khi xoa thi chi can code nen k can truyen vao SubjectDTO
        try:
            sql = '''
                DELETE 
                FROM Subjects
                WHERE Code = %s
            '''
            params = (code,) #can phai co dau , de dinh nghia tuple co mot phan tu (vi chi co 1 %s)
        except Exception as err:
            print(err)
        return self.__dbProvider.exec(sql, params)
    
    #Lay tat ca ban ghi 
    def get(self):
        try:
            sql = 'SELECT * FROM Subjects'
            subs = self.__dbProvider.get(sql)
            subDtos = list(map(lambda sub: SubjectDTO(sub[0], sub[1]), subs))
        except Exception as err:
            print(err)
        return subDtos

    #Lay mot ban ghi theo Code
    def getByCode(self, code: str):
        try:
            sql = '''
                SELECT * FROM Subjects
                WHERE Code = %s
            '''
            params = (code, )
            sub = self.__dbProvider.getOne(sql, params)
            # Chuyen tuple sang StudentDTO
            subDto = SubjectDTO (sub[0], sub[1]) if sub is not None else None
        except Exception as err:
            print(err)
        return subDto
        
    # Tim kiem
    def search(self, text: str):
        try:
            sql = '''
                SELECT * FROM Subjects
                WHERE Code = %s
                    OR Name LIKE %s
            '''
            params=(text, f'%{text}%')
            subs = self.__dbProvider.get(sql, params) #tim kiem co the ra nhieu ket qua nen chon get 
            subDtos = list(map(lambda sub: SubjectDTO(sub[0], sub[1]), subs))
        except Exception as err:
            print(err)
        return subDtos
    
    #Kiem tra ma mon hoc ton tai
    def checkExists(self, code: str):
        try:
            sql = '''
                SELECT  * FROM Subjects
                WHERE Code = %s
            '''
            params = (code,)
            sub = self.__dbProvider.getOne(sql, params)
        except Exception as err:
            print(err)
        return sub is not None #return True neu co ton tai, False neu khong ton tai

    #Kiem tra ten mon hoc ton tai
    def checkExistsName(self, name: str):

        try:
            sql = '''
                SELECT  * FROM Subjects
                WHERE Name = %s
            '''
            params = (name,)
            sub = self.__dbProvider.getOne(sql, params)
        except Exception as err:
            print(err)
        return sub is not None #return True neu co ton tai, False neu khong ton tai
    
