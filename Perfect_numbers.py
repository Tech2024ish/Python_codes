def perfect_num(num):
    return num==sum(i for i in range (1, num) if num %i==0)
for num in range (2,1000000):
    if perfect_num(num ):
        print (num)