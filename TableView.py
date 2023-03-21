from prettytable import from_csv
def ShowTable(file):
    with open(file) as fp:
        mytable = from_csv(fp)
        print(mytable)
