# -*- coding: utf-8 -*-
"""Find Angle MBC.ipynb"""

'''Task-  
You are given the lengths AB and BC.
Your task is to find angle MBC in degrees.

Input Format
The first line contains the length of side AB.
The second line contains the length of side BC.

Output Format
Output angle MBC in degrees.'''

import math

ab=int(input())
bc=int(input())

ca=math.hypot(ab,bc)
mc=ca/2
bca=math.asin(1*ab/ca)
bm=math.sqrt((bc**2+mc**2)-(2*bc*mc*math.cos(bca)))
mbc=math.asin(math.sin(bca)*mc/bm)

print(int(round(math.degrees(mbc),0)),'\u00B0',sep='')

10
