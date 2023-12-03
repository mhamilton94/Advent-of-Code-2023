import re

## Set Variables
TotalRed = 12
TotalGreen = 13
TotalBlue = 14
MaxRed = 0
MaxGreen = 0
MaxBlue = 0
num = ''
power = 0
product = 0

## Open and read file
file = open('2.1-Input.txt', 'r')

## While file has content, read each line
while True:
    content = file.readline()
    if not content:
        break
    ## Extract each result into list
    lst = re.findall(r'Game.\d*|\d*.red|\d*.green|\d*.blue', content)
    ## For each item in list
    for i in lst:
        if 'red' in i:
            ## For each character in item
            for c in i:
                if c.isdigit():
                    num = num + c
            if int(num) > MaxRed:
                MaxRed = int(num)
            num = ''
        if 'green' in i:
            ## For each character in item
            for c in i:
                if c.isdigit():
                    num = num + c
            if int(num) > MaxGreen:
                MaxGreen = int(num)
            num = ''
        if 'blue' in i:
            ## For each character in item
            for c in i:
                if c.isdigit():
                    num = num + c
            if int(num) > MaxBlue:
                MaxBlue = int(num)
            num = ''
    power = MaxRed * MaxGreen * MaxBlue
    product = product + power
    MaxRed = 0
    MaxGreen = 0
    MaxBlue = 0
print(product)  #56322
file.close()