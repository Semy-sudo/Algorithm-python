#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    ans = 0
    mins = [sys.maxsize,sys.maxsize]
    data = reversed(list(enumerate(q,1)))#q리스트를 인덱스 1부터 시작해서 같이 나열, 뒤집기
    for i,p in data:
        #이동 해야 하는 경우
        if p-i>2:
            print('Too chaotic')
            return
        elif p>mins[1]:
            ans+=2
        elif p>mins[0]:
            ans+=1
        
        #이동 안해도 되는 경우
        if p<mins[0]:
            mins = (p,mins[0])
        elif p<mins[1]:
            mins = (mins[0],p)
            
    print(ans)
        
        
        

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
