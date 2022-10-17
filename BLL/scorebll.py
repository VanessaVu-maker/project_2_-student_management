from DAL import ScoreDAL
from DTO import ScoreDTO


class ScoreBLL:
    def __init__(self):
        self.__scDAL = ScoreDAL()
    
    def insert(self, sc: ScoreDTO):
        return self.__scDAL.insert(sc)

    def update(self, sc: ScoreDTO):
        return self.__scDAL.update(sc)

    def delete(self, studentCode: str, subjectCode: str):
        return self.__scDAL.delete(studentCode, subjectCode)

    def get(self):
        return self.__scDAL.get()

    def getByCode(self, studentCode: str, subjectCode: str):
        return self.__scDAL.getByCode(studentCode, subjectCode)

    def search (self, text: str):
        return self.__scDAL.search(text)
    
    def checkExists(self, studentCode: str, subjectCode: str):
        return self.__scDAL.checkExists(studentCode, subjectCode)

    def getTotal(self):
        return self.__scDAL.getTotal()
    