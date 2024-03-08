#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:57:15 2024

@author: Yuanhang Peng
"""

# Initialize a list
sentence = []

# Creating loop
while True: 
    print("What sentence you want to put?")
    sen = input()
    sentence.append(sen)
    print("Do you want to continue to input something?")
    decision = input()
    if decision == "no":
        break

# Ask user to input subset order
sentence_subset = int(input("Which sentence do you want to get? "))
word_subsrt = int(input("Which word you want to get? "))
word = sentence[sentence_subset].split()[word_subsrt]

# Print the output
result = word.center(20, "*")
print(result)
