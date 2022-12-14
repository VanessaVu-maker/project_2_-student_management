from DAL import StudentDAL, SubjectDAL, ScoreDAL
from DTO import StudentDTO, SubjectDTO, ScoreDTO

#test insert student

# stDAL = StudentDAL()
# stDTO = StudentDTO('PY0002', 'V T V', '07/07/2000', 0, 'Hanoi', '9990009999', 'abcc@gmail.com')
# rowCount = stDAL.insert(stDTO)
# print (rowCount)

#test insert subject

# subDAL = SubjectDAL()
# subDTO = SubjectDTO('SUB07', 'Maths')
# rowCount = subDAL.insert(subDTO)
# print (rowCount)

#test insert score

# scDAL = ScoreDAL()
# scDTO = ScoreDTO('PY0006', 'SUB03', 50.0, 80.0)
# rowCount = scDAL.insert(scDTO)
# print (rowCount)

#test update student

# stDAL = StudentDAL()
# stDTO = StudentDTO('PY0002', 'V T V', '07/07/1999', 0, 'Hanoi', '9990009999', 'abcc@gmail.com')
# rowCount = stDAL.update(stDTO)
# print (rowCount)

#test update subject

# subDAL = SubjectDAL()
# subDTO = SubjectDTO('SUB07', 'Probability')
# rowCount = subDAL.update(subDTO)
# print (rowCount)

#test update score

# scDAL = ScoreDAL()
# scDTO = ScoreDTO('PY0006', 'SUB03', 49.0, 80.0)
# rowCount = scDAL.update(scDTO)
# print (rowCount)

#test delete student
# stDAL = StudentDAL()
# rowCount = stDAL.delete('PY0001')
# print(rowCount)

# #test delete subject
# subDAL = SubjectDAL()
# rowCount = subDAL.delete('SUB02')
# print(rowCount)

#test delete score

# scDAL = ScoreDAL()
# rowCount = scDAL.delete('PY0003', 'SUB01')
# print(rowCount)


#test search student
# stDAL = StudentDAL()
# stDtos = stDAL.search('PY0006')
# for stDto in stDtos:
#     print(stDto.Code, '-', stDto.FullName, '-', stDto.Email)


#test search subject
# subDAL = SubjectDAL()
# subDtos = subDAL.search('P')
# for subDto in subDtos:
#     print(subDto.Code, '-', subDto.Name)


#test search score
# scDAL = ScoreDAL()
# scDtos = scDAL.search('SUB06')
# for scDto in scDtos:
#     print(scDto.StudentCode, '-', scDto.SubjectCode, '-', scDto.ProcessScore, '-', scDto.FinalTestScore)

from GUI import StudentGUI, SubjectGUI, ScoreGUI
from utils import clearScreen, printHeader, printMenu

class MainGUI:
    def __init__(self):
        self.__stGUI = StudentGUI()
        self.__subGUI = SubjectGUI()
        self.__scGUI = ScoreGUI()

    def mainMenuScreen(self):
        clearScreen()
        printHeader('CH????NG TR??NH QU???N L?? ??I???M THI')

        try:
            funcs = [
                '1. Qu???n l?? H???c vi??n',
                '2. Qu???n l?? M??n H???c',
                '3. Qu???n l?? ??i???m thi',
                '0. Tho??t'
            ]
            printMenu(funcs)

            cmd = None # m?? l???nh ng?????i d??ng ch???n, ban ?????u ch??a ph???i l???nh n??o c???
            while cmd not in ['1', '2', '3', '0']:
                cmd = input('Ch???n ch???c n??ng: ')

            if cmd == '1':
                # Chuy???n sang m??n h??nh QL H???c vi??n
                self.__stGUI.studentMenuScreen()
                # Quay l???i m??n h??nh Menu ch??nh (G???i ch??nh n??)
                self.mainMenuScreen()
            elif cmd == '2':
                # Chuy???n sang m??n h??nh QL M??n h???c
                self.__subGUI.subjectMenuScreen()
                self.mainMenuScreen()
                pass
            elif cmd == '3':
                # Chuy???n sang m??n h??nh QL ??i???m thi
                self.__scGUI.scoreMenuScreen()
                self.mainMenuScreen()
                pass
            elif cmd == '0':
                # Tho??t ch????ng tr??nh
                print('K???t th??c ch????ng tr??nh. H???n g???p l???i !!!')
                exit()
        except Exception as err:
            print(err)

if __name__ == '__main__':
    mainGUI = MainGUI()
    mainGUI.mainMenuScreen()