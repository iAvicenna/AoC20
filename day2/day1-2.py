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
    pos = re.findall('\d+-\d+', entry)[0]
    pos1 = int(pos.split('-')[0])
    pos2 = int(pos.split('-')[1])

    entry_remain = entry.replace(pos + ' ', '')
    letter = entry_remain[0]

    password = entry_remain.replace(letter + ': ', '')


    if (password[pos1-1] == letter and password[pos2-1] != letter) or (password[pos2-1] == letter and password[pos1-1] != letter):
        possible_passwords.append(password)

print(len(possible_passwords))