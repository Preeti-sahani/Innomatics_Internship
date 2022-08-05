# -*- coding: utf-8 -*-
"""String Validators.ipynb"""

'''Task-  
You are given a string S.
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
In the second line, print True if S has any alphabetical characters. Otherwise, print False.
In the third line, print True if S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.'''

if __name__ == '__main__':
    s = input()
    print(any([i.isalnum() for i in s]))   
    print(any([i.isalpha() for i in s]))     
    print(any([i.isdigit() for i in s]))               
    print(any([i.islower() for i in s]))         
    print(any([i.isupper() for i in s]))
