#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:44:28 2020

@author: avicenna
"""

EYE_COLOURS = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
REQUIRED_KEYS = set(['byr','iyr','eyr','hgt','hcl','ecl','pid'])
ALL_KEYS = set(['cid', 'byr','iyr','eyr','hgt','hcl','ecl','pid'])

class Passport():

    def __init__(self, entry):
        entry = entry.replace('\n', ' ')[0:-1]
        fields = entry.split(' ')

        self.data = {}

        for field in fields:
            key = field[0:3]
            value = field[4:]
            assert key in ALL_KEYS, f'key {key} of passport {entry} not valid'
            self.data[key.upper()] = value

    def check_fields(self):
        if all(x.upper() in list(self.data.keys()) for x in REQUIRED_KEYS):
            return 1
        else:
            return 0

    def check(self):

        is_correct = 1

        if self.check_fields():
            byr_val = self.data['BYR']
            iyr_val = self.data['IYR']
            eyr_val = self.data['EYR']
            hgt_val = self.data['HGT']
            hcl_val = self.data['HCL']
            ecl_val = self.data['ECL']
            pid_val = self.data['PID']

            try:
                byr_val = int(byr_val)
                assert byr_val >= 1920 and byr_val <= 2002
            except:
                is_correct = 0

            try:
                iyr_val = int(iyr_val)
                assert iyr_val >= 2010 and iyr_val <= 2020
            except:
                is_correct = 0

            try:
                eyr_val = int(eyr_val)
                assert eyr_val >= 2020 and eyr_val <= 2030
            except:
                is_correct = 0

            if 'cm' in hgt_val:
                height = hgt_val.replace('cm','')

                try:
                    height = int(height)
                    assert height >= 150 and height <= 193
                except:
                    is_correct = 0

            elif 'in' in hgt_val:
                height = hgt_val.replace('in','')

                try:
                    height = int(height)
                    assert height >= 59 and height <= 76
                except:
                    is_correct = 0
            else:
                is_correct = 0

            try:
                assert hcl_val[0] == '#'
                assert hcl_val[1:].isalnum()
                assert len(hcl_val) == 7
            except:
                is_correct = 0

            try:
                assert len(ecl_val) == 3
                assert ecl_val in EYE_COLOURS
            except:
                is_correct = 0

            try:
                assert pid_val.isnumeric()
                assert len(pid_val)==9
                pid_val = int(pid_val)

            except:
                is_correct = 0

        else:
            is_correct = 0

        return is_correct

with open('input.txt','r') as file:
    lines = file.readlines()

found_fields = []

I = [-1] + [ind for ind,line in enumerate(lines) if line =='\n'] + [len(lines)]
passport_text = [''.join(lines[i+1:j]) for i,j in zip(I[0:-1],I[1:])]

valid_passport_count = 0
passports = []
for passport_entry in passport_text:

    passports.append(Passport(passport_entry))
    valid_passport_count += passports[-1].check()

