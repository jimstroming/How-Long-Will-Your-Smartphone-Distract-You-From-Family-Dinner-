"""
From http://fivethirtyeight.com/features/can-you-slay-the-puzzle-of-the-monsters-gems/

A video game requires you to slay monsters to collect gems. Every time you slay a monster, 
it drops one of three types of gems: a common gem, an uncommon gem or a rare gem. 
The probabilities of these gems being dropped are in the ratio of 3 to 2 to 1. Three common 
gems for every two uncommon gems for every one rare gem, on average. If you slay monsters
until you have at least one of each of the three types of gems, how many of the most 
common gems will you end up with, on average?
"""


"""
Let's try a python simulation

"""

import random

def findgems():

    probgems   = [0,0,0,1,1,2]
    weightgem  = [1, 0, 0]
    numbergems = [0, 0, 0]
    
    while (numbergems[0]*numbergems[1]*numbergems[2] == 0):
        gem = random.choice(probgems)  
        numbergems[gem] += 1

    return numbergems[0]


loopcount = 10000000
sum = 0
for x in range(0, loopcount):
    sum += findgems()
print float(sum)/loopcount

"""
probabilities of gems
common   = 1/2 
uncommon = 1/3 
rare     = 1/6


There are 6, length 3 solutions
CUR 1 common, p = 1/36, e = 1/36
CRU 1 common, p = 1/36, e = 1/36
UCR 1 common, p = 1/36, e = 1/36
URC 1 common, p = 1/36, e = 1/36
RCU 1 common, p = 1/36, e = 1/36
RUC 1 common, p = 1/36, e = 1/36
total expected value      = 1/6   for length 3 solutions

CCUR 2 common, p = 1/72, e = 1/36
CCRU 2 common, p = 1/72, e = 1/36
CUCR 2 common, p = 1/72, e = 1/36 
CRCU 2 common, p = 1/72, e = 1/36
UCCR 2 common, p = 1/72, e = 1/36
RCCU 2 common, p = 1/72, e = 1/36

CUUR 1 common, p = 1/108, e = 1/108
UCUR 1 common, p = 1/108, e = 1/108
UUCR 1 common, p = 1/108, e = 1/108
UURC 1 common, p = 1/108, e = 1/108
URUC 1 common, p = 1/108, e = 1/108
RUUC 1 common, p = 1/108, e = 1/108

CRRU 1 common, p = 1/216, e = 1/216
RRUC 1 common, p = 1/216, e = 1/216
URRC 1 common, p = 1/216, e = 1/216
RCRU 1 common, p = 1/216, e = 1/216
RURC 1 common, p = 1/216, e = 1/216
RRCU 1 common, p = 1/216, e = 1/216

CCCC
CCCU
CCCR

CCUC
CCUU

CCRC
CCRR

CUCC
CUCU

CUUC
CUUU

CRCC
CRCR

CRRC
CRRR

UCCC
UCCU

UCUC
UCUU

UUCC
UUCU

UUUC
UUUR
UUUU

UURR
UURU

URUR
URUU

URRR
URRU

RCCC
RCCR

RCRC
RCRR

RUUR
RUUU

RURR
RURU

RRCC
RRCR

RRUR
RRUU

RRRC
RRRR
RRRU

"""

"""
Too brute force.

Let's try to simplify. 
What if we only consider cases that end in R.
By substituting gems, we should be able to change these into cases that end in C and 
into cases that end in U.

CUR
UCR

CCUR
CUCR
CUUR
UCCR
UCUR
UUCR

CCCUR
CCUCR
CCUUR
CUCCR
CUCUR
CUUCR
CUUUR
UCCCR
UCCUR
UCUCR
UCUUR
UUCCR
UUCUR
UUUCR

"""

"""

Simplify again.
Cases that start with C, end in R.


CUR

CCUR
CUCR

CCCUR
CCUCR
CCUUR
CUCCR
CUCUR
CUUCR
CUUUR  

"""

"""
Another simplification.
Lets do a case with gem A,B, and C,
where P(A)=P(B)=P(C)=1/3
Cases starting with A, ending with C

A B   C   p = 1/9    E(B) = 1/9

A AB  C   p = 1/27   E(B) = 1/27
A BA  C   p = 1/27   E(B) = 1/27 

A AAB C   p = 1/81   E(B) = 1/81
A ABA C   p = 1/81   E(B) = 1/81 
A ABB C   p = 1/81   E(B) = 2/81
A BAA C   p = 1/81   E(B) = 1/81
A BAB C   p = 1/81   E(B) = 2/81
A BBA C   p = 1/81   E(B) = 2/81


So, for cases starting with A, ending with C
E(B) = 1/9  +  2*(1/27)  +  9*(1/81)



"""