n = int(input("Enter pyramid height: "))
mid = n // 2
for i in range(n):
    space = " " * (n-i)
    body = "#"*(2*i+1)
    print(space+body)