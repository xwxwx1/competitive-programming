a = input()
i = 0                                   # pointer variable
while i < len(a)-1:                     # while the string has not ended
    while 65 <= ord(a[i]) <= 90:        # is part of the uppercase alphabet
        print(a[i], end='')
        i += 1
    if a[i] == '+':                     # verb part
        print(' tighten ', end='')
    else:
        print(' loosen ', end='')
    i += 1
    while 48 <= ord(a[i]) <= 57:        # is a digit 0~9
        print(a[i], end='')
        if i + 1 >= len(a):
            break
        else:
            i += 1
    print('')                           # new line
