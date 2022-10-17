from DAL import SubjectDAL
from DTO import SubjectDTO


class SubjectBLL:
    def __init__(self):
        self.__subDAL = SubjectDAL()
    
    def insert(self, sub: SubjectDTO):
        return self.__subDAL.insert(sub)

    def update(self, sub: SubjectDTO):
        return self.__subDAL.update(sub)

    def delete(self, code: str):
        return self.__subDAL.delete(code)

    def get(self):
        return self.__subDAL.get()

    def getByCode(self, code: str):
        return self.__subDAL.getByCode(code)

    def search (self, text: str):
        return self.__subDAL.search(text)
    
    def checkExists(self, code: str):
        return self.__subDAL.checkExists(code)
    
    def checkExistsName(self, name: str):
        return self.__subDAL.checkExistsName(name)