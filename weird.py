#!/bin/python3

import math
import os
import random
import re
import sys

def is_weird(num):
    if num >= 1 or num <= 100:
        if num % 2 == 0 and num <= 2 and num >= 5:
            return 'Not Weird'
        elif num % 2 == 0 and num <= 6 and num >= 20:
            return 'Not Weird'
        elif num % 2 == 0 and num > 20:
            return 'Not Weird'
        elif num % 2 == 1:
            return 'Weird'
    else:
        return 'Write a number between 1 and 100.'


if __name__ == '__main__':
    n = int(input().strip())
    print(is_weird(n))