a, b, c, d = list(map(int, input().split()))

if a < b:
    a, b = b, a

if c < d:
    c, d = d, c

s = a*(b+d) if a > c else c*(b+d)
h = a if a > c else c
w = b+d

s_new = a*(b+c) if a > d else d*(b+c)
if s_new < s:
    s = s_new
    h = a if a > d else d
    w = b+c

s_new = b*(a+d) if b > c else c*(a+d)
if s_new < s:
    s = s_new
    h = b if b > c else c
    w = a+d

s_new = b*(a+c) if b > d else d*(a+c)
if s_new < s:
    s = s_new
    h = b if b > d else d
    w = a+c

print(h, w)
