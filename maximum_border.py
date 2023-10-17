'''
You are given a table with n rows and m columns. Each cell is colored with white or black. Considering the shapes created by black cells, what is the maximum border of these shapes? Border of a shape means the maximum number of consecutive black cells in any row or column without any white cell in between.

A shape is a set of connected cells. Two cells are connected if they share an edge. Note that no shape has a hole in it.
'''
#Code #1
for _ in range(int(input())):
    n, m = map(int,input().split())
    max_value = 0
    for i in range(n):
        arr = input().strip()
        value = arr.count("#")
        max_value = max(value,max_value)
    print(max_value)
# Time (sec) : .04215

# Code #2 
for _ in range(int(input())):
    n,m = map(int,input().split())
    value = list()
    for i in range(n):
        arr = list(input())
        value.append(arr.count ("#"))
    print (max(value))
# Time (sec): .08258
