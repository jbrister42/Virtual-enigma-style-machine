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
        out = get_key(in0)
        out0 = alpha[default.index(out)]
        out1 = beta[default.index(out0)]
        out2 = candy[default.index(out1)]
        outref = default[25 - default.index(out2)] # reflector
        var = candy.index(outref)
        out3 = default[var]
        out4 = default[beta.index(out3)]
        out5 = default[alpha.index(out4)]
        outfinal = get_key(out5)
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
        out = plugboard[in0]
        out0 = alpha[default.index(out)]
        out1 = beta[default.index(out0)]
        out2 = candy[default.index(out1)]
        #print(out2)
        outref = default[25 - default.index(out2)] # reflector 
        #print(outref)
        out3 = default[candy.index(outref)]
        out4 = default[beta.index(out3)]
        out5 = default[alpha.index(out4)]
        #print(out5)
        outfinal = plugboard[out5]
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

plugboard = {'a':'u', # Manually set plugboard settings
             'b':'l',
             'c':'x',
             'd':'e',
             'e':'k',
             'f':'i',
             'g':'j',
             'h':'d',
             'i':'a',
             'j':'q',
             'k':'c',
             'l':'h',
             'm':'v',
             'n':'f',
             'o':'m',
             'p':'z',
             'q':'o',
             'r':'w',
             's':'p',
             't':'g',
             'u':'n',
             'v':'b',
             'w':'r',
             'x':'s',
             'y':'y',
             'z':'t'}

rollera = 'r' # set "initial position" for roller 1
rollerb = 'a' # set "initial position" for roller 2
rollerc = 't' # set "initial position" for roller 3

reset()

message = "Percy Raisin Badger" # Put message to be coded here
coded_message = "jgixt ttwufj yflnwe" # Put message to be decoded here

send()