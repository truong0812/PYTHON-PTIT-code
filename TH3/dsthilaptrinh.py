
Teams = {}
class Team:
    def __init__(self,name,school) -> None:
        self.name = name
        self.school = school
    
for i in range(int(input())):
    code = "Team%02d" % (i+1)
    x = Team(input(),input())
    Teams[code] = x
      
class Student:
    global Teams
    def __init__(self,id,name,team) -> None:
        self.code = "C%03d" %(id)
        self.name = name
        self.team = Teams[team].name
        self.school = Teams[team].school
    def __str__(self) -> str:
        return "%s %s %s %s" % (self.code,self.name,self.team,self.school)
    
Students = []
for i in range(int(input())):
    Students.append(Student(i+1,input(),input()))
Students.sort(key=lambda x:x.name)
for i in Students:
    print(i)
    
