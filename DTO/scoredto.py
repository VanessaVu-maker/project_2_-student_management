class ScoreDTO: 
    def __init__(self, studentCode: str, subjectCode: str, processScore: float, finalTestScore: float):
        self.StudentCode = studentCode
        self.SubjectCode = subjectCode
        self.ProcessScore = processScore
        self.FinalTestScore = finalTestScore
