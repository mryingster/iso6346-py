#!/usr/bin/python
import re

def die(message):
    print message
    quit()

ShippingNumber = raw_input("Enter Container Code (eg. PSSU210948): ")

# Check Number Format
if not re.compile('\D{4}\d{6}').match(ShippingNumber):
    die("Invalid, please ensure code follows ISO 6346 specifications.")

# Calculate Checksum
Total=0
for i in range(len(ShippingNumber)):
    Value=ShippingNumber[i]
    if not Value.isdigit():
        Value=ord(Value.lower())-ord('a')+10
        Value+=Value/11
        Total+=int(Value)*2**i

print "Check Digit:", str(Total%11%10)
