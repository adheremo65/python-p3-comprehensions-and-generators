#!/usr/bin/env python3

def return_evens(num_list):
    x = []
    for n in num_list:
        if n%2 ==0:
            x.append(n)
    return x
    

def make_exclamation(sentence_list):
    y = []
    for i in sentence_list:
        y.append(i + "!")
    return y


    pass