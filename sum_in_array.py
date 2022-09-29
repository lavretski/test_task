# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:22 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants


Test task
"""

def for_in_for(arr:list, S:int) -> list:#speed O(n^2)
    for i in range(len(arr)):           #memory O(1)
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == S:
                return [arr[i], arr[j]]
    return [-1]

def two_pointers(arr:list, S:int) -> list:#speed O(n)
    i = 0                                 #memory O(1)
    j = len(arr) - 1
    while (i < j):
        if (arr[i] + arr[j] == S):
            return [arr[i], arr[j]]
        elif (arr[i] + arr[j] < S):
            i += 1
        else:
            j -= 1
    return [-1]

def hashMap(arr, S) -> list: #speed O(n)
    d = {}                   #speed O(n)
    for i in range(len(arr)):
        diff = S - arr[i]
        if diff in d:
            return [arr[d[diff]], arr[i]]
        else:
            d[arr[i]] = i
    return [-1]

print(for_in_for([0, 19, 34, 500], 500))
print(two_pointers([0, 1, 2, 3, 14], 15))
print(hashMap([-100, 1, 7, 14], -86))

#who is better depends on whether speed or memory is more important to me
#But in general two_pointers is better
#Find the most optimal algorithm for speed and memory -
#it is impossible to prove that some algorithm is the most optimal



