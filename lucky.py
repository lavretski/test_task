# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 12:59:51 2022

@author: Okhrimchuk Roman & Maksym Veremchuk
for Sierentz Global Merchants
Test task
"""

def lucky_1(seq: str) -> bool:
    luckiest = ''
    possibly_lucky = ''
    for i in range(len(seq)):
        if seq[i] in ['5', '6'] and i != len(seq) - 1:
            possibly_lucky += seq[i]
        else:
            if i == len(seq) - 1:
                possibly_lucky = possibly_lucky + seq[i]
            if len(possibly_lucky) > len(luckiest) and (possibly_lucky.replace(possibly_lucky[0], '') != '' or len(possibly_lucky) == 1):
                luckiest = possibly_lucky
            possibly_lucky = ''
    return luckiest if luckiest != '' else 0

print(lucky_1('6'))
print(lucky_1('66666666'))
print(lucky_1('66666666666635'))