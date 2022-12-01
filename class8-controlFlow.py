n = 5
for i in range(n):
    for j in range(n):
        print(i, end = " ")
    print()
    
for i in range(n):
    for j in range(n):
        print(n-j, end = " ")
    print()
for i in range(n):
    for j in range(n):
        print(j+1, end = " ")
    print()
for i in range(n):
    for j in range(n):
        print(max(i+1, j+1, n-i, n-j), end = " ")
    print()
for i in range(n):
    for j in range(n):
        print(max(i,j), end = " ")
    print()
for i in range(n):
    for j in range(n):
        print(max(j,i), end = " ")
    print()
for i in range(n):
    for j in range(n):
        print(n-i-1, end = " ")
    print()










