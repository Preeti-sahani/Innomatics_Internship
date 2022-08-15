# -*- coding: utf-8 -*-
"""Triangle Quest 2.ipynb"""
'''Task-  
You are given a positive integer N.
Your task is to print a palindromic triangle of size N.
For example, a palindromic triangle of size 5 is:
1
121
12321
1234321
123454321'''

for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((pow(10,i)//9)**2)

