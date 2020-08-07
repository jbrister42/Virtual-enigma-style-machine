# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 20:10:40 2020

@author: jbris
"""
import string
import random

default = list(string.ascii_lowercase)
alpha = list(string.ascii_lowercase)
beta = list(string.ascii_lowercase)
candy = list(string.ascii_lowercase)
filler = list(string.ascii_lowercase)

#for x in default:              # < for generating a random plugboard
#    z = random.choice(filler)
#    while z == x:
#        z = random.choice(filler)
#    plugboard[x] = z
#    filler.remove(z)

def get_key(val):
    for key, value in plugboard.items():
        if val==value:
            return key

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
        if in0 in plugboard.values():
            out = get_key(in0)
        else:
            out = plugboard[in0]
        out0 = alpha[default.index(out)]
        out1 = beta[default.index(out0)]
        out2 = candy[default.index(out1)]
        outref = default[25 - default.index(out2)] # reflector
        var = candy.index(outref)
        out3 = default[var]
        out4 = default[beta.index(out3)]
        out5 = default[alpha.index(out4)]
        if out5 in plugboard.values():
            outfinal = get_key(out5)
        else:
            outfinal = plugboard[out5]
        # alternatively : out5 = default[alpha.index(default[beta.index(default[candy.index(default[25 - default.index(out2)])])])]
        twist(alpha)
        if alpha[0] == rev:
            twist(beta)
            if beta[0] == rev2:
                twist(candy)
        return(outfinal)

def code(x):
    global in0, default, alpha, beta, candy
    rev = rollera
    rev2 = rollerb
    in0 = x
    if in0 == ' ':
        out2 = ' '
        return(out2)
    else:
        if in0 in plugboard:
            out = plugboard[in0]
        else:
            out = get_key(in0)
        out0 = alpha[default.index(out)]
        out1 = beta[default.index(out0)]
        out2 = candy[default.index(out1)]
        #print(out2)
        outref = default[25 - default.index(out2)] # reflector 
        #print(outref)
        out3 = default[candy.index(outref)]
        out4 = default[beta.index(out3)]
        out5 = default[alpha.index(out4)]
        if out5 in plugboard:
            outfinal = plugboard[out5]
        else:
            outfinal = get_key(out5)
        twist(alpha)
        if alpha[0] == rev:
            twist(beta)
            if beta[0] == rev2:
                twist(candy)
        return(outfinal)

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

def send():
    messy = ""
    solvy = ""
    reset()
    for x in message.lower():
        messy += code(x)    
    reset()
    for x in coded_message.lower():
        solvy += solve(x)
    print("In: ", message)
    print("Coded message:", messy)
    print("")
    print("Message to decode:", coded_message)
    print("Decoded message:", solvy)
    print('')
    print("Plugboard settings: ", plugboard)
    print("Roller A initial position: ", rollera)
    print("Roller B initial position: ", rollerb)
    print("Roller C initial position: ", rollerc)

def rand_plugboard():
    plugboard.clear()
    alp = list(string.ascii_lowercase)
    while alp:
        a = random.choice(alp)
        alp.remove(a)
        b = random.choice(alp)
        alp.remove(b)
        plugboard[a] = b
        
def check_plugboard():
    checker = []
    for x in plugboard:
        checker.append(x)
    for x in plugboard.values():
        checker.append(x)
    check = []
    for x in default:
        counter = 0
        for y in checker:
            if x == y:
                counter += 1
        check.append(counter)
    if all(i == 1 for i in check):
        send()
    else:
        return(print("Invalid plugboard setting"))

plugboard = {'k': 't', 's': 'i', 'f': 'p', 'o': 'n', 'b': 'v', 'c': 'x', 'a': 'l', 'e': 'g', 'r': 'q', 'w': 'd', 'm': 'j', 'h': 'u', 'y': 'z'}
# to be physically valid, all letters must appear exactly once as either a key or a value
rollera = 'p' # set "initial position" for roller 1
rollerb = 'j' # set "initial position" for roller 2
rollerc = 'x' # set "initial position" for roller 3

message = "Percy raisin badger kaiser tyki dolly darcy" # Put message to be coded here
coded_message = 'gvfex mjwayv ilowyo snpoov pnif mrvyz ysvin' # Put message to be decoded here

#rand_plugboard() # This will generate a random, physically valid plugboard combination (replacing the manually input combination shown above)
check_plugboard() # This checks if the plugboard combination is physically possible and executes the main loop
