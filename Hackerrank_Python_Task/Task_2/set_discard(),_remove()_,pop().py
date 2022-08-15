# -*- coding: utf-8 -*-
"""Set-discard(), remove() ,pop().ipynb
"""

'''Task- 
You have a non-empty set s, and you have to execute N commands given in N lines.
The commands will be pop, remove and discard.

Input Format:

The first line contains integer N, the number of elements in the set s.
The second line contains N space separated elements of set s. 
All of the elements are non-negative integers, less than or equal to 9.
The third line contains integer N, the number of commands.
The next N lines contains either pop, remove and/or discard commands followed by their associated value..'''

n = int(input())
s = set(map(int, input().split()))

N = int(input())

for i in range(N):
    cmd = input().split()
    if cmd[0] == 'pop':
        s.pop()
    if cmd[0] == 'remove':
        s.remove(int(cmd[1]))
    if cmd[0] == 'discard':
        s.discard(int(cmd[1]))

result = 0
for i in s:
    R = result+i;

print(R)

p
