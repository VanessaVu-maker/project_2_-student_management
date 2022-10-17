from BLL import ScoreBLL, SubjectBLL, StudentBLL
from DTO import ScoreDTO
from utils import clearScreen, printHeader, printMenu, checkFloat
import pandas as pd
from tabulate import tabulate

class ScoreGUI:
    def __init__(self):
        self.__scBLL = ScoreBLL()
        self.__subBLL = SubjectBLL()
        self.__stBLL = StudentBLL()
    
    def scoreMenuScreen(self):
        clearScreen()
        printHeader('QUẢN LÍ ĐIỂM THI')
        funcs = [
            '1. Thêm ĐIỂM THI',
            '2. Sửa ĐIỂM THI',
            '3. Xóa ĐIỂM THI',
            '4. Tìm kiếm ĐIỂM THI',
            '5. Thống kê theo Điểm Tổng Kết',
            '0. Trở về màn hình chính'
        ]
        printMenu(funcs)

        # Điều hướng màn hình

        cmd = None 
        while cmd not in ['1','2','3','4', '5','0']: 
            cmd = input('Chọn chức năng: ')

        if cmd == '1':
            self.addScoreScreen()
            self.scoreMenuScreen()
        elif cmd == '2':
            self.editScoreScreen()
            self.scoreMenuScreen()
        elif cmd == '3':
            self.deleteScoreScreen()
            self.scoreMenuScreen()
        elif cmd == '4':
            self.searchScoreScreen()
            self.scoreMenuScreen()
        elif cmd == "5":
            self.rankScoreScreen()
            self.scoreMenuScreen()
        elif cmd == '0':
            # Trở về màn hình Menu chính
            pass

    def addScoreScreen(self):
        clearScreen()
        printHeader('THÊM ĐIỂM THI')

        # Validate dữ liệu nhập từ bàn phím - student_Code
        while True:
            studentCode = input('Nhập mã học viên: ')
            # Khong duoc bo trong
            if studentCode == '':
                print('Không được để trống mã HV')
                continue
            if len(studentCode) != 6:
                print('Mã HV phải bao gồm 6 ký tự.')
                continue
            # 2 ký tự đầu phải là 'PY'
            if studentCode.startswith('PY') == False:
                print('2 ký tự đầu phải là "PY".')
                continue
            # phai viet hoa
            if studentCode.isupper() == False:
                print('Mã học viên phải viết hoa')
                continue
            # phai tồn tại trong DB 
            isExists = self.__stBLL.checkExists(studentCode)
            if isExists == False:
                print(f'Mã HV "{studentCode}" ko ton tai')
                continue
            break 

        # Validate dữ liệu nhập từ bàn phím - ma mon hoc

        while True:
            subjectCode = input('Nhập vào mã môn học: ') 
            # Không được để trống
            if subjectCode == '':
                print('Không được để trống Mã môn học ')
                continue
            # Phai viet in hoa
            if subjectCode.isupper() == False:
                print('Mã môn học phải viết in hoa')
                continue
            # 5 ki tu
            if len(subjectCode) != 5:
                print('Mã môn học phải có 5 kí tự')
                continue
            # phai tồn tại trong DB 
            isExists = self.__subBLL.checkExists(subjectCode)
            if isExists == False:
                print(f'Mã MH "{subjectCode}" ko ton tai')
                continue
            break

        # Kiểm tra xem đã có điểm thi nào tồn tại hay chưa (check dùng bộ studentCode và subjectCode, hàm checkExists

        isExists = self.__scBLL.checkExists(studentCode, subjectCode)
        if isExists == True:
            print('Điểm này đã nhập rồi!') 
        else:
            while True:
                processScore = input('Nhập điểm quá trình: ')
                # Không được để trống
                if processScore == '':
                    print('Không được để trống điểm quá trình ')
                    continue
                #check Float
                if checkFloat(processScore) == False:
                    print('!!! Hãy nhập vào điểm là 1 số thực')
                    continue        
                # 1-100
                if float(processScore) > 100 or float(processScore) < 0:
                    print('Vui lòng nhập lại điểm từ 1-100')
                    continue
                break  
            
            while True:
                finalTestScore = input('Nhập điểm kết thúc: ')    
                # Không được để trống
                if finalTestScore == '':
                    print('Không được để trống điểm kết thúc')
                    continue  
                #check Float
                if checkFloat(processScore) == False:
                    print('!!! Hãy nhập vào điểm là 1 số thực')
                    continue   
                # 1-100
                if float(finalTestScore) > 100 or float(finalTestScore) < 0:
                    print('Vui lòng nhập lại điểm từ 1-100')
                    continue    
                break  


            # Đổ dữ liệu vào cái túi 'ScoreDTO' 
            sc = ScoreDTO(studentCode, subjectCode, processScore, finalTestScore)
            self.__scBLL.insert(sc)
            print("Thêm điểm thành công!!")

        ans = input("Nhập y/Y để tiếp tục thêm: ")
        if ans.lower() == 'y':
            # quay lại để nhập tiếp
            self.addScoreScreen()
    
    def editScoreScreen(self):
        clearScreen()
        printHeader('CHỈNH SỬA THÔNG TIN ĐIỂM THI')

        # Nhập dữ liệu từ bàn phím
        # Validate dữ liệu nhập từ bàn phím - studentCode
        while True:
            # 6 ký tự
            studentCode = input('Mã HV cần sửa: ')
            # Khong duoc bo trong
            if studentCode == '':
                print('Không được để trống mã HV')
                continue
            if len(studentCode) != 6:
                print('Mã HV phải bao gồm 6 ký tự.')
                continue
            # 2 ký tự đầu phải là 'PY'
            if studentCode.startswith('PY') == False:
                print('2 ký tự đầu phải là "PY".')
                continue
            # phai tồn tại trong bảng score 
            isExists = self.__stBLL.checkExists(studentCode)
            if isExists == False:
                print(f'Mã HV "{studentCode}" ko ton tai')
                continue
            # phai viet hoa
            if studentCode.isupper() == False:
                print('Mã học viên phải viết hoa')
                continue
            break 

        # Validate dữ liệu nhập từ bàn phím - subjectCode
        while True:
            subjectCode = input('Nhập vào mã môn học: ') 
            # Không được để trống
            if subjectCode == '':
                print('Không được để trống Mã môn học ')
                continue
            # phai tồn tại trong DB 
            isExists = self.__subBLL.checkExists(subjectCode)
            if isExists == False:
                print(f'Mã HH "{subjectCode}" ko ton tai')
                continue
            # Phai viet in hoa
            if subjectCode.isupper() == False:
                print('Mã môn học phải viết in hoa')
                continue
            # 5 ki tu
            if len(subjectCode) != 5:
                print('Mã môn học phải có 5 kí tự')
                continue
            break

        # Validate để ensure là cặp studentCode, subjectCode được nhập vào đã tồn tại để có thể chỉnh sửa
    
        isExists = self.__scBLL.checkExists(studentCode, subjectCode)
        if isExists == True:

            #     print(f'Điểm thi của học viên "{studentCode}" có mã "{subjectCode}" ko ton tai')
            #     continue
            # break

        #  Lấy thông tin theo mã học viên và mã môn học đã nhập
            sc = self.__scBLL.getByCode(studentCode, subjectCode)

            print('Điểm quá trình:', sc.ProcessScore)
            processScore_new = sc.ProcessScore
            ans = input('Nhập y/Y để sửa: ')
            if ans.lower() == 'y':
                # Validate process score mới
                processScore_new = input('Điểm quá trình mới: ')
                while True:       
                    # Không được để trống
                    if processScore_new == '':
                        print('Không được để trống điểm quá trình ')
                        continue
                    #check Float
                    if checkFloat(processScore_new) == False:
                        print('Hãy nhập vào điểm là 1 số thực')
                        continue   
                    # 1-100
                    if float(processScore_new) > 100 or float(processScore_new) < 0:
                        print('Vui lòng nhập lại điểm từ 1-100')
                        continue
                    break  

            print('Điểm kết thúc:', sc.FinalTestScore)
            finalTestScore_new = sc.FinalTestScore
            ans = input('Nhập y/Y để sửa: ')
            if ans.lower() == 'y':  
                while True:
                    finalTestScore_new = input('Nhập điểm kết thúc mới: ')
                    # Không được để trống
                    if finalTestScore_new == '':
                        print('Không được để trống điểm kết thúc')
                        continue      
                    #check Float
                    if checkFloat(finalTestScore_new ) == False:
                        print('Hãy nhập vào điểm là 1 số thực')
                        continue   
                    # 1-100
                    if float(finalTestScore_new) > 100 or float(finalTestScore_new) < 0:
                        print('Vui lòng nhập lại điểm từ 1-100')
                        continue
                    break  

                # Sửa thông tin - Do du lieu vao tui ScoreDTO
                newSc = ScoreDTO(studentCode, subjectCode, processScore_new, finalTestScore_new) 
                rowCount = self.__scBLL.update(newSc)
                if rowCount == 0:
                    print('Edit attempt failed')
                else:
                    print(f'Chỉnh sửa điểm của học viên có mã "{studentCode}", môn "{subjectCode}" thành công !!!')
        else:
            print(f'Điểm thi của học viên "{studentCode}" có mã "{subjectCode}" ko ton tai')

        ans = input('Nhập y/Y để tiếp tục: ')
        if ans.lower() == 'y':
            # Quay lại nhập tiếp, call chính nó
            self.editScoreScreen()
    
    def deleteScoreScreen(self):
        clearScreen()
        printHeader('XÓA ĐIỂM THI')
        
        while True:
            studentCode = input('Mã học viên cần xóa: ')
            if len(studentCode) != 6:
                print('Mã HV phải bao gồm 6 ký tự.')
                continue
            isExists = self.__stBLL.checkExists(studentCode)
            if isExists == False:
                print(f'Mã HV "{studentCode}" ko ton tai')
                continue
            break

        while True:
            subjectCode = input('Mã môn học cần xóa: ')
            if len(subjectCode) != 5:
                print('Mã HV phải bao gồm 5 ký tự.')
                continue
            isExists = self.__subBLL.checkExists(subjectCode)
            if isExists == False:
                print(f'Mã HV "{subjectCode}" ko ton tai')
                continue
            break

        isExists = self.__scBLL.checkExists(studentCode, subjectCode)
        if isExists == False:
            print(f'Điểm của học viên có mã"{studentCode}", môn "{subjectCode}" không tồn tại')
        else:
            # Xóa
            rowCount = self.__scBLL.delete(studentCode, subjectCode)
            if rowCount == 0:
                print('Delete attempt failed')
            else:
                print(f'Xóa điểm môn học có mã "{subjectCode}" cua hoc vien co ma "{studentCode}" thành công')

        ans = input('Nhập y/Y để tiếp tục: ')
        if ans.lower() == 'y':
            # Quay lại nhập tiếp, call chính nó
            self.deleteScoreScreen()
    
    def searchScoreScreen(self):
        scs = self.__scBLL.get()
        self.printScores(scs)

        searchContent = input('Nội dung tìm kiếm: ')
        if searchContent != '':
            scsFiltered = self.__scBLL.search(searchContent)
            self.printScores(scsFiltered)

        ans = input('Nhập y/Y để tiếp tục: ')
        if ans.lower() == 'y':
            # Quay lại nhập tiếp, call chính nó
            self.searchScoreScreen()
     
    def printScores(self, scs: list):
        clearScreen()
        printHeader('DANH SÁCH ĐIỂM THI')
        
        # scoreList =[]
        # for sc in scs:
        #     s = [sc.StudentCode, sc.SubjectCode, sc.ProcessScore, sc.FinalTestScore]
        #     scoreList.append(s)
        
        scoreList = list(map(lambda sc: [sc.StudentCode, sc.SubjectCode, sc.ProcessScore, sc.FinalTestScore], scs))
        
        h = ['Mã HV', 'Mã MH', 'Điểm quá trình', 'Điểm kết thúc' ]
        print(tabulate(scoreList, headers = h, tablefmt= 'psql'))

    def rankScoreScreen(self):
        clearScreen()
        printHeader('XẾP HẠNG HỌC VIÊN THEO ĐIỂM TỔNG KẾT')
        totalsDTO = self.__scBLL.getTotal()             # Lấy tất cả thông tin ở dạng DTO
        totals = list(map(lambda totalDTO: [totalDTO.StudentCode, totalDTO.StudentName, totalDTO.BirthDay, totalDTO.Sex, totalDTO.Address, totalDTO.Phone, totalDTO.Email, totalDTO.SubjectName, totalDTO.ProcessScore, totalDTO.FinalTestScore],totalsDTO))
        
        rankScoreList = []        # List để append total, diem tong ket va rank, dung de in ra dinh dang table         
        for total in totals: 
            totalScore = (float(total[8]) + float(total[9]) *2) / 3 #diem tong ket
            if totalScore >= 90 and totalScore <= 100:
                rank = 'A'
            elif totalScore >=70 and totalScore <90:
                rank = 'B'
            elif totalScore >=50 and totalScore < 70:
                rank = 'C'
            elif totalScore < 50:
                rank = 'D'    

            totalRank = list(total) #totalRank la list tat ca total + diem tong ket + rank, phai ep  kieu ve dang list de append
            totalRank.append(round(totalScore, 2)) #add diem tong ket vao totalRank
  
            totalRank.append(rank) #add rank vao list total + diem tong ket
            rankScoreList.append(totalRank) #add list tren vao rankScoreList dung de in ra dinh dang table 
        self.printScoresTotal(rankScoreList) 

        ans = input('Nhập y/Y để exit: ')
        if ans.lower() != 'y':
            self.rankScoreScreen()
    
    def printScoresTotal(self,totals: list):
        clearScreen()
        printHeader('DANH SÁCH ĐIỂM')
        h = ['Mã học viên', 'Họ tên', 'Ngày sinh', 'Giới tính', 'Địa chỉ', 'Số điện thoại', 'Email', 'Tên môn học', 'Điểm quá trình', 'Điểm kết thúc', 'Điểm tổng kết', 'Ranking']
        print(tabulate(totals, headers = h, tablefmt = 'psql'))

        data = pd.DataFrame(totals, columns=h)
        data.to_csv('rank_Score_List.csv', index=False)



        
