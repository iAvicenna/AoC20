#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 12:05:54 2020

@author: avicenna
"""

with open('input.txt', 'r') as file:
    lines = file.readlines()

def calculator(inputs):

    if len(inputs) == 0:
        raise ValueError('Empty operation')
    elif len(inputs) == 3:

        assert inputs[0].isnumeric() and inputs[2].isnumeric() and inputs[1] in ['*', '+', '-', '/']

        number1 = int(inputs[0])
        number2 = int(inputs[2])
        operation = inputs[1]

        if operation == '*':
            return str(number1*number2)
        elif operation == '+':
            return str(number1 + number2)
        elif operation == '/':
            return str(number1 / number2)
        elif operation == '-':
            return str(number1 - number2)


    elif '(' not in inputs and ')' not in inputs:

        while len(inputs)>1:
            if '+' not in inputs:
                inputs = [calculator(inputs[0:3])] + inputs[3:]
            else:

                ind1 = inputs.index('+')
                inputs = inputs[0:ind1-1] + [calculator(inputs[ind1-1:ind1+2])] + inputs[ind1+2:]

        return inputs[0]

    else:
        I = [ind for ind,x in enumerate(inputs) if x=='(' or x==')']
        sum_val = 0
        for i in I:
            if inputs[i] == '(':
                sum_val += 1
            else:
                sum_val -= 1

            if sum_val == 0:
                ind1 = I[0]
                ind2 = i
                break

        assert ind1<ind2, 'Unclosed paranthesis'

        return calculator(inputs[0:ind1] + [calculator(inputs[ind1+1:ind2])] + inputs[ind2+1:])

sum_val = 0
for line in lines:

    line = line.replace('\n','')
    inputs = line.replace('(', '( ')
    inputs = inputs.replace(')', ' )')
    sum_val += int(calculator(inputs.split(' ')))

