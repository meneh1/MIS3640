# -*- 'coding: utf-8 -*-
"""
Created on Thu Feb 18 22:24:44 2021

@author: meneh1
"""

list_number = [5, 3, 7]
print(f"This is the original number list {list_number}")
print("-" * 40, "\n")

print ("These are the expressions...")
print(list_number[2])
print(list_number[-1])
print(len(list_number))
print(list_number[0:2])
print(list_number + [2, 20, 5])
print(tuple(list_number))
print("-" * 40, "\n")

print("Replace the first value in data with its negative")
list_number[0] = list_number[0] * -1
print(list_number)

print("Add the value 10 to the end of data")
list_number.append(10)
print(list_number)

print("Insert 16 at position 2 in the data")
list_number = list_number[0:2] + [16] + list_number[2:]
print(list_number)

print("Remove the value at position 1 in data")
list_number.remove(list_number[1])
print(list_number)

print("Sort the values in data tempoarily")
print(sorted(list_number))
print("The list is normal now")
print(list_number)

print("Sort the values in data permanently")
list_number.sort()
print(list_number)

print("Changes even numbers in data to negative values")
a = 0
for a in range(len(list_number)):
    i = list_number[a]
    if i % 2 == 0:
        i = i * -1
        list_number[a] = i
        a = a + 1
    else:
        a = a + 1
print(list_number)

print("Places copies of negative values in data into a new list")
a = 0
negative_list_number = []
for a in range(len(list_number)):
    i = list_number[a]
    if i < 0:
        negative_list_number.append(i)
        a = a + 1
    else:
        a = a + 1
print(negative_list_number)


print("prints the all values in a cumulative sum of data, i.e. -5, -2, 5...")
sum_list = []
a = 0
while a < len(list_number):
    sum_list.append(list_number[a])
    a += 1
        
k = 0
while k < len(negative_list_number):
    sum_list.append(negative_list_number[k])
    k += 1
print(sum_list)
