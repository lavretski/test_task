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

# def lucky_2(seq):
#     lucky = ""
#     while True:
#         index_5 = seq.find("5")
#         index_6 = seq.find("6")
#         if index_5 == -1:
#             if index_6 == -1:
#                 break
#             else:
#                 index = index_6
#         else:
#             index = min([index_5,index_6]) if index_6 != -1 else index_5
#         lstring = ""
#         count5 = 0
#         count6 = 0
#         while(index<=len(seq)):
#             if(seq[index]=="5"):
#                 count5+=1
#                 lstring+=seq[index]
#             elif(seq[index]=="6"):
#                 count6+=1
#                 lstring+=seq[index]
#             else:
#                 break
#             index+=1
#         if len(lstring)>=len(lucky) and count5>0 and count6> 0:
#             lucky = lstring
#         seq=seq[index:]
#         return lucky if lucky != '' else 0

print(lucky_1('6'))
print(lucky_1('66666666'))
print(lucky_1('66666666666635'))