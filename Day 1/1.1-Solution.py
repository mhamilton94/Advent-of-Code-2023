import re

## Open and read file
file = open('1.1-Input.txt', 'r')

## Set total variable equal to 0
total = 0

## While file has content, read each line
while True:
    content = file.readline()
    if not content:
        break
    ## Extract only the numeric content of the line (regex)
    temp = re.findall(r'\d+',content)
    ## Combine numeric content into single string
    jn = ''.join(temp)
    ## If there is only a single digit, duplicate this e.g. 3 -> 33
    if len(jn) == 1:
        jn = jn +jn
    ## If there are multiple digits, take only the first and last e.g. 78775 -> 75
    elif len(jn) > 2:
        jn = jn[0] + jn[-1]
    #print(jn)
    ## Add the two digit line value to the running total
    total = total + int(jn)
print(total)
file.close()
