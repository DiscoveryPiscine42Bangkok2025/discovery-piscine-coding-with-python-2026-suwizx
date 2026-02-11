#!/usr/bin/env python3

numbers = [2, 8, 9, 48, 8, 22, -12, 2]
result = set()

for i in numbers:
    if(i>5):
        result.add(i+2)    

print(result)