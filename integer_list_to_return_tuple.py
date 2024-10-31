def list_of_integers(num):
    even_sum=0
    odd_sum=0
    my_tuple=()
    for i in num:
        if i%2==0:
            even_sum+=i
        else:
            odd_sum+=i
        my_tuple=even_sum,odd_sum
    return my_tuple
num=[1,2,3,4,5,6,7,8,9,10,11]
result=list_of_integers(num)
print(result)
