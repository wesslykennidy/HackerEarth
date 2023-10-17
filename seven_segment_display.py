'''
Seven segment display.
Alice got a number written in seven segment format where each segment was created used a matchstick.

Example: If Alice gets a number 123 so basically Alice used 12 matchsticks for this number.

Alice is wondering what is the numerically largest value that she can generate by using at most the matchsticks that she currently possess.Help Alice out by telling her that number.

Output:
Print the largest possible number numerically that can be generated using at max that 
many number of matchsticks which was used to generate N.
'''

#Code
switch = {
    "1": 2,
    "2": 5,
    "3": 5,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 3,
    "8": 7,
    "9": 6,
    "0": 6
}

for _ in range(int(input())):
    n = list(str(input()))
    string_arr = list()
    for element in n:
        string_arr.append(switch.get(element))
        y = sum(string_arr)
    if y%2 == 0:
        print("1"*(y//2))
    else:
        print("7"+"1"*((y-3)//2))

#Comment: "7" has 3 stick and the maximum number can generate is 7. 