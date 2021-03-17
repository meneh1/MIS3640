# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 22:56:04 2021

@author: meneh1
"""

with open("desolation_row.txt" , "r") as file:
    text = file.read().split()
print(text)

for i in range(len(text)):
    text[i] = text[i].lower()
print()

no_punc = []
punctuations ='''!()-[]{}:;'"\,<>./?@#$%^&*_~'''
for word in text:
    for j in word:
        if j in punctuations:
            word = word.replace(j,"")
    no_punc.append(word)
print(no_punc)

d = {}
for key in no_punc:
    d[key] = d.get(key, 0)+1
print(d)

d_val = sorted(d.values(), reverse=_True)
d_sorted = {}
for i in d_val:
    for k in d.keys():
        if d[k] == i:
            d_sorted[k] = d[k]
            break
print(d_sorted)

print(sum(d_val))

dist_sum = 0 
for k in d:
    dist_sum += 1
print(dist_sum)

print(dist_sum/sum(d_val))