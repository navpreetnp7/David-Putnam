#!/usr/bin/env python
# coding: utf-8

"""
        Code Submitted By
        Navpreet Singh
        ns4767
"""

import copy


def dpll(cs, b):

    while (True):
        if len(cs) == 0:
            return b
        if emptyClause(cs):
            return "Fail"
        if easyCaseIn(cs):
            cs, b = easyCase(cs, b)
        else:
            break

    cscopy = copy.deepcopy(cs)
    bcopy = copy.deepcopy(b)
    p = cs[0][0]
    cscopy, bcopy = propogate(cscopy, bcopy, p, 1)
    answer = dpll(cscopy, bcopy)
    if answer != "Fail":
        return answer
    cs, b = propogate(cs, b, -1 * p, 1)
    return dpll(cs, b)


# Check if clause is empty

def emptyClause(cs):
    if cs[0]==[]:
        return True
    else:
        return False


# Check the easy cases, singleton clause or pure literal

def easyCaseIn(cs):
    for c in cs:
        if len(c)==1:
            return True
    dict = {}
    for c in cs:
        for p in c:
            dict[p]=1
    for p in dict:
        if -1*p not in dict:
            return True
    return False


# Propogating with a given p=T/F value of a propositional atom by deleting entire clause if p
# or removing the atom p within a clause if -p

def propogate(cs, b, a, v):
    b.append([a, v])
    cs1 = copy.deepcopy(cs)

    for c in range(len(cs1)):
        if -1 * a * v in cs1[c]:
            cs1[c].remove(-1 * a * v)

    for c in cs1:
        if c == []:
            return [[]], b

    for c in range(len(cs)):
        if a * v in cs[c]:
            cs1.remove(cs[c])
    return cs1, b


# Propogate the easy cases, singleton clause or pure literal

def easyCase(cs,b):
    for c in cs:
        if len(c)==1:
            return propogate(cs,b,c[0],1)
    dict = {}
    for c in cs:
        for p in c:
            dict[p]=1
    for p in dict:
        if -1*p not in dict:
            return propogate(cs,b,p,1)