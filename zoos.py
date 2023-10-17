'''
Problem:
You are required to enter a word that consists of x and y 
that denote the number of Zs and Os respectively. The input word is considered similar to word zoo if 
 2 x \x  = y.
'''
#Code
n = input().lower()
x = n.count("z")
y = n.count("o")
if "zoo" in n and 2*x == y:
    value = "Yes"
else:
    value = "No"

print(value)