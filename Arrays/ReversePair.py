#Problem link: https://www.codingninjas.com/codestudio/problems/1112652?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=1
from os import *
from sys import *
from collections import *
from math import *

def merge_sort(arr,inv_count):
    n = len(arr)
    if n<2:
        return arr,inv_count
    mid = ceil(n//2)
    left,inv_count = merge_sort(arr[:mid],inv_count)
    right,inv_count = merge_sort(arr[mid:],inv_count)
    return merge(left,right,inv_count)


def merge(left,right,inv_count):
    res = []
    while(left and right):
        if left[0]>right[0]:
            if check_inv(left[0],right[0]):
                inv_count += len(left)
            else:
                idx=0
                while(idx<len(left)):
                    if check_inv(left[idx],right[0]):
                        inv_count += len(left[idx:])
                        break
                    idx+=1
            res.append(right.pop(0))
        else:
            res.append(left.pop(0))
    if left:
        res += left
    elif right:
        res += right
    return res, inv_count

def check_inv(a,b):
    return a>(2*b)


def reversePairs(arr, n):
    # Write your code here.
    res,inv_count = merge_sort(arr,0)
    return inv_count
