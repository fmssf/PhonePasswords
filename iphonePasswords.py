import random,time

f = open("/Users/willsegale/Desktop/iphonePasswords.txt","a")
Max = 999999
numlist = list(range(000000,Max))
random.shuffle(numlist)
Pass = print('\n'.join(list(map(str,numlist))),file=f)
for numlist in range(Max):
    print(Pass)
print("The ammount of passwords is :" + len(Pass))
f.close()
