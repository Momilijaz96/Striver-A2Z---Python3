#problem: https://www.codingninjas.com/codestudio/problems/pair-sum_697295?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=1from os import *
from sys import *
from collections import *
from math import *
from itertools import combinations

def pairSum(arr, s):
    # Write your code here.
    arr.sort(reverse=True)
    
    count_arr = Counter(arr)
    hmap = {k:(None,count_arr[k]) for k in arr}
    pairs = []
    for k in hmap:
        if s-k==k:
            pc = len(list(combinations([k]*count_arr[k],2)))
            hmap[k] = (s-k,pc)
        if s-k in hmap and hmap[s-k][0]!=k:
            hmap[k] = (s-k,hmap[k][1]*hmap[s-k][1])
    
    for k in hmap:
        if hmap[k][0]:
            pairs += [sorted((s-k,k))]*hmap[k][1]
    pairs = sorted(pairs)
    return pairs

        