'''
You are provided an array A of size N that contains non-negative integers. 
Your task is to determine whether the number that is formed by selecting the last digit of all the N numbers is divisible by 10.
'''

#Code
n = int(input())
arr = map(int,input().split())
remainder = [str(element%10) for element in arr]
number = int(''.join(remainder))
if number%10 == 0:
    print("Yes")
else:
    print("No")