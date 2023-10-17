'''
Bob has a playlist of N songs, each song has a singer associated with it (denoted by an integer)

Favourite singer of Bob is the one whose songs are the most on the playlist

Count the number of Favourite Singers of Bob
'''

# Code
n = int(input())
arr = list(map(int,input().split()))
element_count = {}
for element in arr:
    if element in element_count:
        element_count[element] +=1
    else:
        element_count[element] = 1

max_frequency = max(element_count.values())
element_max_frequency = [element for element,frequency in element_count.items() if frequency == max_frequency]
print(len(element_max_frequency))

