from DTO import ScoreDTO, TotalDTO
from .dbprovider import DBProvider


class ScoreDAL:
    def __init__(self):
        #Khoi tao object DBProvider de giao tiep voi Database gian tiep thong qua DBProvdider
        self.__dbProvider = DBProvider()
        self.__createTableIfNotExists()

    def __createTableIfNotExists(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS Scores (
                StudentCode VARCHAR(6) NOT NULL,
                SubjectCode VARCHAR(5) NOT NULL,
                ProcessScore FLOAT NOT NULL,
                FinalTestScore FLOAT NOT NULL,
                PRIMARY KEY (StudentCode, SubjectCode),
                FOREIGN KEY (StudentCode) REFERENCES Students (Code) ON DELETE CASCADE ON UPDATE CASCADE,
                FOREIGN KEY (SubjectCode) REFERENCES Subjects (Code) ON DELETE CASCADE ON UPDATE CASCADE
            );
        '''
        self.__dbProvider.exec(sql)

    #Them 
    def insert(self, sc: ScoreDTO):
        rowCount = 0
        try: 
            sql = '''
                INSERT INTO Scores (StudentCode, SubjectCode, ProcessScore, FinalTestScore)
                VALUES (%s, %s, %s, %s)
            '''
            params = (sc.StudentCode, sc.SubjectCode, sc.ProcessScore, sc.FinalTestScore)
            rowCount = self.__dbProvider.exec(sql, params)
        except Exception as err:
            print(err)
        return rowCount
    
    #Sua
    def update(self, sc: ScoreDTO):
        rowCount =0 
        try:
            sql = '''
                UPDATE Scores
                SET 
                    ProcessScore = %s,
                    FinalTestScore = %s
                WHERE StudentCode = %s AND SubjectCode = %s
            '''
            params = (sc.ProcessScore, sc.FinalTestScore, sc.StudentCode, sc.SubjectCode)
            rowCount = self.__dbProvider.exec(sql, params)
        except Exception as err:
            print(err)
        return rowCount

    #Xoa
    def delete(self, studentCode: str, subjectCode: str): 
        rowCount = 0
        try:
            sql = '''
                DELETE 
                FROM Scores
                WHERE StudentCode = %s AND SubjectCode = %s
            '''
            params = (studentCode, subjectCode)
            rowCount = self.__dbProvider.exec(sql, params)
        except Exception as err:
            print(err)
        return rowCount

    #Lay tat ca ban ghi 
    def get(self):
        scDtos = []
        try:
            sql = 'SELECT * FROM Scores'
            scs = self.__dbProvider.get(sql)
            scDtos = list(map(lambda sc: ScoreDTO(sc[0], 
                                                    sc[1], 
                                                    sc[2], 
                                                    sc[3]), 
                            scs))
        except Exception as err:
            print(err)
        return scDtos 

    #Lay mot ban ghi theo StudentCode and Subject Code
    def getByCode(self, studentCode: str, subjectCode: str):
        scDto = None
        try: 
            sql = '''
                SELECT * FROM Scores
                WHERE StudentCode = %s and SubjectCode = %s
            '''
            params = (studentCode, subjectCode )
            sc = self.__dbProvider.getOne(sql, params)
            # Chuyen tuple sang ScoreDTO
            scDto = ScoreDTO(sc[0],
                            sc[1], 
                            sc[2], 
                            sc[3]) if sc is not None else None
        except Exception as err:
            print(err)
        return scDto 
        
    def search(self, text: str):
        scDtos = []
        try: 
            sql = '''
                SELECT * FROM Scores
                WHERE StudentCode = %s 
                    OR SubjectCode = %s
            '''
            params=(text, text)
            scs = self.__dbProvider.get(sql, params) #tim kiem co the ra nhieu ket qua nen chon get 
            scDtos = list(map(lambda st: ScoreDTO(st[0], 
                                                    st[1], 
                                                    st[2], 
                                                    st[3]),
                            scs))
        except Exception as err:
            print(err)
        return scDtos #co cho bang None o tren cung khong?
    
    #Kiem tra cap ma mon hoc va ma hoc vien co cung ton tai
    def checkExists(self, studentCode: str, subjectCode: str):
        sc = None
        try: 
            sql = '''
                SELECT  * FROM Scores
                WHERE StudentCode = %s AND SubjectCode = %s
            '''
            params = (studentCode, subjectCode, ) #co dau phay khong?
            sc = self.__dbProvider.getOne(sql, params)
        except Exception as err:
            print(err)
        return sc is not None #return True neu co ton tai, False neu khong ton tai
    
    def getTotal(self):
        scDTOs = []
        try:
            sql = '''
                SELECT StudentCode, FullName, Birthday, Sex, Address, Phone, Email, sj.Name as SubjectName, ProcessScore, FinalTestScore
                FROM Scores sc
                JOIN Students st ON sc.StudentCode = st.Code
                JOIN Subjects sj ON sc.SubjectCode = sj.Code 
            '''

            scs = self.__dbProvider.get(sql)
            scDTOs = list(map(lambda sc: TotalDTO(sc[0],sc[1],sc[2],sc[3],sc[4],sc[5],sc[6],sc[7],sc[8],sc[9]),scs))
        except Exception as err:
            print(err)
        return scDTOs