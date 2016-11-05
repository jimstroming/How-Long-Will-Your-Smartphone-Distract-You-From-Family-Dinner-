"""
from fivethirtyeight.com
http://fivethirtyeight.com/features/a-puzzle-will-you-yes-you-decide-the-election/

You are the only sane voter in a state with two candidates running for Senate. 
There are N other people in the state, and each of them votes completely 
randomly! Those voters all act independently and have a 50-50 chance of voting 
for either candidate. 

What are the odds that your vote changes the outcome of the election toward 
your preferred candidate?

More importantly, how do these odds scale with the number of people in the 
state? For example, if twice as many people lived in the state, how much 
would your chances of swinging the election change?
"""

""""
Let's solve it analytically first, and treat the even and off cases 
differently.

The total number of voters is N+1, since you are not included in N.
If N is even, then for your vote to matter, the vote must be tied
prior to your vote.
If N is odd, then for your vote to matter, your vote must either force
a tie or result in no tie.  So either candidate A is up by one vote, 
or candidate B is up by one vote.  

Let's work through the first few cases manually.  See if we 
notice a pattern.

For N = 1, there is one other voter.  Your vote matters.
P(1) = 1.

For N = 2, the two other voters must be split betweend candidate 
A and B for your vote to matter.  
AA
AB
BA
BB
One half of these cases are 1-1 ties, 
so P(2) = 1/2

For N=3, as long as all three do not vote for the same candidate, 
you vote matters

AAA - bad
AAB
ABA
ABB
BAA
BAB
BBA
BBB - bad

So P(3) = 3/4

To go further than this, let's construct a tree where we count
the number of votes for Candidate A

n                    
                            1/2      1/2     
1                            0        1
                             /\      /\
2                        1/4     2/4    1/4
                         0       1      2
                        /\      /\      /\
3                      1/8  3/8    3/8     1/8 
                        0    1      2       3
                       /\   /\     /\      /\
4                  1/16  4/16  6/16  4/16    1/16
                     0     1     2      3      4
                    / \  /  \   / \    / \    / \
5                1/32  5/32  10/32  10/32  5/32  1/32 
                   0    1     2      3      4     5 
                  / \  / \   / \    / \    / \   / \
6            1/64  6/64  15/64 20/64  15/64   6/64  1/64
               0     1     2     3      4       5     6
              / \   / \   / \   / \    / \     / \   / \
7        1/128 7/128 21/128 35/128 35/128 21/128 7/128 1/128             
        
Let's write out the probabilities and see if there is a pattern.

for even values of n:
P(n) = 1, 3/4, 10/16, 35/64


for odd values of n:
P(n) = 1, 2/4, 6/16, 20/64, ...
     = 1, 1/2, 3/8, 10/32, ...  
     
The numerator of both show a pattern: 1, 3, 10, 35
This is recognizable as the odd graph O3, where O3 is
2n-1 choose n-1    or C(2n-1, n-1)   

Using this, we can solve for P(n)



P(n) = 1    for n <= 1
P(n) = C(n-1,n/2 - 1)      /(2^(n-1))     for even n > 1
P(n) = C(n,  ((n+1)/2)-1 ) /(2^(n-1))     for odd n > 1   
        
                       
"""
"""
Let's run a python simulation of these rules to see if they are correct,
using a binomial coefficient routine from Andrew Dalke

"""

import sys
import random



def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0
        
        
def chanceofvotemattering(n):

    if n <= 1: return 1
    if n % 2 == 0:
        numerator =  choose(n-1,(n/2) - 1)
        denominator = 2**(n-1)
        return denominator // numerator
    else:
        numerator = choose(n, ((n+1)/2)-1) 
        denominator = 2**(n-1)
        return denominator // numerator    
print chanceofvotemattering(30000)
print chanceofvotemattering(60000)