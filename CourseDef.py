import csv

def BLTS(lst):
    string = str(lst)
    string=string.replace('[','')
    string=string.replace(']','')         
    string=string.replace(', ',':') 
    return string

class CourseTheory:
    def __init__(self,code, cats, fat, ias):
        self.code = code
        self.cats = cats
        self.fat = fat
        self.ias = ias
        self.score = (((self.fat)/100)*0.4+(sum(self.cats)/(50*len(self.cats))*0.3)+ (sum(self.ias)/(len(self.ias)*10))*0.3)*100
    def ShowScore(self):
        print(str(self.score)+" %")
    def Save(self):
        with open('Theory.csv', 'a', newline='') as file:
            csv.writer(file).writerow([self.code, BLTS(self.cats), BLTS(self.ias),self.fat ,self.score]) 

EXAMPLE = CourseTheory('BEXP101L',[50,50],100,[10,10,10])
EXAMPLE.ShowScore()
EXAMPLE.Save()

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