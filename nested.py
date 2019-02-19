#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

Write a program that checks whether expressions are properly nested within a line of brackets. 

"""

__author__ = "dougenas"


import sys

bracket_dict = {
    ")": "(",
    "*)": "(*",
    ">": "<",
    "}": "{",
    "]": "[" 
}

open_brackets = ['(', '(*', '<', '{', '[']


def check_brackets(expression_list):
    """Checks list of brackets for matching open brackets"""
    list3 = []
    
    for i, char in enumerate(expression_list, 1):
        if char in open_brackets:
            list3.append(char)
        elif char in bracket_dict:
            if bracket_dict[char] == list3[-1]:
                del list3[-1]
            else:
                return 'NO ' + str(i)
        else:
            continue
    
    if len(list3):
        return 'NO ' + str(len(expression_list) + 1)

    return 'YES'


def split_line(line):
    """Splits each line into individual characters (including '(*' and '*)"""
    list1 = list(line)[:-1]
    list2 = []
    length = len(list1)
    i = 0
    while i < length:
        if list1[i] == "(" and i < length - 1 and list1[i+1] == "*":
            list2.append("(*")
            i += 1
        elif list1[i] == "*" and i < length - 1 and list1[i+1] == ")":
            list2.append("*)")
            i += 1
        else:
            list2.append(list1[i])
        i += 1
    return list2


def main(filename):
    if len(sys.argv) != 2:
        print('usage: python nested_brackets.py file-to-read')
        sys.exit(1)
    file = open(filename, "r").readlines()
    for line in file:
        split = split_line(line)
        result = check_brackets(split)
        print(result)


if __name__ == '__main__':
    f = sys.argv[1]
    main(f)
