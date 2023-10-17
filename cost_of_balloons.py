'''
You are conducting a contest at your college. This contest consists of two problems and n participants. You know the problem that a candidate will solve during the contest.

You provide a balloon to a participant after he or she solves a problem. There are only green and purple-colored balloons available in a market. Each problem must have a balloon associated with it as a prize for solving that specific problem. You can distribute balloons to each participant by performing the following operation:

Use green-colored balloons for the first problem and purple-colored balloons for the second problem
Use purple-colored balloons for the first problem and green-colored balloons for the second problem
You are given the cost of each balloon and problems that each participant solve. Your task is to print the minimum price that you have to pay while purchasing balloons
'''

#Code
for _ in range (int(input())):
    cost = sorted(list(map(int,input().split())), reverse= True)
    n = int(input())
    sum_value1, sum_value2 = 0,0
    for i in range(n):
        element1, element2 = map(int,input().split())
        sum_value1 += element1
        sum_value2 +=element2

    result = sum(x*y for x,y in zip(cost,sorted([sum_value1, sum_value2])))
    print(result)