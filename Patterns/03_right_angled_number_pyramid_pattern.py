# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n = int(input("Size: "))

for i in range(1,n+1):
    for j in range(i):
        print(i,end=' ')
    print()
