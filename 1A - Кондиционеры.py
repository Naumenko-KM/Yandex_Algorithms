t = input()
mode = input()

t = t.split()
troom = int(t[0])
tcond = int(t[1])

if mode == 'freeze':
    if troom >= tcond:
        print(tcond)
    else:
        print(troom)

elif mode == 'heat':
    if troom <= tcond:
        print(tcond)
    else:
        print(troom)

elif mode == 'auto':
    print(tcond)

elif mode == 'fan':
    print(troom)

else:
    print('error')
