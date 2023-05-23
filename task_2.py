nums = [1, 5, 10, 25, 100]
target = int(input("target = "))
llist = []
for i in nums[::-1]:
    if(target >= i):
        target -= i
        llist.append(i)
        while(target >= 0) and (target >= i):
            llist.append(i)
            target -= i
print(llist[::-1])