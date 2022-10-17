from re import L
from BLL import StudentBLL
from DTO import StudentDTO
from utils import clearScreen, printHeader, printMenu, checkEmail, checkDate
from tabulate import tabulate

class StudentGUI:
    def __init__(self):
        self.__stBLL = StudentBLL()
    
    def studentMenuScreen(self):
        clearScreen()
        printHeader('QUẢN LÝ HỌC VIÊN')

        funcs = [
            '1. Thêm HỌC VIÊN',
            '2. Sửa HỌC VIÊN',
            '3. Xoá HỌC VIÊN',
            '4. Danh sách HỌC VIÊN',
            '0. Trở về màn hình CHƯƠNG TRÌNH QUẢN LÝ ĐIỂM THI'
        ]
        printMenu(funcs)

        cmd = None  # mã lệnh người dùng chọn, ban đầu chưa phải lệnh nào cả
        while cmd not in ['1', '2', '3', '4', '0']:
            cmd = input('Chọn chức năng: ')

        if cmd == '1':
            # Chuyển sang màn hình Thêm Học viên
            self.addStudentScreen()
            # Quay lại màn hình Menu QL Học viên (Gọi chính nó)
            self.studentMenuScreen()
        elif cmd == '2':
            # Chuyển sang màn hình Sửa Học viên
            self.editStudentScreen()
            # Quay lại màn hình Menu QL Học viên (Gọi chính nó)
            self.studentMenuScreen()
        elif cmd == '3':
            # Chuyển sang màn hình Xoá Học viên
            self.deleteStudentScreen()
            # Quay lại màn hình Menu QL Học viên (Gọi chính nó)
            self.studentMenuScreen()
        elif cmd == '4':
            # Chuyển sang màn hình Danh sách Học viên
            self.searchStudentScreen()
            # Quay lại màn hình Menu QL Học viên (Gọi chính nó)
            self.studentMenuScreen()
        elif cmd == '0':
            # Trở về màn hình Menu chính
            pass

    def addStudentScreen(self):
        clearScreen()
        printHeader('THÊM HỌC VIÊN')

        # Nhập dữ liệu từ bàn phím
        # Validate dữ liệu nhập từ bàn phím - ma hoc vien
        while True:
            code = input('Mã HV: ')
            # Khong duoc bo trong
            if code == '':
                print('Không được để trống mã MH')
                continue
            # không tồn tại trong DB
            isExists = self.__stBLL.checkExists(code)
            if isExists == True:
                print(f'Mã HV "{code}" đã được sử dụng.')
                continue
            # phai viet hoa
            if code.isupper() == False:
                print('Mã học viên phải viết hoa')
                continue
            # 2 ký tự đầu phải là 'PY'
            if code.startswith('PY') == False:
                print('2 ký tự đầu phải là "PY".')
                continue
            # 6 ký tự
            if len(code) != 6:
                print('Mã HV phải bao gồm 6 ký tự.')
                continue
            break    
        
        # Validate dữ liệu nhập từ bàn phím - ten hoc vien
        while True:
            fullName = input('Họ tên:')  
            # Khong duoc bo trong
            if fullName == '':
                print('Không được để trống tên học viên')
                continue  
            # Phai viet hoa 
            if fullName.isupper() == False:
                print('Tên học viên phải viết hoa ')
                continue
            break    

        # Validate dữ liệu nhập từ bàn phím - ngay sinh

        while True:
            birthday = input('Ngày sinh (dd/MM/yyyy): ') 
            # không được để trống
            if birthday == '':
                print('Không được để trống ngày sinh')
                continue
            # đúng định dang đd/MM/yyyy
            if checkDate(birthday) == None:
                print('Hãy nhập ngày sinh đúng với format dd/mm/yyyy')
                continue
            break   

        # Validate dữ liệu nhập từ bàn phím - gioi tinh

        while True:
            sex = input('Giới tính (0-nữ|1-nam): ') 
            # Không được bỏ trống
            if sex == '':
                print('Không được bỏ trống giới tính')
                continue
            # chỉ là '0' hoặc '1'
            if sex not in ['0','1']:
                print('Hãy nhập giới tính: 1 - Nam, 0 - nữ')
                continue
            break

        address = input('Địa chỉ: ')

        # Validate dữ liệu nhập từ bàn phím - SDT

        while True:
            phone = input('SĐT: ')       
            if phone == '':
                break   
            # Chỉ chứa số, độ dài 10 kí tự
            if phone.isdigit() == False:
                print('SĐT chỉ được chứa số')
                continue
            # độ dài 10 kí tự
            if len(phone) != 10:
                print(' Số điện thoại phải chứa đúng 10 kí tự')
                continue
            break  
        
        # Validate dữ liệu nhập từ bàn phím - email

        while True:
            email = input('Email: ')    
            if email == '':
                break     
            # Có thể không nhập, nhưng nếu nhập thì phải đúng format Email (sử dụng regex Email để check)  
            if checkEmail(email) == False:
                print('Yêu cầu nhập đúng format Email')
                continue
            break

        # Đổ dữ liệu vào cái túi 'StudentDTO' 
        st = StudentDTO(code, fullName, birthday, int(sex), address, phone, email)
        self.__stBLL.insert(st)
        print(f'Thêm học viên có mã "{code}" thành công !!!')

        ans = input('Nhập y/Y để tiếp tục: ')
        if ans.lower() == 'y':
            # Quay lại nhập tiếp, call chính nó
            self.addStudentScreen()

    def editStudentScreen(self):
        clearScreen()
        printHeader('CHỈNH SỬA THÔNG TIN HỌC VIÊN')

        while True:
            code = input('Mã HV cần sửa: ')
            # Khong duoc bo trong
            if code == '':
                print('Không được để trống mã MH')
                continue
            # phai tồn tại trong DB
            isExists = self.__stBLL.checkExists(code)
            if isExists == False:
                print(f'HV có mã "{code}" không tồn tại.')
                continue
            # 2 ký tự đầu phải là 'PY'
            if code.startswith('PY') == False:
                print('2 ký tự đầu phải là "PY".')
                continue
            # phai viet hoa
            if code.isupper() == False:
                print('Mã học viên phải viết hoa')
                continue
            # phai co 6 ki tu
            if len(code) != 6:
                print('Mã HV phải bao gồm 6 ký tự.')
                continue
            break

        # Lấy thông tin theo mã học viên đã nhập
        st = self.__stBLL.getByCode(code)

        print('Họ tên:', st.FullName)  # Hiển thị họ tên cũ #Khong truy cap mang [] vi bay gio khong dung list nua
        fullName = st.FullName
        ans = input('Nhập y/Y để sửa: ')
        if ans.lower() == 'y':
            while True:
                fullName = input('Họ tên mới: ')       
                # Khong duoc bo trong
                if fullName == '':
                    print('Không được để trống tên học viên')
                    continue
                # Phai viet hoa
                if fullName.isupper() == False:
                    print('Tên học viên phải viết hoa')
                    continue
                break      

        print('Ngày sinh:', st.Birthday)
        birthday = st.Birthday
        ans = input('Nhập y/Y để sửa: ')
        if ans.lower() == 'y':
            while True:
                birthday = input('Ngày sinh mới (dd/MM/yyyy): ') 
                # không được để trống
                if birthday == '':
                    print('Không được để trống ngày sinh')
                    continue
                # đúng định dang đd/MM/yyyy
                if checkDate(birthday) == None:
                    print('Hãy nhập ngày sinh đúng với format dd/mm/yyyy')
                    continue
                break   

        print('Giới tính:', st.Sex)
        sex = st.Sex
        ans = input('Nhập y/Y để sửa: ')
        if ans.lower() == 'y':
            while True:
                sex = input('Giới tính moiws (0-nữ|1-nam): ') 
                # Không được bỏ trống
                if sex == '':
                    print('Không được bỏ trống giới tính')
                    continue
                # chỉ là '0' hoặc '1'
                if sex not in ['0','1']:
                    print('Hãy nhập giới tính: 1 - Nam, 0 - nữ')
                    continue
                break

        print('Địa chỉ:', st.Address)
        address = st.Address
        ans = input('Nhập y/Y để sửa: ')
        if ans.lower() == 'y':
            address = input('Địa chỉ mới: ')

        print('SĐT:', st.Phone)
        phone = st.Phone
        ans = input('Nhập y/Y để sửa: ')
        if ans.lower() == 'y':
            while True:
                phone = input('SĐT moi: ')          
                # Có thể không nhập
                if phone == '':
                    break
                # Chỉ chứa số, độ dài 10 kí tự
                if phone.isdigit() == False:
                    print('SĐT chỉ được chứa số')
                    continue
                # độ dài 10 kí tự
                if len(phone) != 10:
                    print(' Số điện thoại phải chứa đúng 10 kí tự')
                    continue
                break  

        print('Email:', st.Email)
        email = st.Email
        ans = input('Nhập y/Y để sửa: ')
        if ans.lower() == 'y':
            while True:
                email = input('Email moi: ')        
                # Có thể không nhập
                if email == '':
                    break
                # Có thể không nhập, nhưng nếu nhập thì phải đúng format Email (sử dụng regex Email để check)  
                if checkEmail(email) == False:
                    print('Yêu cầu nhập đúng format Email')
                    continue
                break

        # Sửa thông tin - Do du lieu vao tui StudentDTO
        newSt = StudentDTO(code, fullName, birthday, int(sex), address, phone, email)
        rowCount = self.__stBLL.update(newSt)
        if rowCount == 0:
            print('Edit attempt failed')
        else:
            print(f'Chỉnh sửa học viên có mã "{code}" thành công !!!')

        ans = input('Nhập y/Y để tiếp tục: ')
        if ans.lower() == 'y':
            # Quay lại nhập tiếp, call chính nó
            self.editStudentScreen()

    def deleteStudentScreen(self):
        clearScreen()
        printHeader('XÓA HỌC VIÊN')

        while True:
            code = input('Mã HV cần xóa: ')
            if len(code) != 6:
                print('Mã HV phải bao gồm 6 ký tự.')
                continue
            isExists = self.__stBLL.checkExists(code)
            if isExists == False:
                print(f'HV có mã "{code}" không tồn tại.')
                continue
            break

        # Xóa
        rowCount = self.__stBLL.delete(code)
        if rowCount == 0:
            print('Delete attempt failed')
        else:
            print(f'Xóa học viên có mã "{code}" thành công !!!')

        ans = input('Nhập y/Y để tiếp tục: ')
        if ans.lower() == 'y':
            # Quay lại nhập tiếp, call chính nó
            self.deleteStudentScreen()

    def searchStudentScreen(self):
        sts = self.__stBLL.get()
        self.printStudents(sts)

        searchContent = input('Nội dung tìm kiếm: ')
        if searchContent != '':
            stsFiltered = self.__stBLL.search(searchContent)
            self.printStudents(stsFiltered)

        ans = input('Nhập y/Y để tiếp tục: ')
        if ans.lower() == 'y':
            # Quay lại nhập tiếp, call chính nó
            self.searchStudentScreen()
    
    def printStudents(self, sts: list):
        clearScreen()
        printHeader('DANH SÁCH HỌC VIÊN')

        #Cach 1 (convert studentDTO -> list): 
        studentList = list(map(lambda st: [st.Code, st.FullName, st.Birthday, st.Sex, st.Address, st.Phone, st.Email], sts))
        print(studentList) 
        h = ['Mã HV', 'Họ tên', 'Ngày sinh', 'Giới', 'Địa chỉ', 'SĐT', 'Email']
        print(tabulate(studentList, headers = h, tablefmt= 'psql'))
        
        # -> du lieu hien thi la List cua List. 
        # Dung map de transform datatype cua tung phan tu mot

        #Cach 2: dung vong lap for

        # studentList =[]
        # for st in sts:
        #     s = [st.Code, st.FullName, st.Birthday, st.Sex, st.Address, st.Phone, st.Email]
        #     studentList.append(s)
        


    
    

