# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 20:10:40 2020

@author: jbris
"""
import string

default = list(string.ascii_lowercase)
alpha = list(string.ascii_lowercase)
beta = list(string.ascii_lowercase)
candy = list(string.ascii_lowercase)

def twist(roller):
    roller.append(roller[0])
    roller.remove(roller[0])
    return roller

def atwist(roller):
    pos = len(roller)
    dummy = roller[pos-1]
    for x in roller:
        roller[pos-1] = roller[pos-2]
        pos -= 1
    roller[0] = dummy
    return roller

#print(beta)
#atwist(beta)
#print(beta)
in0 = ""

def solve():
    global in0, default, alpha, beta, candy
    rev = alpha[0]
    rev2 = beta[0]
    while in0 != "end":
        in0 = input("IN: ").lower()
        var = candy.index(in0)
        out0 = default[var]
        in1 = beta.index(out0)
        out1 = default[in1]
        in2 = alpha.index(out1)
        out2 = default[in2]
        print("out: ", out2)
        print(alpha)
        print(beta)
        print(candy)
        twist(alpha)
        if alpha[0] == rev:
            twist(beta)
            if beta[0] == rev2:
                twist(candy)

def code():
    global in0, default, alpha, beta, candy
    rev = alpha[0]
    rev2 = beta[0]
    while in0 != "end":
        in0 = input("IN: ").lower()
        var = default.index(in0)
        out0 = alpha[var]
        in1 = default.index(out0)
        out1 = beta[in1]
        in2 = default.index(out1)
        out2 = candy[in2]
        print("out: ", out2)
        print(alpha)
        print(beta)
        print(candy)
        twist(alpha)
        if alpha[0] == rev:
            twist(beta)
            if beta[0] == rev2:
                twist(candy)

def set(roller):
    setto = ""
    while len(setto) != 1:
        setto = input("Choose the initial setting for roller").lower()
    if setto not in roller:
        print ("roller does not contain this character")
        return
    while roller[0] != setto:
        twist(roller)
    print(roller)

set(alpha)
set(beta)
set(candy)

imp = int(input("Press 1 for code, 2 for solve"))

if imp == 1:
    code()
elif imp == 2:
    solve()
else:
    print("Press 1 or 2")

