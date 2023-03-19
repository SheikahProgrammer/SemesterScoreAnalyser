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

#EXAMPLE = CourseTheory('BEXP101L',[50,50],100,[10,10,10])
#EXAMPLE.ShowScore()
#EXAMPLE.Save()