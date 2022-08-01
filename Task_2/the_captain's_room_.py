# -*- coding: utf-8 -*-
"""The Captain's Room\.ipynb"""

'''Task- 

Mr. Anant has an unordered list of randomly arranged room entries. 
The list consists of the room numbers for all of the tourists. The room numbers will appear
K times per group except for the Captain's room.
Mr. Anant needs you to help him find the Captain's room number.
The total number of tourists or the total number of groups of families is not known to you.
You only know the value of K and the room number list.

Input format :
The first line consists of an integer, K, the size of each group.
The second line contains the unordered elements of the room number list.

Output Format :
Output the Captain's room number.

'''

k =int(input())
lt  = list(map(int,input().split()))

s1 = set()  #unique room
s2 = set()  #room appear more than one

for i in lt:
    if i in s1:
        s2.add(i)
    else:
        s1.add(i)
        
s = s1.difference(s2)
print(*s)

