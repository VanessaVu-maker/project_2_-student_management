class TotalDTO: 
    def __init__(self, studentCode: str, studentName: str, birthDay: str, sex: str, address: str, phone: str, 
    email: str, subjectName: str, processScore: float, finalTestScore: float):
        self.StudentCode = studentCode
        self.StudentName = studentName
        self.BirthDay = birthDay
        self.Sex = sex
        self.Address = address
        self.Phone = phone
        self.Email = email
        self.SubjectName = subjectName
        self.ProcessScore = processScore
        self.FinalTestScore = finalTestScore

