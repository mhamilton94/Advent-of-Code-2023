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
    ## Extract the numeric content and string numbers the line (regex)
    ## (?=...) matches if ... matches next, but doesn’t consume any of the string. This is called a lookahead assertion.
    ## Without this findall will not handle overlap e.g. twone only returns one, not two and one.
    temp = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))',content)
    print(temp)
    ## Combine numeric content into single string
    jn = ' '.join(temp)
    ## Replace string with numeric value
    jn = jn.replace('one', '1')
    jn = jn.replace('two', '2')
    jn = jn.replace('three', '3')
    jn = jn.replace('four', '4')
    jn = jn.replace('five', '5')
    jn = jn.replace('six', '6')
    jn = jn.replace('seven', '7')
    jn = jn.replace('eight', '8')
    jn = jn.replace('nine', '9')
    jn = jn.replace(' ', '')
    ## If there is only a single digit, duplicate this e.g. 3 -> 33
    if len(jn) == 1:
        jn = jn +jn
    ## If there are multiple digits, take only the first and last e.g. 78775 -> 75
    elif len(jn) > 2:
        jn = jn[0] + jn[-1]
    print(jn)
    ## Add the two digit line value to the running total
    total = total + int(jn)
print(total)
file.close()
