import re

## Set Variables
TotalRed = 12
TotalGreen = 13
TotalBlue = 14
MaxRed = 0
MaxGreen = 0
MaxBlue = 0
total = 0
game = ''
num = ''

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

    if MaxRed <= TotalRed and MaxGreen <= TotalGreen and MaxBlue <= TotalBlue:
        for i in lst:
            if 'Game' in i:
                ## For each character in item
                for c in i:
                    if c.isdigit():
                        game = game + c
                total = total + int(game)
                game = ''
    MaxRed = 0
    MaxGreen = 0
    MaxBlue = 0
print(total)
file.close()