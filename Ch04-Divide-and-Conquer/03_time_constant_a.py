from datetime import datetime

def print_items_a(list):
    for item in list:
        print(item, end = ' ')

a = [2, 4, 6, 8, 10]
starttime = datetime.now().microsecond
print_items_a(a)
endtime = datetime.now().microsecond
print("\n")
print("Exec : ", endtime - starttime, " microsecond")