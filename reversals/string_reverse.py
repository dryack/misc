# -*- coding: utf-8 -*-
"""
Created on Mon Feb 03 11:48:43 2014

@author: dave
"""


whatever = "per vigilantia lucrum"


def reverse(str):
    string = list(str)
    j = len(string)-1
    i = 0
    while i < j:
        tmp = string[j]
        string[j] = string[i]
        string[i] = tmp
        j -= 1
        i += 1
    string = ''.join(string)
    return string


def reverse_words(str):
    string = str.split(' ')
    i = 0
    while i < len(string):
        t_string = list(string[i])
        j = len(t_string)-1
        k = 0
        while k < j:
            tmp = t_string[j]
            t_string[j] = t_string[k]
            t_string[k] = tmp
            j -= 1
            k += 1
        t_string = ''.join(t_string)
        string[i] = t_string
        i += 1
    string = ' '.join(string)
    return string

print "\nStarting string:        " + whatever
whatever = reverse(whatever)
print "Reversed string:         " + whatever
whatever = reverse(whatever)
print "Back to start:           " + whatever
whatever2 = reverse_words(whatever)
print "Words reversed in place: " + whatever2
