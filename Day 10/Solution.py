#!/bin/python3

import math
import os
import random
import re
import sys



#!/bin/python

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    s=0
    t=0
    while n>0:
        rem=n%2
        n=n//2
        if(rem==1):
            s=s+1
            if(s>=t):
                t=s
        else:
            s=0
    print(t)


