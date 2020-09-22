
phone = dict()
for i in range(int(input())):
    line = input().split(" ")
    phone[line[0]] = phone.get(line[0],line[1])

while 1:
    try:
        search = input()
        if search in phone:
            print(str(search) + "=" + str(phone[search]))
        else:
            print("Not found")
    except:
        break
