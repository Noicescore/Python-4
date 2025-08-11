class student:
    siso=0
    def __init__(self, na="", ma="", li="", en=""):
        self.name=na
        self.math=ma
        self.literature=li
        self.english=en
        student.siso+=1
    @classmethod
    def from_string(cls, input_string):
        te, to, va, an= input_string.split(",")
        return cls(te, to, va, an)
    @staticmethod
    def getschoolinfo():
        return "Truong THCS Ngo Quyen - Ho Chi Minh"
    def score_average(std):
        return(std.score['Văn'] + std.score['Toán'] + std.score['Anh'])/3
        
    def show_rank(std):
        averageScore=std.score_average()
        if averageScore>= 9:
            return 'Giỏi'
        elif averageScore>= 6:
            return 'Khá'
        else:
            return 'Yếu'
    def showinfostudent(std):
        print('Tên học sinh: ', std.name )
        for key in std.score:
            print(f'Điểm môn {key}: {std.score[key]}')
        averagescore= std.score_average()
        averageround= round(averagescore,2)
        print(f'Điểm trung bình: {averageround}')
        print('Xếp loại: ', std.show_rank())

std1= student()
std1.name= 'Gia Phát'
std1.score= {'Văn': 8, 'Toán': 10, 'Anh': 9}
std1.showinfostudent()