from datetime import datetime
from time import sleep

def print_items_b(list):
    for item in list:
        sleep(1)
        print(item, end = ' ')

starttime = datetime.now().microsecond
a = [2, 4, 6, 8, 10]
print_items_b(a)
endtime = datetime.now().microsecond
print("\n")
print("Exec : ", endtime - starttime, " microsecond")