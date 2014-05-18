#!/usr/bin/python
import sys

def die(message):
    print message
    quit()

def checkFormat(number):
    import re
    if re.compile('\D{4}\d{6}').match(number):
        return
    else:
        die("Invalid, please ensure code follows ISO 6346 specifications.")

def calculateSum(number):
    Total=0
    for i in range(len(number)):
        Value=number[i]
        if not Value.isdigit():
            Value=ord(Value.lower())-ord('a')+10
            Value+=Value/11
            Total+=int(Value)*2**i
    return Total % 11 % 10

if len(sys.argv) < 2:
    number = raw_input("Enter Container Code (eg. PSSU210948): ")

checkFormat(number)
print "Check Digit:", calculateSum(number)

