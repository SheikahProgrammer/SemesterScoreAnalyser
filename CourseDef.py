import csv

def BLTS(lst):
    string = str(lst)
    string=string.replace('[','')
    string=string.replace(']','')         
    string=string.replace(', ',':') 
    return string

class CourseTheory:
    def __init__(self,code, cats, fat, ias,avg,std):
        self.code = code
        self.cats = cats
        self.fat = fat
        self.ias = ias
        self.average = avg
        self.std = std
        self.absolute_score = (((self.fat)/100)*0.4+(sum(self.cats)/(50*len(self.cats))*0.3)+ (sum(self.ias)/(len(self.ias)*10))*0.3)*100
        self.ScoreFor = {
            'S':self.average +1.5*self.std,
            'A':self.average +0.5*self.std,
            'B':self.average -0.5*self.std,
            'C':self.average -1.5*self.std,
        }
        GradeScore = {
            'S':10,
            'A':9,
            'B':8,
            'C':7,
        }
        if self.average == -1:
            self.grade = 'U'
            self.gscore = self.std
        elif self.absolute_score >= self.ScoreFor['S']:
            self.grade = 'S'
            self.gscore = 10
        elif self.absolute_score >= self.ScoreFor['A']:
            self.grade = 'A'
            self.gscore = 9
        elif self.absolute_score >= self.ScoreFor['B']:
            self.grade = 'B'
            self.gscore = 8
        elif self.absolute_score >= self.ScoreFor['C']:
            self.grade = 'C'
            self.gscore = 7
        else:
            self.grade = 'F'
    def ShowScore(self):
        print(str(self.absolute_score)+" %")
        print(self.gscore)
    def Save(self):
        with open('Theory.csv', 'a', newline='') as file:
            csv.writer(file).writerow([self.code, BLTS(self.cats), BLTS(self.ias),self.fat ,self.absolute_score,self.grade,self.gscore]) 
    
#EXAMPLE = CourseTheory('BEXP101L',[50,50],100,[10,10,10],80,2)
#print(EXAMPLE.ScoreFor)
#EXAMPLE.ShowScore()
#EXAMPLE.Save()

class CourseLab:
    def __init__(self,code, fat, ias):
        self.code = code
        self.fat = fat
        self.ias = ias
        self.score = ((((self.fat)/100)*0.4)+ (sum(self.ias)/(len(self.ias)*10))*0.6)*100
    def ShowScore(self):
        print(str(self.score)+" %")
    def Save(self):
        with open('Lab.csv', 'a', newline='') as file:
            csv.writer(file).writerow([self.code, BLTS(self.ias),self.fat ,self.score])

#EXAMPLE = CourseLab('BEXP101P',100,[10,10,10,10,5])
#EXAMPLE.Save()

class CourseEmbedded:
    def __init__(self,code, fat, pats,mat):
        self.code = code
        self.fat = fat
        self.mat = mat
        self.pats = pats
        self.score = ((((self.fat)/100)*0.4)+ (sum(self.pats)/(len(self.pats)*10))*0.5+(((self.mat)/50)*0.1))*100 
    def ShowScore(self):
        print(str(self.score)+" %")
    def Save(self):
        with open('Embedded.csv', 'a', newline='') as file:
            csv.writer(file).writerow([self.code, BLTS(self.pats),self.mat,self.fat ,self.score])

#EXAMPLE = CourseEmbedded('BEXP101E',100,[10,10,10,10,10],50)
#EXAMPLE.ShowScore()
#EXAMPLE.Save()