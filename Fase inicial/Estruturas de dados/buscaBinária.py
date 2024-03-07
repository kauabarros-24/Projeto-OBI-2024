l = 1
r = 5
x = int(input())

while l <= r:
    md = l+(r-l)/2
    if md == x:
        print(md)
    elif md < x:
        l = md + 1
        print(md)
    else:
        r = md - 1
        print(md)
    
    