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
        return(out2)
    else:
        out0 = alpha[default.index(in0)]
        out1 = beta[default.index(out0)]
        out2 = candy[default.index(out1)]
        outref = default[25 - default.index(out2)] # reflector
        var = candy.index(outref)
        out3 = default[var]
        out4 = default[beta.index(out3)]
        out5 = default[alpha.index(out4)]
        # alternatively : out5 = default[alpha.index(default[beta.index(default[candy.index(default[25 - default.index(out2)])])])]
        twist(alpha)
        if alpha[0] == rev:
            twist(beta)
            if beta[0] == rev2:
                twist(candy)
        return(out5)

def code(x):
    global in0, default, alpha, beta, candy
    rev = rollera
    rev2 = rollerb
    in0 = x
    if in0 == ' ':
        out2 = ' '
        return(out2)
    else:
        out0 = alpha[default.index(in0)]
        out1 = beta[default.index(out0)]
        out2 = candy[default.index(out1)]
        outref = default[25 - default.index(out2)] # reflector 
        out3 = default[candy.index(outref)]
        out4 = default[beta.index(out3)]
        out5 = default[alpha.index(out4)]
        twist(alpha)
        if alpha[0] == rev:
            twist(beta)
            if beta[0] == rev2:
                twist(candy)
        return(out5)

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

rollera = 'r' # set "initial position" for roller 1
rollerb = 'a' # set "initial position" for roller 2
rollerc = 't' # set "initial position" for roller 3

reset()

message = "Percy Raisin Badger" # Put message to be coded here
coded_message = "qzkxz etjxfy ihcxxi" # Put message to be decoded here


messy = ""
solvy = ""

for x in message.lower():
    messy += code(x)    
reset()
for x in coded_message.lower():
    solvy += solve(x)

print("In: ", message)
print("Coded message:", messy)
print("Message to decode:", coded_message)
print("Decoded message:", solvy)