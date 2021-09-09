
a = int(input())
b = int(input())
n = int(input())
m = int(input())

xmin = n*1 + (n-1)*a
xmax = n*1 + (n+1)*a

ymin = m*1 + (m-1)*b
ymax = m*1 + (m+1)*b

if xmin>ymax or ymin>xmax:
    print(-1)
else:
    min = xmin if xmin > ymin else ymin
    max = xmax if xmax < ymax else ymax

    print(min,max)