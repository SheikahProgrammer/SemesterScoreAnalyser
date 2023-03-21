from CourseDef import *
from TableView import *
while True:
    print("""
    Press 1 for insertion of data
    Press 2 for viewing data
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
            Cat= eval(input("Enter Cats:"))
            DAs= eval(input("Enter DAs:"))
            FAt= int(input("Enter Fat:"))
            Ex = CourseTheory(Code,Cat,FAt,DAs)
            Ex.Save()
            del Ex
        if cmd == 2:
            Code= input("Enter Course Code:")
            DAs= eval(input("Enter DAs:"))
            FAt= int(input("Enter Fat:"))
            Ex = CourseLab(Code,FAt,DAs)
            Ex.Save()
            del Ex
        if cmd == 3:
            Code= input("Enter Course Code:")
            Pat= eval(input("Enter Pats:"))
            MAt= int(input("Enter Mat:"))
            FAt= int(input("Enter Fat:"))
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