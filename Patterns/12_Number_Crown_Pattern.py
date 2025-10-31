# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321

N = int(input("Rows: "))

for i in range(1, N+1):
    for j in range(1, i+1):
        print(j,end="")
    print(" "*((N*2)-(i*2)),end="")
    for k in range(i, 0, -1):
        print(k,end="")
    print()
