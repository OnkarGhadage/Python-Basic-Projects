# 1
# 01
# 101
# 0101
# 10101

N = int(input("Size: "))

for i in range(1, N+1):
    for j in range(i, 0, -1):
        print(j%2,end="")
    print()
