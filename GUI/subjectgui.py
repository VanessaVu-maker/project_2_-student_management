
from BLL import SubjectBLL
from DTO import SubjectDTO
from utils import clearScreen, printHeader, printMenu


class SubjectGUI:
    def __init__(self):
        self.__subBLL = SubjectBLL() #vi sao ko import duoc subBLL ben main -> khong kich hoat duoc subBLL (vi khong tab pass) -> ko checkexist duoc

    def subjectMenuScreen(self):
        clearScreen()
        printHeader('QUẢN LÍ MÔN HỌC')
        funcs = [
            '1. Thêm',
            '2. Sửa',
            '3. Xóa',
            '4. Tìm kiếm',
            '0. Trở về màn hình CHƯƠNG TRÌNH QUẢN LÝ ĐIỂM THI'
        ]
        printMenu(funcs)

        # Điều hướng màn hình

        cmd = None 
        while cmd not in ['1','2','3','4','0']: 
            cmd = input('Chọn chức năng: ')

        if cmd == '1':
            # Chuyển sang màn hình Thêm MÔN HỌC 
            self.addSubjectScreen() #tai sao khong goi addSubjectScreen? - quen ko tab pass :))
            self.subjectMenuScreen()
        elif cmd == '2':
            # Chuyển sang màn hình Sửa MÔN HỌC
            self.editSubjectScreen()
            self.subjectMenuScreen()
        elif cmd == '3':
            # Chuyển sang màn hình Xóa MÔN HỌC
            self.deleteSubjectScreen()
            self.subjectMenuScreen()
        elif cmd == '4':
            # Chuyển sang màn hình Tìm kiếm MÔN HỌC
            self.searchSubjectScreen()
            self.subjectMenuScreen()
        elif cmd =='0':
            # Chuyển về màn hình 
            pass

    def addSubjectScreen(self):
        clearScreen()
        printHeader('THÊM MÔN HỌC')
        
        # Nhập dữ liệu từ bàn phím
        # Validate dữ liệu nhập từ bàn phím - ma mon hoc

        while True:
            Code = input('Nhập vào mã môn học: ') 
            # Không được để trống
            if Code == '':
                print('Không được để trống Mã môn học ')
                continue
            # Không được trùng
            isExists = self.__subBLL.checkExists(Code)
            if isExists == True:
                print(f'Mã Subject "{Code}" đã được sử dụng.')
                continue
            # Phai viet in hoa
            if Code.isupper() == False:
                print('Mã môn học phải viết in hoa')
                continue
            # 3 ký tự đầu phải là 'SUB'
            if Code.startswith('SUB') == False:
                print('2 ký tự đầu phải là "SUB".')
                continue
            # 5 ki tu
            if len(Code) != 5:
                print('Mã môn học có 5 kí tự')
                continue
            break

        # Validate dữ liệu nhập từ bàn phím - tên môn học

        while True:
            Name = input('Nhập vào tên môn học: ')  
            # KHông được để trống
            if Name == '':
                print('Không được để trống Tên môn học')
                continue
            #Ko duoc trung ten mon hoc
            isExists = self.__subBLL.checkExistsName(Name) 
            if isExists == True:
                print('Tên môn học đã tồn tại')
                continue
            break
        
        # Đổ dữ liệu vào cái túi SubjectDTO
        sub = SubjectDTO(Code, Name)
        self.__subBLL.insert(sub)
        print(f"Thêm môn học {Name} thành công !!!")

        ans = input('Nhập y/Y để tiếp tục')
        if ans.lower() == 'y':
            self.addSubjectScreen() 
    
    def editSubjectScreen(self):
        clearScreen()
        printHeader('CHỈNH SỬA THÔNG TIN MÔN HỌC')

        while True:
            Code = input('Mã môn cần sửa: ')
            # Không được để trống
            if Code == '':
                print('Không được để trống Mã môn học ')
                continue
            # check ton tai
            isExists = self.__subBLL.checkExists(Code)
            if isExists == False:
                print(f'Mã Subject "{Code}" ko ton tai.')
                continue
            # 3 ký tự đầu phải là 'SUB'
            if Code.startswith('SUB') == False:
                print('2 ký tự đầu phải là "SUB".')
                continue
            # Phai viet in hoa
            if Code.isupper() == False:
                print('Mã môn học phải viết in hoa')
                continue
            # 5 ki tu
            if len(Code) != 5:
                print('Mã môn học có 5 kí tự')
                continue
            break
    
        # Lấy thông tin theo mã môn học đã nhập
        sub = self.__subBLL.getByCode(Code)

        print('Môn học:', sub.Name)  # Hiển thị tên cũ #Khong truy cap mang [] vi bay gio khong dung list nua
        name = sub.Name
        ans = input('Nhập y/Y để sửa: ')
        if ans.lower() == 'y':
            name = input('Tên môn mới: ')  

        # Sửa thông tin - Do du lieu vao tui SubjectDTO
        newSub = SubjectDTO(Code, name) #tai sao Name lai not defined neu viet hoa
        rowCount = self.__subBLL.update(newSub)
        if rowCount == 0:
            print('Edit attempt failed')
        else:
            print(f'Chỉnh sửa Subject có mã "{Code}" thành công !!!')

        ans = input('Nhập y/Y để tiếp tục: ')
        if ans.lower() == 'y':
            # Quay lại nhập tiếp, call chính nó
            self.editSubjectScreen()
    
    def deleteSubjectScreen(self):
        clearScreen()
        printHeader('XÓA MÔN HỌC')

        while True:
            code = input('Mã môn học cần xóa: ')
            if len(code) != 5:
                print('Mã mon hoc phải bao gồm 5 ký tự.')
                continue
            # check ton tai
            isExists = self.__subBLL.checkExists(code)
            if isExists == False:
                print(f'Mã Subject "{code}" khong ton tai.')
                continue
            break

        # Xóa

        rowCount = self.__subBLL.delete(code)
        if rowCount == 0:
            print('Delete attempt failed')
        else:
            print(f'Xóa môn học có mã "{code}" thành công')

        ans = input('Nhập y/Y để tiếp tục: ')
        if ans.lower() == 'y':
            # Quay lại nhập tiếp, call chính nó
            self.deleteSubjectScreen()

    def searchSubjectScreen(self): 
        subs = self.__subBLL.get() 
        self.printSubjects(subs)

        searchContent = input('Nội dung tìm kiếm: ')
        if searchContent != '':
            subsFiltered = self.__subBLL.search(searchContent)
            self.printSubjects(subsFiltered)
            
        ans = input('Nhập y/Y để tiếp tục: ')
        if ans.lower() == 'y':
            # Quay lại nhập tiếp, call chính nó
            self.searchSubjectScreen()
    
    def printSubjects(self, subs: list):
        clearScreen()
        printHeader('DANH SÁCH MÔN HỌC')
        
        from tabulate import tabulate

        #Cach 1 (convert subjectDTO -> list): 
        # subjectList = list(map(lambda sub: [sub.Code, sub.Name], subs))
        # print(subjectList) -> du lieu hien thi la List cua List. 
        # Dung map de transform datatype cua tung phan tu mot

        #Cach 2: dung vong lap for
        subjectList =[]
        for sub in subs:
            s = [sub.Code, sub.Name]
            subjectList.append(s)
        
        h = ['Mã MH', 'Tên MH']
        print(tabulate(subjectList, headers = h, tablefmt= 'psql'))