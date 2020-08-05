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

def solve(x):
    global in0, default, alpha, beta, candy
    rev = rollera
    rev2 = rollerb
    in0 = x
    if in0 == ' ':
        out2 = ' '
        print(out2)
    else:
        var = candy.index(in0)
        out0 = default[var]
        in1 = beta.index(out0)
        out1 = default[in1]
        in2 = alpha.index(out1)
        out2 = default[in2]
        print("out: ", out2)
        twist(alpha)
        if alpha[0] == rev:
            twist(beta)
            if beta[0] == rev2:
                twist(candy)

def code(x):
    global in0, default, alpha, beta, candy
    rev = rollera
    rev2 = rollerb
    in0 = x
    if in0 == ' ':
        out2 = ' '
        print(out2)
    else:
        var = default.index(in0)
        out0 = alpha[var]
        in1 = default.index(out0)
        out1 = beta[in1]
        in2 = default.index(out1)
        out2 = candy[in2]
        print("out: ", out2)
        print(alpha)
        twist(alpha)
        if alpha[0] == rev:
            twist(beta)
            if beta[0] == rev2:
                twist(candy)

def set(roller, x):
    setto = str(x)
    if setto not in roller:
        print ("roller does not contain this character")
        return
    while roller[0] != setto:
        twist(roller)

def reset():
    set(alpha, rollera)
    set(beta, rollerb)
    set(candy, rollerc)

rollera = 'd'
rollerb = 'o'
rollerc = 'g'

reset()

mess = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
coded = " "

print("In: ", mess)
for x in mess:
    code(x)
    print(beta)
    print(candy)

reset()
print("solver: ")
for x in coded:
    solve(x)