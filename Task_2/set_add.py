# -*- coding: utf-8 -*-
"""Set-add.ipynb"""

'''Task- 
Apply your knowledge of the .add() operation to help your friend Rupal.
Rupal has a huge collection of country stamps. 
She decided to count the total number of distinct country stamps in her collection. S
he asked for your help. You pick the stamps one by one from a stack of N country stamps.
Find the total number of distinct country stamps.


Input Format :
The first line contains an integer N, the total number of country stamps.
The next N lines contains the name of the country where the stamp is from.

Output Format :
Output the total number of distinct country stamps on a single line.'''

n = int(input())
s1 = set()
for i in range(n):
    s1.add(input())
print(len(s1))

