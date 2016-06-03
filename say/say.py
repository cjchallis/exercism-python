# coding: utf-8
def say(num):
    orders = ['trillion', 'billion', 'million', 'thousand', '']
    while num > 0:
        rmdr = num % 1000
        num = (num - rmdr) / 1000
        
ONES = dict(zip(range(20), ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']))

TENS = dict(zip(range(2,10),['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']))

def _three_digit(num):
    pass
    
def _two_digit(num):
    if num < 20:
        return ONES[num]
    
    return 
    