#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:56:22 2020

@author: avicenna
"""
import re

with open('input.txt','r') as f:
    entries = f.readlines()

possible_passwords = []

for entry in entries:
    rrange = re.findall('\d+-\d+', entry)[0]
    minr = int(rrange.split('-')[0])
    maxr = int(rrange.split('-')[1])

    entry_remain = entry.replace(rrange + ' ', '')
    letter = entry_remain[0]

    password = entry_remain.replace(letter + ': ', '')


    if password.count(letter) >= minr and password.count(letter) <= maxr:
        possible_passwords.append(password)

print(len(possible_passwords))