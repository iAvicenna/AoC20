#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:44:28 2020

@author: avicenna
"""
import re

REQUIRED = set(['byr','iyr','eyr','hgt','hcl','ecl','pid'])


with open('input.txt','r') as file:
    lines = file.readlines()

found_fields = []


I = [-1] + [ind for ind,line in enumerate(lines) if line =='\n'] + [len(lines)]

passports = [''.join(lines[i+1:j]) for i,j in zip(I[0:-1],I[1:])]


valid_passport_count = 0
invalid_passport_count = 0
valid_fields = []
for passport in passports:

    passport = passport.replace('\n',' ')[0:-1]
    fields = passport.split(' ')

    if all(x+':' in passport for x in REQUIRED):
        valid_passport_count += 1
    else:
        invalid_passport_count += 1


assert valid_passport_count + invalid_passport_count == len(passports)

