import re

list1 = []


file_redukcyjny = open("plik.txt", 'r')
file_eventowy = open('mail_list.txt', 'r')


for mail in file_eventowy.readlines():
    # print(str(mail))
    list1.append(mail)


print("=============================")
for xa in list1:
    print(xa)
    #print(re.findall("^([^ ]*)", x))
print("=============================")
for x in file_redukcyjny.readlines():
    if str(x) in list1:
        print("find it!")
    else:
        print(x)