#!/usr/bin/python

import random

print 'Python Guessing Game'
print 'By Luke Wriglesworth'
print '--------------------'

answer = random.randrange(50)
running = True
maxTries = 12
tries = 0
while running == True:     
    tries = tries + 1
    guess = int(raw_input('Guess a number: '))
    if guess == answer:
        print 'You Win!'
        running = False
    elif tries >= maxTries:
        print 'You Suck!'
        running = False
    else:
        if guess < answer:
            print 'Higher!'
        elif guess > answer:
            print 'Lower!'



