class StudentModel:
    def __init__(self,id=0,name="",age=0,score=0):
        self.id=id
        self.name=name
        self.age=age
        self.score=score

class StudentManagerController:
    def __init__(self):
        self.__stu_list=[]
    @property
    def stu_list(self):
        return self.__stu_list


