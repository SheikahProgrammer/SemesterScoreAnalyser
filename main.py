from CourseDef import *
from TableView import *
while True:
    print("""
    Press 1 for insertion of data
    Press 2 for viewing data
    Press 3 for exiting
    """)
    cmd = int(input())
    if cmd == 1:
        print("""
    Press 1 for Theory
    Press 2 for Lab
    Press 3 for Embedded
    """)
        cmd = int(input())
        if cmd == 1:
            Code= input("Enter Course Code:")
            Cat= list(map(float,(input("Enter Cats:")).split()))
            DAs= list(map(float,(input("Enter DAs:")).split()))
            FAt= float(input("Enter Fat:"))
            avg= float(input("Enter average {Enter -1 if unknown}:"))
            if avg == -1:
                std= float(input("Enter dummy grade:"))
            else:    
                std= float(input("Enter standard deviation:"))
            Ex = CourseTheory(Code,Cat,FAt,DAs,avg,std)
            Ex.Save()
            del Ex
        if cmd == 2:
            Code= input("Enter Course Code:")
            DAs= list(map(float,(input("Enter Das:")).split()))
            FAt= float(input("Enter Fat:"))
            Ex = CourseLab(Code,FAt,DAs)
            Ex.Save()
            del Ex
        if cmd == 3:
            Code= input("Enter Course Code:")
            Pat= list(map(float,(input("Enter Pats:")).split()))
            MAt= float(input("Enter Mat:"))
            FAt= float(input("Enter Fat:"))
            Ex = CourseEmbedded(Code,FAt,Pat,MAt)
            Ex.Save()
            del Ex
    if cmd==2:
        print("""
    Press 1 for Theory
    Press 2 for Lab
    Press 3 for Embedded
    """)
        cmd = int(input())
        if cmd == 1:
            ShowTable("Theory.csv")
        if cmd == 2:
            ShowTable("Lab.csv")
        if cmd == 3:
            ShowTable("Embedded.csv")
    if cmd==3:
        break
exit()